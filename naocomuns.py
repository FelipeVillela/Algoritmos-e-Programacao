"""Programa desenvolvido na UFRJ para disciplina Algortmos e Programa��o"""

def naocomuns(a,b):
    #retorna os elementos n�o comuns entre duas listas 'a' e 'b'
    naocomuns = []
    

    for i in range (0,len(a)):
            
        if not (a[i] in b):
            naocomuns = naocomuns + [a[i]]
                    
    for i in range (0,len(b)):
            
        if not (b[i] in a):
            naocomuns = naocomuns + [b[i]]

                
    return naocomuns
