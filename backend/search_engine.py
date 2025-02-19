import requests
from config import settings

def fetch_search_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={settings.GOOGLE_API_KEY}&cx={settings.SEARCH_ENGINE_ID}&q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return [{'title': item['title'], 'link': item['link'], 'snippet': item['snippet']} for item in data.get('items', [])]
    return {'error': 'Search failed'}
