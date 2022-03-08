import notify2
from datetime import datetime

class Notifier:
    def __init__(self) -> None:
        pass

    def notificaCardapioDoDia(self, cardapioTxt):
        self.sendmessage('Que tem de bom?', cardapioTxt[datetime.today().strftime('%A')])
    
    
    def sendmessage(self, title, message):
        notify2.init("Cardapio")
        notice = notify2.Notification(title, message)
        notice.show()
        return
        