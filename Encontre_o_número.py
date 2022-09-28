# Tem seu funcionamento inspirado na busca binária
# É um algoritmo que gera um número aleatório entre 1 e 20, no qual o objetivo é acertar qual é o número

import PySimpleGUI as sg
import random 

class EncontreNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.minimo = 1
        self.maximo = 10
        self.tentar_novamente = True
    
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Sua tentativa',size=(40,0))],
            [sg.Input(size=(18,0),key='Valortentativa')],
            [sg.Button('Tentar!')],
            [sg.Output(size=(39,10))]
        ]
        # gerar uma janela
        self.janela = sg.Window('Tente encontrar o número!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber os valores
                self.evento, self.valores = self.janela.Read()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Frio! Valor alto!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Frio! Valor baixo!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False #já que o valor foi encontrado, não é necessário nova tentativa
                            print('Encontrou!!')
                            break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()
            

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.minimo,self.maximo)

busca = EncontreNumero()
busca.Iniciar()