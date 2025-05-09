import requests
import os

def shorten_url(long_url):
    api_key = os.getenv("GPLINK_API_KEY")
    try:
        response = requests.get(f"https://gplinks.in/api?api={api_key}&url={long_url}")
        return response.json().get("shortenedUrl", long_url)
    except Exception:
        return long_url