import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ABUSEIPDB_KEY")

if api_key:
    print("Key loaded")
else:
    print("Key not found")