from scrapping import Scrapping
from interface import Interface
from datetime import date
from PIL import Image, ImageTk

import pprint

def main():
    scrapping = Scrapping()
    cardapio = scrapping.completeCardapio

    # pprint.pprint(cardapio)    
    interface = Interface('O que tem de bom hoje? ')

    image = None
    if getDiaDaSemana() == "Sábado" or "Domingo":
        image = Image.open("./assets/cardapioTriste.png")
    else:
        image = Image.open("./assets/cardapioFeliz.png")
    photo = ImageTk.PhotoImage(image)
    interface.populateImage(photo)

    try:
        interface.populateText(convertToPrettyText(cardapio[getDiaDaSemana()]))
    except:
        interface.populateText("Hoje não tem nada no RU! :(\nSegunda-Feira a gente te fala o novo cardápio! ;)")
    interface.start()
    pass

def getDiaDaSemana():
    sem = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
    num = date.today().weekday()
    return sem[num]


def convertToPrettyText(cardapioDoDia):
    prettyText = ''
    for item in cardapioDoDia:
        prettyText += item['Alimento'].upper() + '\n'
        for tag in item['Tags']:
            prettyText += tag + '\n'
        prettyText += '\n'

        
    return prettyText

if __name__ == "__main__":
    main()
    pass

