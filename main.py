from PySimpleGUI import PySimpleGUI as sg
print("Magic Sign")

sg.theme('Reddit')
layout = [
    [sg.Text('Login'), sg.Input(key='login')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        print ('Chegou aqui')