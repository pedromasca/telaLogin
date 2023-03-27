from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme("Reddit")
layout = [
    [sg.Text("Usuário"), sg.Input(key="usuario", size=(20, 1))],
    [sg.Text("Senha  "), sg.Input(
        key="senha", password_char="*", size=(20, 1))],
    [sg.Checkbox("Salvar o login?")],
    [sg.Button("Entrar", size=(10, 1))]
]
# Janela
janela = sg.Window("Login", layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores["usuario"] == "Pedro" and valores["senha"] == "123456":
            print("Bem vindo!")
