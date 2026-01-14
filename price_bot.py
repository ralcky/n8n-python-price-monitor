import requests
from bs4 import BeautifulSoup
import json

def get_data():
    # The practice website
    url = "https://www.scrapethissite.com/pages/simple/"
    
    # Download and Read
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the population number (our practice "price")
    raw_data = soup.find('span', {'class': 'country-population'}).text
    number = float(raw_data.replace(',', ''))
    
    # Print as JSON so n8n can read it
    print(json.dumps([{"price": number}]))

if __name__ == "__main__":
    get_data()