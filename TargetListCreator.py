import requests  # requests kütüphanesini kullanabilmek için import ediyoruz

BINARYEDGE_API_KEY = "YOUR_BINARYEDGE_API_KEY"  # BinaryEdge API anahtarınızı buraya girin
search_query = input("Enter the search query: ")  # Kullanıcıdan arama sorgusunu alıyoruz
num_pages = 15  # İlk 15 sayfayı taramak için sayfa sayısı

ip_addresses = []  # Boş bir liste oluşturuyoruz, bu listede IP adreslerini saklayacağız

# Belirtilen sayfa sayısı kadar döngü oluşturuyoruz
for page in range(1, num_pages + 1):
    # API isteği için URL oluşturuyoruz, arama sorgusu ve sayfa numarası dahil ediliyor
    url = f"https://api.binaryedge.io/v2/query/search?query={search_query}&page={page}"

    # API isteği için gereken başlıkları (headers) belirliyoruz
    headers = {
        "X-Key": BINARYEDGE_API_KEY
    }

    # API isteği yaparak yanıtı alıyoruz
    response = requests.get(url, headers=headers)
    
    # Yanıtı JSON formatına çözümleyerek "data" değişkenine atıyoruz
    data = response.json()

    # Her bir "event" için IP adresini çıkarıp listeye ekliyoruz
    for event in data["events"]:
        ip_addresses.append(event["target"]["ip"])

# Oluşturulan IP adresleri dosyasını arama sorgusu ile aynı isimde kaydediyoruz
file_name = f"{search_query.replace(' ', '_')}_ip_addresses.txt"
with open(file_name, "w") as file:
    for ip in ip_addresses:
        file.write(ip + "\n")

# Kullanıcıya kaydedilen dosyanın adını bildiriyoruz
print(f"IP addresses saved to {file_name}")
