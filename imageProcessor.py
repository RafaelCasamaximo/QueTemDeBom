import cv2
import PIL
import numpy
import notify2
import pytesseract as tes
from datetime import datetime

class ImageProcessor:
    def __init__(self) -> None:
        pass

    def process(self, img):
        cvImg = numpy.array(img) 
        return self.__splitImageIntoFive(cvImg)

    def __splitImageIntoFive(self, img):
        # seg: 0:495        0:421
        # ter: 496:989      0:421
        # qua: 0:495        422:843
        # qui: 496:989      422:843
        # sex: 0:495        844:1263
        # croppedImg = img[y:y+h, x:x+w]

        cardapioPorDiaImg = {
            'Monday': img[0:421, 0:495],
            'Tuesday': img[0:421, 496:989],
            'Wednesday': img[422:843, 0:495],
            'Thursday': img[422:843, 496:989],
            'Friday': img[844:1263, 0:495]
        }
        cardapioPorDiaTxt = {
            'Monday': tes.image_to_string(cardapioPorDiaImg['Monday'], lang='por'),
            'Tuesday': tes.image_to_string(cardapioPorDiaImg['Tuesday'], lang='por'),
            'Wednesday': tes.image_to_string(cardapioPorDiaImg['Wednesday'], lang='por'),
            'Thursday': tes.image_to_string(cardapioPorDiaImg['Thursday'], lang='por'),
            'Friday': tes.image_to_string(cardapioPorDiaImg['Friday'], lang='por')
            }

        return cardapioPorDiaTxt

