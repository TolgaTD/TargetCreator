# TargetCreator
This code scans internet targets using BinaryEdge API with a query, extracts IPs, and saves them. Useful for identifying security vulnerabilities or errors.
Using the BinaryEdge API, the code retrieves results over a specific range of pages (e.g., first 15 pages) based on a given search query and saves the obtained IP addresses from these results into a file.

Here's what the code block can do:

Accessing the API: It enables access to the BinaryEdge API, which scans internet targets based on specific search queries to gather various information.

Taking User Input: It prompts the user to input a search query. The user can enter a query term like "Apache," for example.

Scanning Specific Number of Pages: By making API requests throughout a specific page range (e.g., first 15 pages), it fetches results. This facilitates a more comprehensive outcome by scanning more targets.

Processing Results: By parsing the JSON response from the API, it processes the results. It extracts the IP address of each target to create a list.

Saving IP Addresses to File: It records the obtained IP addresses into a file. This proves useful for later analysis or utilization of these IP addresses.

Generating File Names: It generates a file name matching the user-entered search query. This provides additional information about the content of the saved file.

In summary, this code block employs the BinaryEdge API with a specified search query to scan internet targets, extract IP addresses, and save them into a file. Such scans can be utilized by cybersecurity professionals or researchers to detect security vulnerabilities or configuration errors within the targets.
