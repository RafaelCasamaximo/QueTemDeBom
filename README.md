# QueTemDeBom?

![Restaurante Universitário - Universidade Estadual de Londrina](https://operobal.uel.br/wp-content/uploads/2020/11/1605534196167blob.png)

As aulas presenciais voltaram na UEL e o RU também. Isso cria uma dúvida na nossa cabeça no começo de cada dia: *O que tem de bom no RU hoje?*

Por conta disso eu criei um script em Python que:
- Faz a requisição do cardápio do dia no site do RU - UEL;
- Salva a imagem localmente;
- Recorta a imagem em 5 partes (cada dia da semana);
- Converte a imagem do cardápio de cada dia em texto;
- Envia uma notificação para o sistema operacional com o conteúdo;

## Como instalar

- É necessário Python 3 sou superior;
- Todos os requerimentos do python estão em `requirements.txt`, para instalar eles use `pip install -r requirements.txt`;
- Instalar [PyTesseract](https://tesseract-ocr.github.io/);
- Para melhor reconhecimento do texto é necessário [instalar o treinamento de linguagem em português](https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata);
- Por fim, é necessário adicionar o script ao startup do sistema. Isso pode ser feito através da GUI do Gnome ou também através dos [scripts de startup](https://smallbusiness.chron.com/adobe-creative-cloud-grow-business-13771091.html); 

## Como executar
- O comando para executar o script é `python3 main.py`. Isso enviará uma notificação para o sistema contendo as informações do cardápio do dia do RU - UEL;

## TODOs
- Adicionar suporte para Windows;
- Adicionar integração com o Google Calendar API para poder adicionar na agenda;
- Complementar README com informações de como instalar o PyTesseract no Linux e Windows;
- Refatorar código para incluir [PEP-484](https://www.python.org/dev/peps/pep-0484/);

## Contribuições:
Se você é dá UEL ou de algum outro lugar e tem vontade de contribuir sinta-se a vontade!

### Guidelines
- Novos arquivos em camelCase;
- Nomes de métodos em camelCase;
- Todo o código deve estar dentro da função `main()` em `main.py` ou de uma classe com o nome correspondente ao nome do arquivo;