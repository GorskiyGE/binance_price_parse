import requests
from time import gmtime, strftime


def get_ticker(coin1='ETH', coin2='USDT'):
    response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={coin1}{coin2}')
    q = response.text
    x = q.split('"')
    return x[7]

def main():
    print('Input pair tokens')
    coin1=input("enter the first token, for example: ETH : ")
    coin2=input("enter the first token, for example: USDT : ")
    temp =  float(get_ticker(coin1, coin2))
    h = int(strftime("%H", gmtime())) + 3
    m = int(strftime("%M", gmtime()))
    temp_date = (h+1)*100 + m
    while True:
        h1 = int(strftime("%H", gmtime())) + 3
        m1 = int(strftime("%M", gmtime()))
        temp_date_1 = h*100 + m
        price = float(get_ticker())
        if price < temp*0.99 and temp_date >= temp_date_1:
            print("The price has fallen by 1% from the maximum price in the last hour, the current price is:", price)
            temp = price
        if temp_date <= temp_date_1:
                temp_date = (h+1)*100 + m
                print("next our")
                temp = float(get_ticker(coin1, coin2))


if __name__ == '__main__':
    main()
