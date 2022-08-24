#
# Example file for retrieving data from the internet
#
import sys
import urllib.request
SITE = "http://www.google.com"


def main():
    webUrl = urllib.request.urlopen(SITE)
    resultcode = webUrl.getcode()           # le o codigo de retorno
    if resultcode == 200:                   # OBA, deu certo acessar a pagina
        print("\n Sucesso acessei ", SITE, "resultcode =" + str(resultcode))
    else:
        print("Erro acessando ", SITE, "resultcode = ", resultcode)
        exit

    data = webUrl.read()
    tam_pag_google = sys.getsizeof(data)

    print("\ndados =", data)                # Mostra todo a pagina HYML lida
    print("Tamanho da pagina do google =", tam_pag_google)


if __name__ == "__main__":
    main()
