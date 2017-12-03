import csv
import json
import requests
import sys

api_key = 'API_KEY'

def fetch_engagement_count(url):
    result = requests.get("https://engagedcount.com/api",
                          params={'apikey': api_key, 'url': url})
    if result.status_code == 200:
        return result.json()
    else:
        raise RuntimeError('Unsuccessful response')

def fetch_engagement_counts(input_file):
    with open(input_file) as urls:
        return [[url, json.dumps(fetch_engagement_count(url))] for url in urls.read().splitlines()]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('You need to supply an input and output file.')
        print('Example: ./fetch-engagement-counts.py urls.txt urls-with-stats.csv')
        exit(1)

    url_file = sys.argv[1]
    results = sys.argv[2]

    urls_with_metrics = fetch_engagement_counts(url_file);
    with open(results, 'w') as out:
        writer = csv.writer(out);
        for row in urls_with_metrics:
            writer.writerow(row)
