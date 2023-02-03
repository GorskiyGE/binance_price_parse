import requests
import json
import io
import re

def get_ticker(coin1='ETH', coin2='USDT'):
    response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={coin1}{coin2}')
    q = response.text
    x = q.split('"')
    q = x[3]+" "+x[5]+"="+x[7]
    print(q)

def get_ticker_all():
    response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price')
    q = response.text
    x = re.split('[^A-Z0-9.]', q)
    x = [x for x in x if x]
    i=1
    for i in range(len(x)):
        if i%2==1:
            print(x[i-1]+" price="+x[i])
            

def main():
    word_input=input('Do you want prices for a specific pair of tokens? Enter "yes" or "no"\n')
    if word_input=='yes':
        print("enter two tokens. If you do not enter anything, the price for ETH/USDT\n")
        coin1=input("enter the first token, for example: ETH : ")
        coin2=input("enter the first token, for example: USDT : ")
        if coin1=='' or coin2=='':
            get_ticker()
        else:
            get_ticker(coin1, coin2)
    elif word_input=='no':
        get_ticker_all()
    else:
        print("entered something else\n")

if __name__ == '__main__':
    main()
