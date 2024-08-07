import requests
from bs4 import BeautifulSoup
def scrape_website(url):
  try:
    response=reuqests.get(url)
    response.raise_for_status()
    status codes 
    soup=BeautifulSoup(response.content,'html.parser')
    titles = []
    for h1 in soup.find_all('h1'):
      titles.append(h1.text.strip())
      return titles
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None
    url="https://www.example.com"
    extracted_titles=scrape_website(url)
    if extracted_titles:
      print(f"Extracted titles:{extracted_titles}")
    else:
      print("Failed to extract titles.")