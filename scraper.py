import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
import argparse

def clean_number(value):
    """Extracts numeric part from a string and converts it to an integer."""
    number_match = re.match(r'(\d+)', value.replace(',', ''))
    return int(number_match.group(0)) if number_match else None

def scrape_table_data(url):
    """Scrapes table data from the specified URL and returns it as a DataFrame."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'example'})
    # print(table)
    if not table:
        raise ValueError("Table with the specified ID not found in the HTML content.")

    data = []
    for row in table.find('tbody').find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 5:
            data.append({
                'Category': cols[0].text.strip(),
                'Particulars': cols[1].text.strip(),
                'Civil': clean_number(cols[2].text.strip()),
                'Criminal': clean_number(cols[3].text.strip()),
                'Total': clean_number(cols[4].text.strip())
            })

    return pd.DataFrame(data)

def save_to_csv(df, filename):
    """Saves the DataFrame to a CSV file."""
    df.to_csv(filename, index=False)

def convert_to_dict(df):
    """Converts the DataFrame to a dictionary."""
    return df.to_dict(orient='records')

def main():
    parser = argparse.ArgumentParser(description="Scrape judicial data from a webpage.")
    parser.add_argument('--url', type=str, required=True, help="The URL of the page to scrape.")
    parser.add_argument('--output', type=str, choices=['csv', 'dict'], default='csv', help="Output format: csv or dict.")
    parser.add_argument('--filename', type=str, default="judicial_data.csv", help="The name of the output file (for CSV output).")
    
    args = parser.parse_args()

    df = scrape_table_data(args.url)

    if args.output == 'csv':
        filename = args.filename
        save_to_csv(df, filename)
        print(f"Data saved to {filename}")
    elif args.output == 'dict':
        data_dict = convert_to_dict(df)
        print(data_dict)

if __name__ == "__main__":
    main()