"""Programa desenvolvido na UFRJ para disciplina Algortmos e Programação"""

def verifica_matriz(m):
    u"""Dada uma matriz m, verifica se a matriz é quadrada"""
    for i in range(len(m)):
        if len(m[i]) != len(m):
            return False

def magico(m):
    u"""Dada uma matriz m, verifica se a matriz é mágica, ou seja, se a soma das linhas,
    colunas e e diagonais forem iguais, retorna true"""
    
    resultado = [] #Lista que recebe o valor da soma de cada linha, coluna e diagonais    

    if verifica_matriz(m) == False:
        return False
    
    for i in range(len(m)): #Soma as linhas
        soma = 0
        for j in range (len(m)):
            soma += m[i][j]
        resultado.append(soma)        

    for j in range(len(m)): #Soma as colunas
        soma = 0
        for i in range(len(m)):
            soma += m[i][j]
        resultado.append(soma)
   
    soma = 0
    for i in range(len(m)): #soma a diagonal da esquerda para a direita
        soma += m[i][i]
    resultado.append(soma)

    soma = 0
    for i in range(len(m)-1, -1, -1):  #soma a diagonal da direita para a esquerda
        soma += m[i][i]
    resultado.append(soma)

    for n in range(len(resultado)): #Verifica se os elementos da lista resultado são iguais
        for m in range(len(resultado)):
            if resultado[n] != resultado[m]:
                return False
            
    return True

