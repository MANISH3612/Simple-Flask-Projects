import requests
def quote_day():
    base = "http://quotes.rest/qod.json"
    r = requests.get(base).json()
    return r