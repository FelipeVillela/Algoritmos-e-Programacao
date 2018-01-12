# -*- coding: cp1252 -*-
"""Programa em Python para analisar duas listas e gerar uma nova com os valores comuns entre elas
Desenvolvido na UFRJ para a disciplina Algoritmons e programação"""


def vernaLista(i, ls):
    #Verifica se valor i existe na lista
	flag = False
	for k in ls:
		if i == k:
			flag = True
			break
	return flag


def analisaLista(ls1, ls2):
    #Verifica Valores repetidos numa lista e preenche uma lista nova com esses valores
	ls_aux = []
	#Ordena as listas
	ls1.sort()
	ls2.sort()
	for i in ls1:
		counter = 0
		counterls1 = ls1.count(i)
		counterls2 = ls2.count(i)
		#Analisa quantas vezes o valor i menos aparece tanto na lista 1 qnto na 2
		if counterls1 < counterls2:
			counter = counterls1
		else:
			counter = counterls2
			
		if  counter > 0 and vernaLista(i, ls_aux) == False:
			#Preenche a lista auxiliar com o valor i, counter vezes
			j = 0
			while j < counter:
				ls_aux.append(i)
				j = j + 1
	#Imprime lista auxiliar
	print ls_aux

