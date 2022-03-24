from PySimpleGUI import PySimpleGUI as sg
from numpy import size

# layout
sg.theme('BluePurple')
# aparencia é o nome da variável q eu escolhi
aparencia = [
    # criando 3 linhas
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Button('Entrar')]
]
# Criando a janela
janela = sg.Window('Tela de Login', aparencia)

# ler eventos
while True:  # para que não pare de funcionar
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break  # para que ele não continue rodando o programa caso a pessoa ja tenha fechado o programa
    if eventos == 'Entrar':  # se clicou no botão entrar
        # acessando os valor lidos na tela
        if valores['usuario'] == 'flavia' and valores['senha'] == '123456':
            print("Funcionou bem")
   
