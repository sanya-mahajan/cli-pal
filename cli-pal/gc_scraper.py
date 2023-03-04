import requests
from bs4 import BeautifulSoup




def get_search_data(query):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = f"https://www.google.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    for result in soup.select(".tF2Cxc"):
        title = result.select_one(".DKV0Md").text
        link = result.a["href"]
        print(title, link)

