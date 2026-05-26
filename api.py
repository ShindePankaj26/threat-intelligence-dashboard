import requests

url = "https://api.abuseipdb.com/api/v2/blacklist"

headers = {
    'Key': 'YOUR_API_KEY',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.json())