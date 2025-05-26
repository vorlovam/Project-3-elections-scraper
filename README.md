# Project-3-elections-scraper
Python scraper to extract and export 2017 Czech parliamentary election results by district.

# Election Results Scraper 🇨🇿

This project is a Python script that scrapes election results for selected districts (okrsky) from the official Czech election website (https://www.volby.cz) for the 2017 parliamentary elections.

## How it works

You run the script with two arguments:

1. A valid election result URL (e.g. for Kladno, Kutná Hora, or Mělník)
2. The name of the CSV file where the results will be saved

### Usage example

```bash
python main.py <URL> <output_file.csv>
```

Example for Kutná Hora:

```bash
python main.py https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2105 vysledky_kutna_hora.csv
```

---

## Processed districts

The following districts were scraped and saved as separate CSV files:

- [Kladno](https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xnumnuts=2103)
- [Kutná Hora](https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xnumnuts=2105)
- [Mělník](https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xnumnuts=2106)


---

## Requirements

Install required Python libraries using:

```bash
pip install -r requirements.txt
```

---

## Output

Each CSV file contains the election results for one district, including:

- Municipality name
- Number of registered voters
- Number of envelopes issued
- Number of valid votes
- Vote counts for each political party

---

## Author

Markéta Vorlová – Final project for a data analysis course 🇨🇿

