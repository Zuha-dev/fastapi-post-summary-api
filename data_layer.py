import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    return data