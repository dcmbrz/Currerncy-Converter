'''
This Python script allows users to convert a given base currency into multiple currencies using the Free Currency API.


'''
import requests

# This variable stores the API key required to access the Free Currency API.
API_KEY = 'fca_live_Duq8rePCjjagEoTF9Rm2tgJS6MxwRip0ffEcLGoH'

#  It constructs the base URL for the API request, including the API key.
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

# This list contains the currencies to which the base currency will be converted.
CURRENCIES= ['USD', 'CAD', 'EUR', 'AUD', 'CNY']

'''
This function takes a base currency as input, constructs the API request URL with the 
provided base currency and the list of currencies to convert, sends a GET request to the API,
and returns the JSON response containing the conversion rates.
It handles exceptions such as invalid currencies by printing a message and returning None.
'''
def convert_currency(base):
    currencies= ','.join(CURRENCIES) # this joins all the string together but adds a , in between them EX: 'USD,NI,CAD,EUR,AUD,CNY'
    url= f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    
    try: 
        response = requests.get(url)
        data=  response.json()
        return data
    
    except:
        print('Invalid currency')
        return None
    
while True:
    base= input('Enter your base currency (q to quit):').upper()

    if base == 'Q':
        print('Try Again Later')
        break

    data= convert_currency(base)
    if not data:
        continue
    
    for ticker, value in data.items():
        print(f'{ticker}:{value}')