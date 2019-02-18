import requests

def get_quotes():
    quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    response = requests.get(quotes_url)

    quotes = response.json()

    return quotes

