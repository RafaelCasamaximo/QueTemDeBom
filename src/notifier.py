from datetime import datetime
from notifypy import Notify 


class Notifier:
    def __init__(self) -> None:
        pass

    def notificaCardapioDoDia(self, cardapioTxt):
        print(cardapioTxt[datetime.today().strftime('%A')])
        self.sendMessage('Que tem de bom?', cardapioTxt[datetime.today().strftime('%A')])

    
    def sendMessage(self, title, message):
        notification = Notify()
        notification.title = title
        notification.message = message
        notification.send()
        return
        