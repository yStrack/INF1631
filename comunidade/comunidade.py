from itertools import combinations

class Grafo:
    def __init__(self,lconvidados):
        self.elementos = lconvidados
        self.conexoes = [] #grafo de conhecidos preenchido com lista vazia
        #posicao i conhece elementos da sublista dessa posicao
        for i in range(len(lconvidados)):
            self.conexoes.append([])
        return
    
    def conhece(self,conv1,conv2):
        self.conexoes[conv1-1].append(conv2)
        self.conexoes[conv2-1].append(conv1)
        return

    def verificaConheceMetade(self,lista,pessoa):
        nConhecidos = 0
        conhecidos = self.conexoes[pessoa-1]
        for el in conhecidos:
            if el in lista:
                nConhecidos += 1
        if nConhecidos >= len(lista)//2:
            return True
        else:
            return False

def comunidade():
    arqEntrada = open('comunidade.txt','r')
    arqSaida = open('saida.txt','w')
    nConv = int(arqEntrada.readline().strip('\n'))
    lconvidados = []
    for i in range(nConv):
        lconvidados.append(i+1)
    grafo = Grafo(lconvidados)
    for linha in arqEntrada:
        linha = linha.strip('\n')
        linha = linha.split(',')
        for i in range(1,len(linha)):
            grafo.conhece(int(linha[0]),int(linha[i]))
    conjFinal = maiorConj2(grafo)
    arqSaida.write(str(conjFinal)+'\n')
    arqSaida.write(str(len(conjFinal))+'\n')
    arqEntrada.close()
    arqSaida.close()
    return

def verifica(grafo,lista):
    for el in lista:
        if not grafo.verificaConheceMetade(lista,el):
            return False
    return True

def combinacoes(lista,tam):
    if tam == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        el = lista[i]
        lResto = lista[i+1:]
        T = combinacoes(lResto,tam-1)
        for conj in T:
            resultado.append([el]+conj)
    return resultado

def maiorConj2(grafo):
    lista = grafo.elementos
    k = len(lista)
    while True:
        if k == 0:
            return []
        comb = combinacoes(lista,k)
        for conj in comb:
            if verifica(grafo,list(conj)):
                return list(conj)
        k -= 1

comunidade()
