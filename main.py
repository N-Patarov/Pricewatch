import requests
from bs4 import BeautifulSoup
import time


def main():
    print(" WELLCOME TO PRICEWATCH ")
    print(" by NPatarov ")
    run=True
    while run:
        ask=input("CHOOSE btc, eth, xrp or q to quit: ").lower()
        if ask == "xrp":
            xrp()
        elif ask == "xrpt":
            xrpt()
        elif ask == "btc":
            btc()
        elif ask == "btct":
            btct()
        elif ask == "eth":
            eth()
        elif ask == "etht":
            etht()
        elif ask == "q":
            run=False
        

def xrp():
    link = requests.get("https://coinmarketcap.com/currencies/xrp/")
    soup = BeautifulSoup(link.content,'html.parser')
    price =  soup.find(class_='priceValue___11gHJ')
    print("XRP: "+price.text)
    
    
def btc():
    link = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
    soup = BeautifulSoup(link.content,'html.parser')
    price =  soup.find(class_='priceValue___11gHJ')
    print("BTC: "+price.text)

def eth():
    link = requests.get("https://coinmarketcap.com/currencies/ethereum/")
    soup = BeautifulSoup(link.content,'html.parser')
    price =  soup.find(class_='priceValue___11gHJ')
    print("ETH: "+price.text)


def xrpt():
    while True:
        link = requests.get("https://coinmarketcap.com/currencies/xrp/")
        soup = BeautifulSoup(link.content,'html.parser')
        price =  soup.find(class_='priceValue___11gHJ')
        print("XRP: "+price.text)
        time.sleep(30)

def btct():
    while True:
        link = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
        soup = BeautifulSoup(link.content,'html.parser')
        price =  soup.find(class_='priceValue___11gHJ')
        print("BTC: "+price.text)
        time.sleep(30)
        
def etht():
    while True:
        link = requests.get("https://coinmarketcap.com/currencies/ethereum/")
        soup = BeautifulSoup(link.content,'html.parser')
        price =  soup.find(class_='priceValue___11gHJ')
        print("ETH: "+price.text)
        time.sleep(30)


if __name__ == '__main__':
    main()
    