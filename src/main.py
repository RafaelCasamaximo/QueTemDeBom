from scrapping import Scrapping
from interface import Interface
from datetime import date
import pprint

def main():
    scrapping = Scrapping()
    cardapio = scrapping.completeCardapio

    # pprint.pprint(cardapio)    
    interface = Interface('O que tem de bom hoje? ' + getDiaDaSemana())
    interface.populateText(convertToPrettyText(cardapio[getDiaDaSemana()]))
    interface.start()
    pass

def getDiaDaSemana():
    sem = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]
    num = date.today().weekday()
    return sem[num]


def convertToPrettyText(cardapioDoDia):
    prettyText = ''
    for item in cardapioDoDia:
        prettyText += item['Alimento'] + '\n'
        for tag in item['Tags']:
            prettyText += tag + '\n'
        prettyText += '\n\n'

        
    return prettyText

if __name__ == "__main__":
    main()
    pass

