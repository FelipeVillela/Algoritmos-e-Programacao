"""Programa desenvolvido na UFRJ para disciplina Algortmos e Programação"""

def palindromo(n):
    u"""Dado um número n, retorna o
    palindromo desse número, isto é, o inverso"""
    n = str(n)[::-1]
    return int(n)


def fatorLychrel(n):
    u"""Retorna a quantidade de vezes que um número n tem que ser somado
    ao seu inverso, afim de encontrar um número palíndromo. Retorna -1
    caso após 50 iterações, não se conseguiu achar um palindromo"""

    cont = 1

    while cont <= 50:
        n += palindromo(n)
        if n == palindromo(n):
            return cont
        cont += 1
    return -1
