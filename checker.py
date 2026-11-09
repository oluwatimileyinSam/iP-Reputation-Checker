import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ABUSEIPDB_KEY")

if api_key:
    print("Key loaded")
else:
    print("Key not found")

with open("ips.txt") as f:
    ips = [line.strip() for line in f if line.strip()]

url = "https://api.abuseipdb.com/api/v2/check"

headers = {
    "Accept": "application/json",
    "Key": api_key
}

for ip in ips:
    querystring = {
        "ipAddress": ip,
        "maxAgeInDays": "90"
    }
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print(ip, "-> request failed:", response.status_code)
        continue

    data = response.json()["data"]
    score = data["abuseConfidenceScore"]

    if score >= 25:
        print("SUSPICIOUS", ip, "| score:", score, "| country:", data["countryCode"], "| reports:", data["totalReports"])
    else:
        print(ip, "| score:", score, "| country:", data["countryCode"], "| reports:", data["totalReports"])