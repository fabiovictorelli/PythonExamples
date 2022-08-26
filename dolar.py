# Show Exchange Dollar vs Brazilian Reais of today rate from 3 sites
# fabiovictorelli@gmail.com
# Mon Aug 23 11:33:21 EDT 2022


"""
 Here we are getting the Currency Exchange USD to BRL (Dollar to Real Brazil)
"""

import sys
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import Request, urlopen
from html.parser import HTMLParser

# SITEGOOGLE = "https://www.google.com/finance/quote/USD-BRL?hl=en"

TAGDOLAR = "data-rate"
TAGDOLAR2 = "Dólar Turismo"
DOLARATUAL = '1.00'


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        # if tag == 'meta':
        #    print("achei uma tag == meta")
        if tag == 'div':
            # print("achei uma tag == div")
            pos = self.getpos()
            if attrs.__len__() > 0:
                # print("\tAttributes:")
                for a in attrs:
                    # print("\t", a[0], "=", a[1])  # atributo "name" and "value"
                    # if (a[0] == 'data-rate'):

                    if (a[0] == TAGDOLAR):
                        # print("Achei TAG_DOLAR = ", TAGDOLAR)
                        dolaratual = str(a[1])
                        # print("dolar atual = ", dolaratual)
                        DOLARATUAL = float(dolaratual)
                        print("%2.2f" % DOLARATUAL)


def Mostra_Dolar_FXRATE():
    SITE = "https://fx-rate.net/USD/BRL/"
    print("SITE 1: ", SITE,
          "                                            ===> R$", end='')
    # instancializa a classe MyHTMLParser
    parser = MyHTMLParser()
    # Atencao sempre tenho que passar o headers abaixo p nao retornar: 403 Forbiden
    # headers = "'User-Agent': 'Mozilla/5.0'"
    req = Request(SITE, headers={'User-Agent': 'Mozilla/5.0'})
    web_page = str(urlopen(req).read())
    tamweb_page = sys.getsizeof(web_page)
    # print("Li Pagina html do site: ", SITE, "tamanho da pagina=", tamweb_page)
    # print("\nPagina =", web_page)              # Mostra a pagina lida

    # print("Agora vamos trabalhar com a pagina HTML na MyHTMLparser")
    parser.feed(web_page)


def PegaValoresDollarAWESOMEAPI(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    # print("theJSON = " + str(theJSON))
    # now we can access the contents of the JSON like any other Python object
    if "high" in theJSON["USD"]:
        dolaralto = theJSON["USD"]["high"]
        # print("Achei USD high: %2.2f" % float(dolaralto))
    if "low" in theJSON["USD"]:
        dolarbaixo = theJSON["USD"]["low"]
        # print("Achei USD low: %2.2f" % float(dolarbaixo))
    return (dolarbaixo, dolaralto)


def MostraValorDolarAWESOMEAPI():

    urlData = "https://economia.awesomeapi.com.br/json/all/USD-BRL"
    webUrl = urllib.request.urlopen(urlData)
    # print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        dollow, dolhig = PegaValoresDollarAWESOMEAPI(data)
    else:
        print("Recebi codig o erro, cannot parse results")
        exit()

    print("SITE 2: ", urlData, "                     ===>", end='')
    print(" R$%2.2f" % ((float(dollow) + float(dolhig)) / 2))
    #print("         media do dolar baixo =",dollow, " e   dolar alto=", dolhig)


def MostraDolarTurismo():
    # Peguei de https://github.com/fernandomaia/dolar-turismo/commit/f812f6869dd516e5dfbdc8c42b665c8d1ec5cf3a
    # headers = {
    #    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    headers = {'User-Agent': 'Mozilla/5.0'}
    SITE = 'https://www.melhorcambio.com/cotacao/compra/dolar-turismo/sao-paulo'
    response = requests.get(SITE, timeout=5, headers=headers)
    page_content = BeautifulSoup(response.content, 'html.parser')
    currency = page_content.find('span', attrs={'content': 'BRL'})
    currency = page_content.find('span', string='R$ ')
    value = currency.find_next_sibling('span')
    print("SITE 3: ", SITE, "     ===> ", end='')
    dolarnow = currency.text + value.text
    dolarnow = dolarnow.replace(" ", "")
    dolarnow = dolarnow.replace(",", ".")
    print(dolarnow)
    # return(currency.text + value.text)


def main():
    now = datetime.now()
    # Data e Hora
    print(now.strftime("Date: %x"), now.strftime("Time: %X"))
    print("Showing dollar vs Brazilian Reais exchange today rate from some sites:\n")
    Mostra_Dolar_FXRATE()
    MostraValorDolarAWESOMEAPI()
    MostraDolarTurismo()


if __name__ == "__main__":
    main()
