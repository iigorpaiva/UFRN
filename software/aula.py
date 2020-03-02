from PIL import Image, ImageTk
from tkinter import *
import serial

global azul
azul = False
global verde
verde = False
global vermelho
vermelho = False

def create_porta():
    global portaUSB
    aux = temp.get()
    portaUSB = serial.Serial(aux, 9600)
    

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
        botao1.config(image=icone, highlightthickness = 0, bd=0)
        botao1.image = icone
        azul = True

    elif (op == 1 and azul == True):
        print('Led Azul Desligado')
        sen_command('018')
        icone = ImageTk.PhotoImage(file="preto.jpg")
        botao1.config(image=icone, highlightthickness = 0, bd=0)
        botao1.image = icone
        azul = False

    elif (op == 2 and verde == False):
        print('Led Verde Ligado')
        sen_command('013')
        icone = ImageTk.PhotoImage(file="verde.jpg")
        botao2.config(image=icone, highlightthickness = 0, bd=0)
        botao2.image = icone
        verde = True

    elif (op == 2 and verde == True):
        print('Led Verde Desligado')
        sen_command('016')
        icone = ImageTk.PhotoImage(file="preto.jpg")
        botao2.config(image=icone, highlightthickness = 0, bd=0)
        botao2.image = icone
        verde = False    

    elif (op == 3 and vermelho == False):
        print('Led Vermelho Ligado')
        sen_command('014')
        icone = ImageTk.PhotoImage(file="vermelho.jpg")
        botao3.config(image=icone, highlightthickness = 0, bd=0)
        botao3.image = icone
        vermelho = True

    elif (op == 3 and vermelho == True):
        print('Led Vermelho Desligado')
        sen_command('017')
        icone = ImageTk.PhotoImage(file="preto.jpg")
        botao3.config(image=icone, highlightthickness = 0, bd=0)
        botao3.image = icone
        vermelho = False
    

janela = Tk()

janela.title('Controle de LED')

janela.geometry('650x500')
janela.configure(bg='white')

text_Port = Label(text='Digite a porta:').place(x=50,y=200)
temp = StringVar ()
porta = Entry(janela, textvariable = temp).place(x=150,y=200)
botao_port  = Button(text='OK', command = create_porta).place(x=290,y=195)



texto1 = Label(text='Botão que liga led azul', fg = 'blue',bg='white')
texto1.place(x=50,y=70)

ico1 = ImageTk.PhotoImage(file="preto.jpg")
botao1 = Button(text='Ligar Led Azul', command = lambda: comando(1))
botao1.config(image=ico1, highlightthickness = 0, bd=0)
botao1.place(x=110,y=90)


texto2 = Label(text='Botão que liga led verde', fg = 'green',bg='white')
texto2.place(x=220,y=70)

ico2 = ImageTk.PhotoImage(file="preto.jpg")
botao2 = Button(text='Ligar Led Verde', command = lambda: comando(2))
botao2.config(image=ico2, highlightthickness = 0, bd=0)
botao2.place(x=270,y=90)

texto3 = Label(text='Botão que liga led vermelho', fg = 'red',bg='white')
texto3.place(x=390,y=70)

ico3 = ImageTk.PhotoImage(file="preto.jpg")
botao3 = Button(text='Ligar Led Vermelho', command = lambda: comando(3))
botao3.config(image=ico3, highlightthickness = 0, bd=0)
botao3.place(x=460,y=90)



janela.mainloop()
