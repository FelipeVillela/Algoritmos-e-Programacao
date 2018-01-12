# -*- coding: cp1252 -*-
"""Programa desenvolvido na UFRJ para disciplina Algortmos e Programação"""

def divisores(n):
    #Retorna uma lista com os divisores de n, excluindo 1 e ele mesmo
    
    lista_divisores = []
    
    for i in range (2,n):
        if(n%i == 0):
            lista_divisores = lista_divisores + [i]
    return lista_divisores
