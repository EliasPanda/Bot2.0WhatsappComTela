from tkinter import *
import customtkinter, tkinter
from PIL import Image
from BotComTela2 import whatsWeb, whatsWind

tela = customtkinter.CTk(fg_color='black')

my_image = customtkinter.CTkImage(light_image=Image.open('imgs/pngwing.com.png'),
                                    dark_image=Image.open('imgs/pngwing.com.png'),
                                    size=(80, 80))
LabelImagem = customtkinter.CTkLabel(
                           tela, text='', image=my_image).place(x=210, y=10)
customtkinter.CTkLabel(tela,text='Bot', font=('Arial', 40, 'bold')).place(x=210, y=90)

tela.title('Bot Whatsapp')
largura = 500
altura = 300
largura_tela = tela.winfo_screenwidth()
altura_tela = tela.winfo_screenheight()
posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura  / 2
tela.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
tela._set_appearance_mode('System')

WhatsWeb = customtkinter.CTkButton(tela,text='Clique Aqui se for Whatsapp Web', width=300 ,command=whatsWeb, fg_color='#075E54',hover_color='#25D366')
WhatsWeb.place(x=100, y=180)

WhatsWind = customtkinter.CTkButton(tela,text='Clique Aqui se for Whatsapp Windows', width=300 ,command=whatsWind, fg_color='#075E54',hover_color='#25D366')
WhatsWind.place(x=100, y=220)


customtkinter.CTkLabel(tela, text='By: Elias_Panda1').place(x=20, y=270)

tela.mainloop()
