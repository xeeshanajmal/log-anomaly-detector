# src/shodan_client.py

import shodan
from config import SHODAN_KEY

api = shodan.Shodan(SHODAN_KEY)

def search_devices(query, limit=10):
    results = api.search(query, limit=limit)
    return results['matches']
