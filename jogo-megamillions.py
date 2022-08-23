# Mega Millions Games for Brazilian Currency

import random
custojogo = 2


def MostraJogosMegaRandomicos(njogos):
    print(njogos, "Random numbers for Megamillions  + 1 MB :")
    for i in range(njogos):
        # amostragem randomica sem repeticao
        lista_mega = sorted(random.sample(range(1, 71), 5))
        # print("list_mega=", lista_mega)
        lista_mega_formatada = ['', '', '', '', '']
        for ii in range(0, len(lista_mega)):
            lista_mega_formatada[ii] = str(lista_mega[ii]).zfill(2)
            # preenhe com zero a esquerda

        print(lista_mega_formatada, " MB=", str(
            random.randrange(1, 26)).zfill(2))


def main():
    MostraJogosMegaRandomicos(10)

    dolar = float(input("How many dollar do you want to play U$:"))
    cotacao = float(
        input("What is the exchange rate for the dollar to Brazilian Reais today?"))
    conversao = dolar*cotacao
    print('The total amount for Brazilian today is: R$', ("%.2f" % conversao))
    print()

    jogosremanescentes = input("How many free games from Last game? :")

    if jogosremanescentes == '':
        jogosremanescentes = 0

    numjogos = (int(dolar) / custojogo) + int(jogosremanescentes)
    print("OWW !!! Lets play ", int(numjogos), "times. Good Luck")

    exit()


if __name__ == "__main__":
    main()
