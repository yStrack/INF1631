import random
import math

def voting():
    arqEntrada = open('voting.txt','r')
    arqSaida = open('voting-saida.txt','w')
    votos = int(arqEntrada.readline().strip('\n')) #equivalente ao a
    dif = int(arqEntrada.readline().strip('\n')) #equivalente ao b
    limite = int(arqEntrada.readline().strip('\n')) #equivalente ao c
    conjunto = gera_subconjuntos(votos,dif,limite,0,0) # conjunto resultado
    if len(conjunto) >= 1000:
        arqSaida.write(str(len(conjunto))+'\n')
    else:
        for conj in conjunto:
            for el in conj:
                arqSaida.write(el)
            arqSaida.write('\n')
    arqEntrada.close()
    arqSaida.close()
    return

def gera_subconjuntos(tam, dif,limite,contW,contL):
    if tam == contW + contL:
        return ['']
    else:
        resultado = []
        if 2*contL == (tam - dif):
            t = gera_subconjuntos(tam,dif,limite,contW+1,contL)
            for i in range(len(t)):
                resultado.append('W'+t[i])
        elif contW - contL +1 >= limite:
            t = gera_subconjuntos(tam, dif,limite,contW,contL+1)
            for i in range(len(t)):
                resultado.append('L'+t[i])
        else:
            t = gera_subconjuntos(tam,dif,limite,contW+1,contL)
            for i in range(len(t)):
                resultado.append('W'+t[i])
            t = gera_subconjuntos(tam,dif,limite,contW,contL+1)
            for i in range(len(t)):
                resultado.append('L'+t[i])
        return resultado

voting()
