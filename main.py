
"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Markéta Vorlová
email: vorlovamarketa@seznam.cz
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    response = requests.get(url)
    return response.text

def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all("table")
    party_tables = tables[1:3]  # druhá a třetí tabulka
    all_data = []

    for table in party_tables:
        rows = table.find_all("tr")[2:]  # přeskočíme hlavičky
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 4:
                data = {
                    "party_number": cols[0].text.strip(),
                    "party_name": cols[1].text.strip(),
                    "votes": cols[2].text.strip().replace('\xa0', ''),
                    "percent": cols[3].text.strip().replace('\xa0', '')
                }
                all_data.append(data)
    return all_data

def save_to_csv(data, output_file):
    if data:
        keys = data[0].keys()
        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Saved results to: {output_file}")
    else:
        print("No data to save.")

def scrape(url, output_file):
    html = fetch_html(url)
    data = parse_data(html)
    save_to_csv(data, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <URL> <output.csv>")
        sys.exit(1)
    scrape(sys.argv[1], sys.argv[2])
