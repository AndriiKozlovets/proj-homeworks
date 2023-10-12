import requests


def search_gifs(api_key, query):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": query,
        "limit": 3
    }
    response = requests.get(url, params=params)
    data = response.json()
    gifs = [item['images']['original']['url'] for item in data['data']]
    return gifs


api_key = "lwZGuUKXitiTsBd4ppeWgcMpV5tTfV6Z"
query = input("Enter a word to search for GIF images: ")
gifs = search_gifs(api_key, query)
for gif in gifs:
    print(gif)
