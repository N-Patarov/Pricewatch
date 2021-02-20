import requests
from bs4 import BeautifulSoup
import time


def main():
    print(" WELLCOME TO PRICEWATCH ")
    print(" by NPatarov ")
    lst=["btc","eth","xrp","dot","doge","xmr"]
    cryptos=str(lst)
    run=True
    while run:
        print("SUPORTED CRYPTOCURRENCIES"+cryptos)
        ask=input("CHOOSE crypto, all to display all or q to quit: ").lower()
        if ask == "xrp":
            xrp()
        elif ask == "xmr":
            xmr()
        elif ask == "doge":
            doge()
        elif ask == "btc":
            btc()
        elif ask == "eth":
            eth()
        elif ask == "dot":
            dot()
        elif ask == "all":
            btc()
            eth()
            xrp()
            doge()
            xmr()
            dot()
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

def dot():
    link = requests.get("https://coinmarketcap.com/currencies/polkadot/")
    soup = BeautifulSoup(link.content,'html.parser')
    price =  soup.find(class_='priceValue___11gHJ')
    print("DOT: "+price.text)

def xmr():
    link = requests.get("https://coinmarketcap.com/currencies/monero/")
    soup = BeautifulSoup(link.content,'html.parser')
    price =  soup.find(class_='priceValue___11gHJ')
    print("XMR: "+price.text)

def doge():
    link = requests.get("https://coinmarketcap.com/currencies/dogecoin/")
    soup = BeautifulSoup(link.content,'html.parser')
    price =  soup.find(class_='priceValue___11gHJ')
    print("DOGE: "+price.text)

if __name__ == '__main__':
    main()
    