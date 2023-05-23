from tkinter import *
import customtkinter
import pyautogui as bot
from PIL import Image



def whatsWeb():
   
    tela = customtkinter.CTk(fg_color='black')
    tela.title('Calculando Tudo')
    largura = 500
    altura = 500
    largura_tela = tela.winfo_screenwidth()
    altura_tela = tela.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    tela.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    tela._set_appearance_mode('System')
    customtkinter.CTkLabel(tela,text='Bot\n Whatsapp Web', font=('Arial', 40, 'bold')).place(x=100, y=30)

   
    entradaNavegador = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Navegador')
    entradaNavegador.place(x=100, y=150)

    entradaSite = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Site')
    entradaSite.place(x=100, y=200)

    entradaNomeGrupo = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Contato ou Grupo')
    entradaNomeGrupo.place(x=100, y=250)

    entradaMenssagem = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite A Menssagem a Ser Enviada')
    entradaMenssagem.place(x=100, y=300)
   
    def funcionamentoWhats():
        bot.press('win') # press() ele pressiona a tecla, nesse caso mandei pressionar a tecla do windows 
        bot.sleep(3)
        bot.write(entradaNavegador.get())# write() é uma função para escrever algo, nesse caso ele escreve na pesquisa do menu inicar
        bot.sleep(3)
        bot.press('enter')# aqui ele preciona o ENTER
        bot.sleep(3) #aqui você da um tempo de pesquisa, nesse caso eu dei 1s
        bot.write(entradaSite.get()) #aqui você passará o endereço desejado, no nosso caso é do whats.
        bot.sleep(3)
        bot.press('enter')
        bot.sleep(5)
        bot.press('tab')
        bot.press('tab')
        bot.press('tab')
        bot.press('tab')
        bot.press('tab')
        bot.sleep(3)
        bot.write(entradaNomeGrupo.get())
        bot.press('enter')
        bot.sleep(3)
        bot.write(entradaMenssagem.get())
        bot.sleep(3)
        bot.press('enter')
    
    comecar = customtkinter.CTkButton(tela,text='>>COMEÇAR<<', width=300 ,command=funcionamentoWhats, fg_color='#075E54',hover_color='#25D366')
    comecar.place(x=100, y=360)
    comecar = customtkinter.CTkButton(tela,text='>>VOLTAR<<', width=300 ,command=tela.destroy, fg_color='#075E54',hover_color='#25D366')
    comecar.place(x=100, y=400)
    customtkinter.CTkLabel(tela, text='By: Elias_Panda1').place(x=20, y=470)
    tela.mainloop()

def whatsWind():
    tela = customtkinter.CTk(fg_color='black')
    tela.title('Calculando Tudo')
    largura = 500
    altura = 500
    largura_tela = tela.winfo_screenwidth()
    altura_tela = tela.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    tela.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    tela._set_appearance_mode('System')
    customtkinter.CTkLabel(tela,text='Bot\n Whatsapp Windows', font=('Arial', 40, 'bold')).place(x=50, y=30)

    entradaNomeGrupo = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Contato ou Grupo')
    entradaNomeGrupo.place(x=100, y=150)

    entradaMenssagem = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite A Menssagem a Ser Enviada')
    entradaMenssagem.place(x=100, y=200)

    def funcionalidadeWhatsWindows():
        bot.press('win')
        bot.sleep(1)
        bot.write('Aplicativos: Whatsapp')
        bot.sleep(2)
        bot.press('enter')
        bot.sleep(7)
        bot.press('tab')
        bot.sleep(2)
        bot.press('enter')
        bot.sleep(2)
        bot.write(entradaNomeGrupo.get())
        bot.sleep(1)
        bot.press('tab')
        bot.sleep(1)
        bot.press('enter')
        bot.sleep(1)
        bot.write(entradaMenssagem.get())
        bot.sleep(2)
        bot.press('enter')
    comecar = customtkinter.CTkButton(tela,text='>>COMEÇAR<<', width=300 ,command=funcionalidadeWhatsWindows, fg_color='#075E54',hover_color='#25D366')
    comecar.place(x=100, y=300)   
    Voltar = customtkinter.CTkButton(tela,text='>>VOLTAR<<', width=300 ,command=tela.destroy, fg_color='#075E54',hover_color='#25D366')
    Voltar.place(x=100, y=340) 
    customtkinter.CTkLabel(tela, text='By: Elias_Panda1').place(x=20, y=470)
    tela.mainloop()






