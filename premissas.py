from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

win_principal = Tk()
# Propriedades da Janela
win_principal.title("Gestão de Teste de Software")
win_principal.configure(background="#ced2d9")

# Define o tamanho da janela principal
#win_principal.geometry("1375x1000+100+100")
win_principal.geometry("1375x700")

def visualiza():
    pass

frm_planoteste = Frame(win_principal,bg='#00CED1',highlightbackground='#00CED1',highlightthickness=4)
frm_planoteste.place(relx= 0.01, rely=0.01, relwidth=0.98, relheight=0.30)

# Cria o widget Label com o texto "Identificação do projeto"
lbl_identificacao = Label(frm_planoteste, text="Premissas", font=("Arial", 70), bg="#00CED1", fg="white")

lbl_identificacao.place(relx=0.5, rely=0.5, anchor=CENTER)

# cria o objeto PhotoImage com a imagem do monitor
imagem_monitor = PhotoImage(file='monitor.png')

# carrega a imagem original
imagem_original = PhotoImage(file='monitor.png')

# define a proporção de redução da imagem
proporcao = 2

# reduz a imagem pela metade
imagem_reduzida = imagem_original.subsample(proporcao, proporcao)

# adiciona a imagem no label
lbl_monitor = Label(frm_planoteste, image=imagem_reduzida, bg="#00CED1")
lbl_monitor.pack(side=LEFT)

#########################################

# cria um frame para o label
frm_ferramenta = Frame(win_principal, bg="#ced2d9")
frm_ferramenta.pack(side="left", anchor="nw", padx=50, pady=230)

# cria um widget Label com o texto "Apresento uma ferramenta de teste" dentro do novo frame
lbl_ferramenta = Label(frm_ferramenta, text="- Descrevas as premissas para que o projeto seja concluído com sucesso", font=("Arial", 20), bg="#ced2d9")
# empacota o widget no topo do frame
lbl_ferramenta.pack(side="top", anchor="w", padx=10, pady=10)

#########################################

# cria um frame para os campos 1 e 2
frm_campos12 = Frame(frm_ferramenta, bg="#ced2d9")
frm_campos12.pack(side="top", anchor="w", padx=10, pady=10)

# cria um widget Label com o texto "Campo 1:"
lbl_campo1 = Label(frm_campos12, text="Campo 1:", font=("Arial", 16), bg="#ced2d9")
lbl_campo1.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 1
ent_campo1 = Entry(frm_campos12, font=("Arial", 16), width=35)
ent_campo1.pack(side="left", padx=10, pady=10)

# cria um widget Label com o texto "Campo 2:"
lbl_campo2 = Label(frm_campos12, text="Campo 2:", font=("Arial", 16), bg="#ced2d9")
lbl_campo2.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 2
ent_campo2 = Entry(frm_campos12, font=("Arial", 16), width=35)
ent_campo2.pack(side="left", padx=10, pady=10)

# cria um frame para os campos 3 e 4
frm_campos34 = Frame(frm_ferramenta, bg="#ced2d9")
frm_campos34.pack(side="top", anchor="w", padx=10, pady=10)

# cria um widget Label com o texto "Campo 3:"
lbl_campo3 = Label(frm_campos34, text="Campo 3:", font=("Arial", 16), bg="#ced2d9")
lbl_campo3.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 3
ent_campo3 = Entry(frm_campos34, font=("Arial", 16), width=35)
ent_campo3.pack(side="left", padx=10, pady=10)

# cria um widget Label com o texto "Campo 4:"
lbl_campo4 = Label(frm_campos34, text="Campo 4:", font=("Arial", 16), bg="#ced2d9")
lbl_campo4.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 4
ent_campo4 = Entry(frm_campos34, font=("Arial", 16), width=35)
ent_campo4.pack(side="left", padx=10, pady=10)

#########################################

frm_atualizacao = Frame(frm_ferramenta, bg="#ced2d9")
frm_atualizacao.pack(side="top", anchor="w", padx=10, pady=10)

ent_id_atualizacao = tk.Entry(win_principal, font=("Arial", 16), width=8)
ent_id_atualizacao.place(x=190, y=550)

def inserir_dados():
    campo1= ent_campo1.get()
    campo2 = ent_campo2.get()
    campo3 = ent_campo3.get()
    campo4 = ent_campo4.get()
   
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO premissas (campo1,campo2,campo3,campo4) VALUES (?, ?, ?, ?)", (campo1,campo2,campo3,campo4))
    
    conexao.commit()
    conexao.close()
    
    ent_campo1.delete(0, tk.END)
    ent_campo2.delete(0, tk.END)
    ent_campo3.delete(0, tk.END)
    ent_campo4.delete(0, tk.END)

btn = Button(win_principal,text="Salvar", font=("Arial", 12) , width=20, command=inserir_dados)
btn.place(x=560,y=500)

def excluir_dados():

    id_exclusao = ent_id_exclusao.get()

    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM premissas WHERE id=?", (id_exclusao,))

    conexao.commit()

    conexao.close()

    ent_id_exclusao.delete(0, tk.END)

ent_id_exclusao = tk.Entry(win_principal, font=("Arial", 16), width=8)
ent_id_exclusao.place(x=810, y=550)

btn_excluir = tk.Button(win_principal, text="Excluir", font=("Arial", 12), width=20, command=excluir_dados)
btn_excluir.place(x=770, y=500)

def atualizar_dados():
    id_atualizacao = ent_id_atualizacao.get()
    campo1 = ent_campo1.get()
    campo2 = ent_campo2.get()
    campo3 = ent_campo3.get()
    campo4 = ent_campo4.get()

    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    cursor.execute("UPDATE premissas SET campo1=?, campo2=?, campo3=?, campo4=? WHERE id=?", (campo1, campo2, campo3, campo4, id_atualizacao))

    conexao.commit()
    conexao.close()

    ent_id_atualizacao.delete(0, tk.END)
    ent_campo1.delete(0, tk.END)
    ent_campo2.delete(0, tk.END)
    ent_campo3.delete(0, tk.END)
    ent_campo4.delete(0, tk.END)

btn_atualizar = Button(win_principal, text="Atualizar", font=("Arial", 12), width=20, command=atualizar_dados)
btn_atualizar.place(x=150, y=500)

def select_dados():
    id_selecionado = ent_id_select.get()

    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM premissas WHERE id=?", (id_selecionado,))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        janela_resultado = Toplevel(win_principal)
        janela_resultado.title("Resultado do Select")
        janela_resultado.geometry("400x200")

        lbl_campo1_resultado = Label(janela_resultado, text="Campo 1: " + resultado[0])
        lbl_campo1_resultado.pack()

        lbl_campo2_resultado = Label(janela_resultado, text="Campo 2: " + resultado[1])
        lbl_campo2_resultado.pack()

        lbl_campo3_resultado = Label(janela_resultado, text="Campo 3: " + resultado[2])
        lbl_campo3_resultado.pack()

        lbl_campo4_resultado = Label(janela_resultado, text="Campo 4: " + resultado[3])
        lbl_campo4_resultado.pack()

    else:
        messagebox.showinfo("Erro", "ID não encontrado!")


frm_consulta = Frame(win_principal, bg="#ced2d9")
frm_consulta.pack(side="top", anchor="nw", padx=50, pady=10)

ent_id_select = tk.Entry(win_principal, font=("Arial", 16), width=8)
ent_id_select.place(x=390, y=550)

btn_select = tk.Button(win_principal, text="Selecionar", font=("Arial", 12), width=20, command=select_dados)
btn_select.place(x=350, y=500)

##############################################################

win_principal.mainloop()




