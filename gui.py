import PySimpleGUI as psg
import requests
import io
import re

def get_ticker_all():
    #response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price')
    #q = response.text
    q= ""
    parametrs = ['ETHUSDT','BTCUSDT','UNIUSDT' ]
    for i in 1,2,3:

        response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={parametrs[i-1]}')
        q += response.text
    x = re.split('[^A-Z0-9.]', q)
    x = [x for x in x if x]
    i=1
    coin_name = []
    coin_price = []  
    for i in range(len(x)):
        if i%2==1:
            coin_name.append(x[i-1])
    psg.theme('SandyBeach')
#define layout
    layout=[[psg.Text('Choose coin pair:',size=(20, 1), font='Lucida',justification='left')],
            [psg.Combo(coin_name,default_value='ETHUSDT',size=(20, 1),readonly=True, key='pair'), psg.Text('', key='TEXT')]]
#Define Window
    win =psg.Window('Binance price',layout).Finalize()
    while True:
        win.refresh()
        event, values = win.read(timeout=0)
        #response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price')
        #q = response.text
        q= ""
        parametrs = ['ETHUSDT','BTCUSDT','UNIUSDT' ]
        
        for i in 1,2,3:
            response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={parametrs[i-1]}')
            q += response.text
            #print(q)       
        x = re.split('[^A-Z0-9.]', q)
        x = [x for x in x if x]
        i=1
        coin_name = []
        coin_price = []  
        for i in range(len(x)):
            if i%2==1:
                coin_name.append(x[i-1])
             #   print(x[i-1])
        if event == psg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        else:
            b = False
            j = 1
            a= "" 
            while b != True:
                if j%2==1 and x[j-1]==values['pair']: 
                    a = x[j]
                #print(a)
                    b = True
                else:
                    j+=1
            win['TEXT'].update(a)
            
    win.close()


def main():
    get_ticker_all()

if __name__ == '__main__':
    main()
