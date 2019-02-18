import urllib.request, json
from .models import Quote


def get_quotes(id):
    '''
    Function that gets the json responce to quotes url request
    '''
    quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quotes_url) as url:
        quotes_details_data = url.read()
        quotes_details_response = json.loads(quotes_details_data)

        quote_object = None

        if quotes_details_response:
            id = quotes_details_response.get('id')
            author = quotes_details_response('author')
            quote = quotes_details_response('quote')
            permalink = quotes_details_response('permalink')
    

            quote_object = Quote(id, author, quote, permalink)

        return quote_object


    