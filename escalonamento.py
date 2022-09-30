import heapq as hq
import fileinput
from random import randint

class Processo:

    def __init__(self, chegada, duracao):
      self.chegada = chegada
      self.duracao = duracao
      self.consumido = 0
      self.quantum = 2
      self.prioridade = 0

file = fileinput.input()

processos = []

for line in file:
  p = line.rstrip().split(" ")
  processos.append((int(p[0]), int(p[1]))) # para cada processo escreve a tupla ('chegada', 'duracao')

processos = sorted(processos, key=lambda processo: processo[0]) # ordena os processos pelo momento de chegada

def imprime_saida(infoProcessos, alg):
  somaRetM = 0
  somaResM = 0
  somaEspM = 0

  for ip, values in infoProcessos.items():
    somaRetM += values["retorno"]
    somaResM += values["resposta"]
    somaEspM += values["espera"]

  total = len(infoProcessos)
  print(alg+ " %.2f %.2f %.2f" % (somaRetM/total, somaResM/total, somaEspM/total))

# list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy')] 
# hq.heapify(list_stu) 
  
# print("The order of presentation is :") 
  
# for i in list_stu: 
#   print(i[0],':',i[1])]

def pd():
  pass

def loteria():
  infoProcessos = {}  
  lista = []

  for i in range(0, len(processos)): # insere os processos na lista
    p = Processo(processos[i][0], processos[i][1])
    infoProcessos[p] = {"retorno": 0, "resposta": 0, "espera": 0}
    lista.append(p)

  TEMPO = 0
  prontos = []

  while len(lista) != 0: # enquanto existirem processos na fila

    for p in lista: # seleciona os processos em estado pronto
      if p.chegada <= TEMPO:
        prontos.append(p)

    sorteado = randint(0, len(prontos) - 1)

    processo = prontos[sorteado]

    if processo.consumido == 0: # salva o tempo da primeira resposta para o atual processo
          infoProcessos[p]["resposta"] = TEMPO - p.chegada

    TEMPO += 1
    processo.consumido += 1

    if processo.consumido == processo.duracao:
      retorno = TEMPO - p.chegada
      infoProcessos[p]["retorno"] = retorno
      infoProcessos[p]["espera"] = retorno - p.duracao
      lista.remove(processo)

    prontos = []
    
  imprime_saida(infoProcessos, "LOT")


def rr():
  infoProcessos = {}
  lista = []

  for i in range(0, len(processos)): # insere os processos na lista
    p = Processo(processos[i][0], processos[i][1])
    infoProcessos[p] = {"retorno": 0, "resposta": 0, "espera": 0}
    lista.append(p)

  TEMPO = 0

  while len(lista) != 0: # enquanto existirem processos na fila

    for p in lista.copy():

      if p.chegada <= TEMPO: # verifica se já chegou o tempo de entrada do processo
        if p.consumido == 0: # salva o tempo da primeira resposta para o atual processo
          infoProcessos[p]["resposta"] = TEMPO - p.chegada
          
        while p.quantum != 0: # consome os quantums do processo
          TEMPO += 1
          p.quantum -= 1
          p.consumido += 1

          if p.consumido == p.duracao: # terminou execução do processo
            lista.remove(p)
            retorno = TEMPO - p.chegada
            infoProcessos[p]["retorno"] = retorno
            infoProcessos[p]["espera"] = retorno - p.duracao
            break

        if p.consumido != p.duracao: # dá mais 2 quantums ao processo
          p.quantum = 2

  imprime_saida(infoProcessos, "RR")

loteria()
rr()