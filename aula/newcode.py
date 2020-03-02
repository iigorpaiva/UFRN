from tkinter import *
from PIL import Image, ImageTk

global azul
azul = False
global verde
verde = False
global vermelho
vermelho = False



def comando(op):
    global azul
    global verde
    global vermelho    
    
    if (op == 1 and azul == False):
        print("Led Azul Ligado")
        ico2 = ImageTk.PhotoImage(file="azul.jpg")
        botao1.config(image=ico2, highlightthickness = 0, bd=0)
        botao1.image = ico2
        azul = True

    elif (op == 1 and azul == True):
        print('Led Azul Desligado')
        ico3 = ImageTk.PhotoImage(file="preto.jpg")
        botao1.config(image=ico3, highlightthickness = 0, bd=0)
        botao1.image = ico3
        azul = False

    elif (op == 2 and verde == False):
        print('Led Verde Ligado')
        verde = True

    elif (op == 2 and verde == True):
        print('Led Verde Desligado')
        verde = False    

    elif (op == 3 and vermelho == False):
        print('Led Vermelho Ligado')
        vermelho = True

    elif (op == 3 and vermelho == True):
        print('Led Vermelho Desligado')
        vermelho = False
    

janela = Tk()

janela.title('Arduino Controle')

janela.geometry('750x750')
texto1 = Label(text='Botão que liga led azul', fg = 'blue')
texto1.place(x=50,y=70)

ico = ImageTk.PhotoImage(file="preto.jpg")
botao1 = Button(text='Ligar Led Azul', command = lambda: comando(1), bg = 'green', fg = 'white')
botao1.config(image=ico, highlightthickness = 0, bd=0)
botao1.place(x=65,y=90)


texto2 = Label(text='Botão que liga led verde', fg = 'green')
texto2.place(x=200,y=70)
botao2 = Button(text='Ligar Led Verde', command = lambda: comando(2), bg = 'green', fg = 'white').place(x=215,y=90)

texto3 = Label(text='Botão que liga led vermelho', fg = 'red')
texto3.place(x=370,y=70)
botao3 = Button(text='Ligar Led Vermelho', command = lambda: comando(3), bg = 'red', fg = 'white').place(x=385,y=90)

janela.mainloop()
