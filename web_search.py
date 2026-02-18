import requests

def web_search(query):
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    return response.json()
