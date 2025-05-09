import requests
import config

def shorten_url(url, service):
    api_key = config.SHORTENER_API_KEYS.get(service)
    if not api_key:
        return None
    # Example API call to a shortener service
    response = requests.get(f"https://api.{service}.com/shorten", params={'key': api_key, 'url': url})
    if response.status_code ==
