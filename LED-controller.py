# import para podermos gerar uma interface grafica
# import para estabelecermos uma comunicação serial com o arduino

from PIL import Image, ImageTk
from tkinter import *
import serial
import time

# variaveis globais
global azul
azul = False
global verde
verde = False
global vermelho
vermelho = False

# cria a porta de conexão usb
# aux para pegar a porta digitada transformada em string
# variavel recebe a porta que a gente passa, com 9600 velocidade padrao


def create_porta():
    global portaUSB
    aux = temp.get()
    try:
        while(1):
            portaUSB = serial.Serial(aux, 9600, timeout=1)
            incomingByte = portaUSB.read()
            print(incomingByte)
            janela.update()
    except:
        print('conexao nao estabelecida')

# funcao recebe o codigo, converte de novo para string
# escreve o codigo para dentro do arduino


def sen_command(cod):
    aux = str(cod)
    portaUSB.write(aux.encode())


def comando(op):
    global azul
    global verde
    global vermelho

    if (op == 1 and azul == False):
        print("Led Azul Ligado")
        sen_command('015')
        icone = ImageTk.PhotoImage(file="azul.jpg")
        botao1.config(image=icone, highlightthickness=0, bd=0)
        botao1.image = icone
        azul = True

    elif (op == 1 and azul == True):
        print('Led Azul Desligado')
        sen_command('018')
        icone = ImageTk.PhotoImage(file="preto.jpg")
        botao1.config(image=icone, highlightthickness=0, bd=0)
        botao1.image = icone
        azul = False

    elif (op == 2 and verde == False):
        print('Led Verde Ligado')
        sen_command('013')
        icone = ImageTk.PhotoImage(file="verde.jpg")
        botao2.config(image=icone, highlightthickness=0, bd=0)
        botao2.image = icone
        verde = True

    elif (op == 2 and verde == True):
        print('Led Verde Desligado')
        sen_command('016')
        icone = ImageTk.PhotoImage(file="preto.jpg")
        botao2.config(image=icone, highlightthickness=0, bd=0)
        botao2.image = icone
        verde = False

    elif (op == 3 and vermelho == False):
        print('Led Vermelho Ligado')
        sen_command('014')
        icone = ImageTk.PhotoImage(file="vermelho.jpg")
        botao3.config(image=icone, highlightthickness=0, bd=0)
        botao3.image = icone
        vermelho = True

    elif (op == 3 and vermelho == True):
        print('Led Vermelho Desligado')
        sen_command('017')
        icone = ImageTk.PhotoImage(file="preto.jpg")
        botao3.config(image=icone, highlightthickness=0, bd=0)
        botao3.image = icone
        vermelho = False

    elif (op == 4 and vermelho == False and azul == False and verde == False):
        print('Liga Tudo')
        sen_command('069')
        vermelho = True
        azul = True
        verde = True

    elif (op == 4 and vermelho == True and azul == True and verde == True):
        print('Desliga Tudo')
        sen_command('070')
        vermelho = False
        azul = False
        verde = False

####################################### INTERFACE GRAFICA ##############################################################

# da biblioteca Tk


janela = Tk()

janela.title('Controle de LED')

# define o tamanho da janela

janela.geometry('650x360')
janela.configure(bg='white')

# pede ao usuario para inserir a porta conectada com o arduino. Ex: com6
# pode ser escrita em letras maiuscula ou minuscula
# o temp sera usado no codigo acima e sera passado como uma string

Label(text='Digite a porta:').place(x=50, y=200)
temp = StringVar()
Entry(janela, textvariable=temp).place(x=150, y=200)
Button(text='OK', command=create_porta).place(x=320, y=195)


# botoes que serão pressionados para ligar os LEDS (azul, verde, vermelho)

texto1 = Label(text='Botão que liga led azul', fg='blue', bg='white')
texto1.place(x=50, y=70)

ico1 = ImageTk.PhotoImage(file="preto.jpg")
botao1 = Button(text='Ligar Led Azul', command=lambda: comando(1))
botao1.config(image=ico1, highlightthickness=0, bd=0)
botao1.place(x=110, y=90)

texto2 = Label(text='Botão que liga led verde', fg='green', bg='white')
texto2.place(x=220, y=70)

ico2 = ImageTk.PhotoImage(file="preto.jpg")
botao2 = Button(text='Ligar Led Verde', command=lambda: comando(2))
botao2.config(image=ico2, highlightthickness=0, bd=0)
botao2.place(x=270, y=90)

texto3 = Label(text='Botão que liga led vermelho', fg='red', bg='white')
texto3.place(x=390, y=70)

ico3 = ImageTk.PhotoImage(file="preto.jpg")
botao3 = Button(text='Ligar Led Vermelho', command=lambda: comando(3))
botao3.config(image=ico3, highlightthickness=0, bd=0)
botao3.place(x=460, y=90)

texto4 = Label(text='Botão que liga tudo', fg='black', bg='white')
texto4.place(x=240, y=260)

ico4 = ImageTk.PhotoImage(file="preto.jpg")
botao4 = Button(text='Ligar Tudo', command=lambda: comando(4))
botao4.config(image=ico3, highlightthickness=0, bd=0)
botao4.place(x=270, y=290)

janela.mainloop()
