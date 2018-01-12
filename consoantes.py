"""Programa desenvolvido na UFRJ para disciplina Algortmos e Programação"""

def consoantes(s):
    #Retorna as consoantes de uma string definida pelo usuário

    alfabeto_consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z']

    lista = list(s)
    resultado = []

    for i in range(0,len(lista)):

        if lista[i] in alfabeto_consoantes:
            if not lista[i] in resultado:
                resultado = resultado + [lista[i]]
    return resultado
            
