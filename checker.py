import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ABUSEIPDB_KEY")

if api_key:
    print("Key loaded")
else:
    print("Key not found")

url = "https://api.abuseipdb.com/api/v2/check"

querystring = {
    "ipAddress": "181.215.65.37",
    "maxAgeInDays": "90"
    }

headers = {
    "Accept": "application/json",
    "Key": api_key
}

response = requests.get(url, headers=headers, params=querystring)
print(response.text)