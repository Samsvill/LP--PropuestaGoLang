
from tkinter import *
from sintactico import *
from lexico import *

lexer = lex.lex()



def validaRegla(s):
  result = parser.parse(s)
  print(result)

def mostrarDatosLex():
    contenido= caja_codigo.get(1.0, 'end-1c')
    lexer.input(contenido)
    texto=[]
    for token in lexer:
        texto.append(str(token))
    texto= '\n'.join(texto)
    caja_resultados.delete('1.0','end')
    caja_resultados.insert('1.0', texto)

def mostrarDatosSintac():
    contenido= caja_codigo.get(1.0, 'end-1c')
    print(contenido)
    result = parser.parse(contenido)
    print(result)

    caja_resultados.delete('1.0','end')
    caja_resultados.insert('1.0', result)


def borrarDatos():
    caja_codigo.delete("1.0","end")
    caja_resultados.delete("1.0", "end")

# Configuración de la raíz
root = Tk()
root.title("Mi editor")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#--------------------------------------------Titulo-----------------------------------------#
titulo= Label(root, font=("JetBrains Mono",24) ,text='Editor Golang', fg='white', background='black')
titulo.grid(row=0, column=1, columnspan=1)
#--------------------------------------------------------------------------------------------#


#----------------------------Logo-------------------------#
logo = PhotoImage(file="imgs/logo.gif")
logo_label= Label(root, image=logo, bd=0)
logo_label.grid(row=0, column=2,sticky="s")
#---------------------------------------------------------#


resultado= Label(root, font=("JetBrains Mono",24) ,text='Resultados', fg='white', background='black')
resultado.grid(row=0, column=4, columnspan=2)



#------------------------------Editor de texto------------------------------------#
caja_codigo = Text(root)
caja_codigo.config(bd=0, padx=6, pady=4,font=("JetBrains Mono",12) ,
             insertbackground='white',spacing1='4',highlightthickness=2,
             insertborderwidth=10,background='black', fg='white',highlightbackground='#AEACAC',highlightcolor='#FFFFFF')
caja_codigo.grid(row=1, column=0, columnspan=3,padx=10,sticky="n")
#-----------------------------------------------------------------------------------#


#------------------------------Resultados------------------------------------#
caja_resultados= Text(root)
caja_resultados.config(bd=0, padx=6, pady=4,font=("JetBrains Mono",12) ,
             insertbackground='white',spacing1='4',highlightthickness=2,
             insertborderwidth=10, background='black', fg='white',highlightbackground='#AEACAC',highlightcolor='#FFFFFF')
caja_resultados.grid(row=1, column=4,padx=10,sticky="w", columnspan=2)
#-----------------------------------------------------------------------------------#


#------------------------------Boton Run-----------------------------------#
lexico = PhotoImage(file="imgs/lexico.gif")
lexico_button= Button(root, relief='flat', padx=0,pady=0, command=mostrarDatosLex,image=lexico, bg='black',activeforeground='black',activebackground='black')
lexico_button.grid(row=2, column=0, pady=10,padx=10)


sintactico = PhotoImage(file="imgs/sintactico.gif")
sintactico_button= Button(root, relief='flat', padx=0,pady=0, command=mostrarDatosSintac,image=sintactico, bg='black',activeforeground='black',activebackground='black')
sintactico_button.grid(row=2, column=1, pady=10,padx=10)


#------------------------------------------------------------------------------------#
delete = PhotoImage(file="imgs/delete.gif")
delete_button= Button(root, relief='flat', padx=0, pady=0, command=borrarDatos,image=delete, bg='black',activeforeground='black',activebackground='black')
delete_button.grid(row=2, column=2, pady=10, sticky='s')


integrantes_label=Label(root, text='Integrantes:  ○ Samantha Sanchez  ○ Yanaleen Pluas ○ Xavier Pauta',font=("JetBrains Mono",14), background='black',fg='white')
integrantes_label.grid(row=2, column=4)

root.configure(bg='black')

root.mainloop()
