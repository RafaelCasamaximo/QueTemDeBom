import requests 
from bs4 import BeautifulSoup 
import urllib.request
from PIL import Image

class Scrapper:
    def __init__(self) -> None:
        pass

    def getCardapioImageURL(self):
        htmldata = self.getdata("http://www.uel.br/ru/pages/cardapio.php") 
        soup = BeautifulSoup(htmldata, 'html.parser') 
        allImages = soup.find_all('img')
        cardapioImage = allImages[5]['src']
        return cardapioImage

    def getdata(self, url): 
        r = requests.get(url) 
        return r.text 
        
    def getImageFromURL(self, url):
        urllib.request.urlretrieve(url, "./assets/cardapio.png")
        return Image.open("./assets/cardapio.png")
    