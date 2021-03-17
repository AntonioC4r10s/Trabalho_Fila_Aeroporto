from Include.Client import Cliente as cl
from Include.Atendente import Atendente as atd
from collections import deque as dq
from tkinter import *

#lista de cada um dos funcionarios
lista_1 = []
lista_2 = []
lista_3 = []
lista_4 = []
lista_5 = []

#Criando funcionarios e passando uma lista de clientes a cada um
atendente_1 = atd(1, lista_1)
atendente_2 = atd(2, lista_2)
atendente_3 = atd(3, lista_3)
atendente_4 = atd(4, lista_4)
atendente_5 = atd(5, lista_5)

#fila onde ficarão os clientes durante todo o processo de fila
filaGeral = dq()

i = 0
hora = 0
minutos = 0
horaMaxima = 2
tempoDeAtendimentoCliente = 60/15
numeroDeChegadas = 500
numeroDeAtendentes = 5
#tempoMedioCliente = 0

def numeroDeAtendentesIdeal(numeroDeChegadas, atendimentoPorHora):
    atendimentoPorHora = 60/atendimentoPorHora
    return  ("Serão necessário ao todo " + str(round(numeroDeChegadas/atendimentoPorHora)+1) + " atendentes para atender a tempo, ou")

def quantidadeDeAtendimentoIdeal(numeroDeChegadas, numeroDeAtendentes):
    return ("Cada atendente deve atender " + str(int(numeroDeChegadas/numeroDeAtendentes)) + " clientes por hora")

janela = Tk()
janela.title("Fila do Aeroporto")

#Labels
fontePadrao = "Arial 10"
labelNumeroDeAtendentes = Label(janela, text="Numero de Atendentes: ", font=fontePadrao)
labelAtendentes = Label(janela, text=numeroDeAtendentes, font=fontePadrao)
labelNumeroDeChegadas = Label(janela, text="Número de Chegadas por hora: ", font=fontePadrao)
labelChegadas = Label(janela, text=numeroDeChegadas, font=fontePadrao)
labelTempoDeAntendimento = Label(janela, text="Tempo de atendimento:", font=fontePadrao, height=2, anchor=N)
labelAntendimento = Label(janela, text=str(tempoDeAtendimentoCliente) + " min", font=fontePadrao, height=2, anchor=N)
labelSolucao_1 = Label(janela, font=fontePadrao)
labelSolucao_2 = Label(janela, font=fontePadrao)
#Layout
labelNumeroDeAtendentes.grid(row=1, column=0)
labelAtendentes.grid(row=1, column=1)
labelNumeroDeChegadas.grid(row=2,column=0)
labelChegadas.grid(row=2,column=1)
labelTempoDeAntendimento.grid(row=3, column=0)
labelAntendimento.grid(row=3, column=1)
labelSolucao_1.grid(row=10,column=0)
labelSolucao_2.grid(row=11,column=0)

    #Conta o tempo maximo
while(hora  < horaMaxima):
    # Conta os minutos
    while(minutos < 60 ):
        #print("hora: {0}:{1}" .format(hora, minutos))
        if(minutos == 0):
            a = len(filaGeral)
            b = len(filaGeral) + numeroDeChegadas

            for c in range(a, b):
                filaGeral.append(cl(i, hora, 0, 0))
                #print(filaGeral[i])
                i += 1

        if(minutos % tempoDeAtendimentoCliente == 0):
            #Atendente 1
            aux = filaGeral.popleft()
            cl.setTempoFinal(aux, 4)
            lista_1.append(aux)
            print(aux)
            #Atendente 2
            aux = filaGeral.popleft()
            cl.setTempoFinal(aux, 4)
            lista_2.append(aux)
            print(aux)
            #Atendente 3
            aux = filaGeral.popleft()
            cl.setTempoFinal(aux, 4)
            lista_3.append(aux)
            print(aux)
            # Atendente 4
            aux = filaGeral.popleft()
            cl.setTempoFinal(aux, 4)
            lista_4.append(aux)
            print(aux)
            # Atendente 5
            aux = filaGeral.popleft()
            cl.setTempoFinal(aux, 4)
            lista_5.append(aux)
            print(aux)
            janela.update()
        for d in range(0, len(filaGeral)):
            cl.setTempoDeFila(filaGeral[d], 1)

        minutos += 1
    minutos = 0
    hora += 1

while(filaGeral):
    if(minutos % 4 == 0):
        # Atendente 1
        aux = filaGeral.popleft()
        cl.setTempoFinal(aux, 4)
        lista_1.append(aux)
        print(aux)
        # Atendente 2
        aux = filaGeral.popleft()
        cl.setTempoFinal(aux, 4)
        lista_2.append(aux)
        print(aux)
        # Atendente 3
        aux = filaGeral.popleft()
        cl.setTempoFinal(aux, 4)
        lista_3.append(aux)
        print(aux)
        # Atendente 4
        aux = filaGeral.popleft()
        cl.setTempoFinal(aux, 4)
        lista_4.append(aux)
        print(aux)
        # Atendente 5
        aux = filaGeral.popleft()
        cl.setTempoFinal(aux, 4)
        lista_5.append(aux)
        print(aux)
#        time.sleep(1/velocidade)
        janela.update()

    for d in range(0, len(filaGeral)):
        cl.setTempoDeFila(filaGeral[d], 1)

    minutos += 1
    if(minutos == 60):
        minutos = 0
        hora += 1

labelSolucao_1["text"] = numeroDeAtendentesIdeal(numeroDeChegadas, tempoDeAtendimentoCliente)
labelSolucao_2["text"] = quantidadeDeAtendimentoIdeal(numeroDeChegadas, numeroDeAtendentes)

janela.resizable(False, False)
janela.mainloop()
