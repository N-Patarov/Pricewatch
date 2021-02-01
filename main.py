import requests
from bs4 import BeautifulSoup


def main():
    print(" WELLCOME TO PRICEWATCH ")
    print(" by NPatarov ")
    run=True
    while run:
        ask=input("CHOOSE btc, eth, xrp or q to quit: ").lower()
        if ask == "xrp":
            xrp()
        elif ask == "btc":
            btc()
        elif ask == "eth":
            eth()
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


if __name__ == '__main__':
    main()
    