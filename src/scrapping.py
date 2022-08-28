import requests
from bs4 import BeautifulSoup
import urllib.request
import pprint

class Scrapping:
    def __init__(self) -> None:
        # Faz a request para o site
        selections = self.getCardapioFromURL()
        # print(selections)
        # Extrai as opções da semana
        self.completeCardapio = self.getDiasDaSemanaFromCardapio(selections)
        pass


    def getCardapioFromURL(self):
        htmlData = self.getData("https://sites.uel.br/sebec/cardapio/")
        soup = BeautifulSoup(htmlData, 'html.parser')
        selection1 = soup.find("div", class_="wp-container-3 wp-block-columns")
        selection2 = soup.find("div", class_="wp-container-6 wp-block-columns")
        selection3 = soup.find("div", class_="wp-container-9 wp-block-columns")
        # print(selection1, selection2, selection3)
        return [selection1, selection2, selection3]


    def getData(self, url):
        r = requests.get(url)
        return r.text

    def getDiasDaSemanaFromCardapio(self, selections):
        cardapio = {
            'Segunda-Feira': selections[0].find("div", class_="wp-container-1 wp-block-column"),
            'Terça-Feira': selections[0].find("div", class_="wp-container-2 wp-block-column"),
            'Quarta-Feira': selections[1].find("div", class_="wp-container-4 wp-block-column"),
            'Quinta-Feira': selections[1].find("div", class_="wp-container-5 wp-block-column"),
            'Sexta-Feira': selections[2].find("div", class_="wp-container-7 wp-block-column"),
        }

        cardapio = {
            'Segunda-Feira': cardapio['Segunda-Feira'].findAll("p"),
            'Terça-Feira':  cardapio['Terça-Feira'].findAll("p"),
            'Quarta-Feira':  cardapio['Quarta-Feira'].findAll("p"), 
            'Quinta-Feira':  cardapio['Quinta-Feira'].findAll("p"),
            'Sexta-Feira':  cardapio['Sexta-Feira'].findAll("p"),
        }

        # cardapio.remove(cardapio["sexta-feira"])
        # cardapio["sexta-feira"] = "peixe"

        filteredCardapio = {}
        for key, value in cardapio.items():
            filteredCardapio[key] = [self.filterParagraphFromCardapio(p) for p in value]
        # print(filteredCardapio)
        return filteredCardapio    
        

    def filterParagraphFromCardapio(self, paragraph):

        tagsEnum = {
            'Contém Lactose, Queijo, Ovo, Origem Animal': 'background-color:rgba(0, 0, 0, 0);color:#f10606',
            'Opções para Vegetarianos': 'background-color:rgba(0, 0, 0, 0);color:#45cc4b',
            'Contém Molho Shoyu': 'background-color:rgba(0, 0, 0, 0)',
            'Pode conter Pimenta': 'background-color:rgba(0, 0, 0, 0);color:#fde321',
            'Contém Molho de Tomate': 'background-color:rgba(0, 0, 0, 0);color:#9d06d9',
            'Contém Glúten': 'background-color:rgba(0, 0, 0, 0);color:#0935d3',
            'Servidos Diariamente': 'background-color:rgba(0, 0, 0, 0);color:#200ae3'
        }

        inverseTagsEnum = {v: k for k, v in tagsEnum.items()}

        tags = paragraph.findAll("mark")
        tagsStyles = []
        for tag in tags:
            tagsStyles.append(tag["style"])
        
        alimentoTags = []
        for tagStyle in tagsStyles:
            try:
                alimentoTags.append(inverseTagsEnum[tagStyle])
            except:
                pass

        item = {
            'Alimento': paragraph.get_text(" ").replace('▄','').title(),
            'Tags': alimentoTags,
        }
        return item

