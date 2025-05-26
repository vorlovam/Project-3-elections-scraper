import sys
import requests
from bs4 import BeautifulSoup
import csv

def scrape(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table")

    # Získání tabulek s hlasy pro strany (druhá a třetí tabulka)
    party_tables = tables[1:3]
    all_data = []

    for table in party_tables:
        rows = table.find_all("tr")[2:]  # Přeskočíme hlavičky
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

    if all_data:
        keys = all_data[0].keys()
        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_data)

        print(f"Saved results to: {output_file}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <URL> <output.csv>")
        sys.exit(1)
    scrape(sys.argv[1], sys.argv[2])
