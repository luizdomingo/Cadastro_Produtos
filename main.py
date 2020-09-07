from tkinter import *
from tkinter import ttk
from time import strftime
import os

pasta_arqui = os.path.dirname(__file__)

app = Tk()
app.geometry('1285x720+330+130')
app.resizable(False, False)
app.title('Sistema')
app.iconbitmap('imageres_5306.ico')

frame = Frame(app)  # , text='Cadastrar Produtos')
frame.place(x=3, y=0, width=1280, height=715)

# Adcionando imagem dentro do sistema -----------------------------------------------------
# imagem = PhotoImage(file=pasta_arqui + "\\system.png")
# img = Label(frame, image=imagem, width=500, height=400)
# img.place(x=1000, y=0)
# --------------------------------------------------------------------------------------------

label1 = Label(frame, text=strftime('%H:%M:%S'), font='Helvetica 25 bold', fg='#2c2f33')
label1.place(x=1120, y=660, width=168, height=35)

label_produto = Label(frame, text='Descrição: ', font='Helvetica 11 bold')
label_produto.grid(row=1, column=0, pady=0)

txt1 = Entry(frame, font='Helvetica 12 ', fg='#000', relief='solid')
txt1.grid(row=1, column=1, pady=1, ipady=3)
txt1.focus()

label_quantidade = Label(frame, text='Quantidade: ', font=('Helvetica', 11, 'bold'))
label_quantidade.grid(row=2, column=0)

txt2 = Entry(frame, font='Helvetica 12 ', fg='#000', relief='solid')
txt2.grid(row=2, column=1, pady=1, ipady=3)

btn = ttk.Button(frame, text='Salvar')
btn.place(x=420, y=637, width=155, height=50)

bt_login = ttk.Button(frame, text='Login', command=lambda: login())
bt_login.place(x=595, y=637, width=155, height=50)

btn1 = Button(frame, text='Iniciar', bd=1, width=17, height=2, relief='solid', font=('Helvetica', '11', 'bold'))
btn1.place(x=235, y=637)

lista = ttk.Treeview(frame, columns=('ID', 'Descrição', 'Quantidade', 'Preço', 'Data'), show='headings')
lista.column('ID', minwidth=0, width=50)
lista.column('Descrição', minwidth=0, width=275)
lista.column('Quantidade', minwidth=0, width=120)
lista.column('Preço', minwidth=0, width=50)
lista.column('Data', minwidth=0, width=50)

lista.heading('ID', text='ID')
lista.heading('Descrição', text='Descrição')
lista.heading('Quantidade', text='Quantidade')
lista.heading('Preço', text='Preço')
lista.heading('Data', text='Data')
lista.place(x=4, y=80, width=800, height=550)


def login():
    applogin = Tk()
    applogin.geometry('450x250+750+430')
    applogin.title('Login PDV')
    applogin.iconbitmap('1301321325_database.ico')
    applogin.resizable(False, False)


def relogio():
    agora = strftime('%H:%M:%S')
    if agora != label1['text']:
        label1['text'] = agora
    label1.after(100, relogio)


relogio()
app.mainloop()
