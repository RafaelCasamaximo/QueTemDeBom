from scrapper import Scrapper
from imageProcessor import ImageProcessor
from notifier import Notifier

def main():
    scrapper = Scrapper()
    cardapioUrl = scrapper.getCardapioImageURL()
    cardapioImg = scrapper.getImageFromURL(cardapioUrl)

    imageProcessor = ImageProcessor()
    cardapioPorDiaTxt = imageProcessor.process(cardapioImg)

    notifier = Notifier()
    notifier.notificaCardapioDoDia(cardapioPorDiaTxt)
    pass

if __name__ == '__main__':
    main()

