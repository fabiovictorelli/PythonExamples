# My first Python
# Fabio D Victorelli
# 06/29/2022

import googletrans
from googletrans import Translator


def traduzir(texto, idioma):
    trans = Translator()
    textotraduzido = trans.translate(texto, dest=idioma).text
    print(texto, '=>', ' no idioma (', idioma, ')', textotraduzido)


traduzir("The book is on the table", "pt")


# chamando a funcao traduzir
textoptraduzir = input("Write something in English : ")
linguagem = input("enter with some languague, Ex pt or es :")
traduzir(textoptraduzir, linguagem)
