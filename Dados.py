# Simula o arremesso de dados, com valores de 1 até 6
import PySimpleGUI as sg
import random

class ArremessarDado:
    def __init__(self):
        self.minimo = 1
        self.maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Deseja aremessar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
    
    def Iniciar(self):
        # gerar janela
        self.janela = sg.Window('Aremesso de Dado',layout=self.layout)
        # leitura dos valores 
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.ArremessoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agrecemos a sua participação!')
            else:
                print('Digite sim ou não')
        except:
            print('Erro')
    
    def ArremessoDado(self):
        valor = random.randint(self.minimo,self.maximo)
        print(f'O valor que saiu no dado foi: {valor}')

arremesso = ArremessarDado()
arremesso.Iniciar()