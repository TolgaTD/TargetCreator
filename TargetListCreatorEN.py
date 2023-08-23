import requests  # Importing the requests library to use

BINARYEDGE_API_KEY = "YOUR_BINARYEDGE_API_KEY"  # Enter your BinaryEdge API key here
search_query = input("Enter the search query: ")  # Taking the search query input from the user
num_pages = 15  # Number of pages to scan, set to 15

ip_addresses = []  # Creating an empty list to store IP addresses

# Creating a loop for the specified number of pages
for page in range(1, num_pages + 1):
    # Constructing the URL for the API request, including search query and page number
    url = f"https://api.binaryedge.io/v2/query/search?query={search_query}&page={page}"

    # Setting the required headers for the API request
    headers = {
        "X-Key": BINARYEDGE_API_KEY
    }

    # Sending the API request and receiving the response
    response = requests.get(url, headers=headers)
    
    # Parsing the response as JSON and storing it in the "data" variable
    data = response.json()

    # Extracting and appending the IP address for each "event" to the list
    for event in data["events"]:
        ip_addresses.append(event["target"]["ip"])

# Saving the generated IP addresses to a file named after the search query
file_name = f"{search_query.replace(' ', '_')}_ip_addresses.txt"
with open(file_name, "w") as file:
    for ip in ip_addresses:
        file.write(ip + "\n")

# Notifying the user about the saved file name
print(f"IP addresses saved to {file_name}")
