from tkinter import *
from tkinter import ttk, filedialog

class Interface:
    def __init__(self, title):
        # Inicia biblioteca e define o nome da janela
        self.root = Tk()
        self.root.maxsize(400, 600) 
        self.root.title(title)
        # Define o tamanho mínimo da janela
        # self.root.minsize(500, 500)
        pass

    def populateImage(self, content):
        self.imagem = Label(self.root, text = "Cardápio do dia", image = content)
        self.imagem.image = content
        self.imagem.pack()
        pass

    def populateText(self, content):
        text = Label(self.root, text=content, width=100, height=100)
        text.pack()
        pass

    def start(self):
        self.root.mainloop()
