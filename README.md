# IP Reputation Checker

A small Python script that checks IP addresses against the AbuseIPDB API. It reads the IPs from a text file, looks up each one, and marks the risky ones.

## How it works

The script reads ips.txt, one address per line. For each address it asks AbuseIPDB for the abuse score, the country, and the number of reports. Any IP with a score of 25 or higher is printed with SUSPICIOUS in front.

## Setup

1. Clone the repo and open the folder.
2. Create a virtual environment and activate it.
3. Run: pip install requests python-dotenv
4. Get a free API key from abuseipdb.com.
5. Make a file called .env and put this in it: ABUSEIPDB_KEY=your_key_here
6. Add the IPs you want to check to ips.txt.
7. Run: python3 checker.py

The .env file is in .gitignore, so the key stays on your own machine.

## Example output

    8.8.8.8 | score: 0 | country: US | reports: 188
    SUSPICIOUS 181.215.65.37 | score: 47 | country: US | reports: 37

## What I learned

I wrote this while learning Python. My key would not load at first because of a typo in the variable name. I also hit a Git merge conflict and had to fix it by hand. I learned to keep API keys out of the code and out of GitHub.

## Next

I want to point it at real log files and save the results to a file.