"""Programa desenvolvido na UFRJ para disciplina Algortmos e Programa��o"""

def palindromo(n):
    u"""Dado um n�mero n, retorna o
    palindromo desse n�mero, isto �, o inverso"""
    n = str(n)[::-1]
    return int(n)


def fatorLychrel(n):
    u"""Retorna a quantidade de vezes que um n�mero n tem que ser somado
    ao seu inverso, afim de encontrar um n�mero pal�ndromo. Retorna -1
    caso ap�s 50 itera��es, n�o se conseguiu achar um palindromo"""

    cont = 1

    while cont <= 50:
        n += palindromo(n)
        if n == palindromo(n):
            return cont
        cont += 1
    return -1
