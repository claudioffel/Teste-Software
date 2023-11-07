from tkinter import *
import tkinter as tk
import sqlite3

win_principal = Tk()
# Propriedades da Janela
win_principal.title("Gestão de Teste de Software")
win_principal.configure(background="#ced2d9")

# Define o tamanho da janela principal
win_principal.geometry("1375x700")

def visualiza():
    pass

frm_planoteste = Frame(win_principal,bg='#00CED1',highlightbackground='#00CED1',highlightthickness=4)
frm_planoteste.place(relx= 0.01, rely=0.01, relwidth=0.98, relheight=0.30)

lbl_identificacao = Label(frm_planoteste, text="Artefatos", font=("Arial", 50), bg="#00CED1", fg="white")

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
lbl_ferramenta = Label(frm_ferramenta, text="- Preencha as informações do artefato de entrada e de saída abaixo:", font=("Arial", 20), bg="#ced2d9")
# empacota o widget no topo do frame
lbl_ferramenta.pack(side="top", anchor="w", padx=10, pady=10)

#########################################

# cria um frame para os campos 1 e 2
frm_campos12 = Frame(frm_ferramenta, bg="#ced2d9")
frm_campos12.pack(side="top", anchor="w", padx=10, pady=10)

# cria um widget Label com o texto "Campo 1:"
lbl_campo1 = Label(frm_campos12, text="", font=("Arial", 16), bg="#ced2d9")
lbl_campo1.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 1
ent_campo1 = Entry(frm_campos12, font=("Arial", 16), width=30)
ent_campo1.pack(side="left", padx=10, pady=10)

# cria um widget Label com o texto "Campo 2:"
lbl_campo2 = Label(frm_campos12, text="", font=("Arial", 16), bg="#ced2d9")
lbl_campo2.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 2
ent_campo2 = Entry(frm_campos12, font=("Arial", 16), width=30)
ent_campo2.pack(side="left", padx=10, pady=10)

# cria um frame para os campos 3 e 4
frm_campos34 = Frame(frm_ferramenta, bg="#ced2d9")
frm_campos34.pack(side="top", anchor="w", padx=10, pady=10)

# cria um widget Label com o texto "Campo 3:"
lbl_campo3 = Label(frm_campos34, text="", font=("Arial", 16), bg="#ced2d9")
lbl_campo3.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 3
ent_campo3 = Entry(frm_campos34, font=("Arial", 16), width=30)
ent_campo3.pack(side="left", padx=10, pady=10)

# cria um widget Label com o texto "Campo 4:"
lbl_campo4 = Label(frm_campos34, text="", font=("Arial", 16), bg="#ced2d9")
lbl_campo4.pack(side="left", padx=10, pady=10)

# cria um widget Entry para capturar as informações do campo 4
ent_campo4 = Entry(frm_campos34, font=("Arial", 16), width=30)
ent_campo4.pack(side="left", padx=10, pady=10)

#########################################

def inserir_dados():
    id = ent_id.get()
    campo1= ent_campo1.get()
    campo2 = ent_campo2.get()
    campo3 = ent_campo3.get()
    campo4 = ent_campo4.get()

    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO artefatos (id,campo1,campo2,campo3,campo4) VALUES (?, ?, ?, ?, ?)", (id,campo1,campo2,campo3,campo4))
    
    conexao.commit()
    conexao.close()
    
    ent_campo1.delete(0, tk.END)
    ent_campo2.delete(0, tk.END)
    ent_campo3.delete(0, tk.END)
    ent_campo4.delete(0, tk.END)
    ent_id.delete(0, tk.END)


def alterar_dados():


    id = ent_id.get()
    campo1= ent_campo1.get()
    campo2 = ent_campo2.get()
    campo3 = ent_campo3.get()
    campo4 = ent_campo4.get()
   
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE artefatos SET campo1 = ?, campo2 = ?, campo3 = ?, campo4 = ? WHERE id = ?", (campo1,campo2,campo3,campo4,id))
    
    conexao.commit()
    conexao.close()

    ent_campo1.delete(0, tk.END)
    ent_campo2.delete(0, tk.END)
    ent_campo3.delete(0, tk.END)
    ent_campo4.delete(0, tk.END)
    ent_id.delete(0, tk.END)

   

def excluir_dados():
    id = ent_id.get()
   
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM artefatos WHERE id = ?", (id,))
    
    conexao.commit()
    conexao.close()

    ent_id.delete(0, tk.END)

def selecionar_dados():
    id = ent_id.get()
   
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM artefatos WHERE id = ?", (id,))
    dados = cursor.fetchone()
    
    if dados:
        ent_campo1.delete(0, tk.END)
        ent_campo1.insert(tk.END, dados[0])
        
        ent_campo2.delete(0, tk.END)
        ent_campo2.insert(tk.END, dados[1])
        
        ent_campo3.delete(0, tk.END)
        ent_campo3.insert(tk.END, dados[2])

        ent_campo4.delete(0, tk.END)
        ent_campo4.insert(tk.END, dados[3])

    id = ent_id.get()
    
    conexao.close()


lbl_id = Label(win_principal, text="ID:", font=("Arial", 16), bg="#ced2d9")
lbl_id.place(x=100,y=450)


# cria um widget Entry para capturar as informações do campo 3
ent_id = Entry(win_principal, font=("Arial", 16), width=30)
ent_id.place(x=160,y=450)

btn = Button(win_principal,text="Alterar", font=("Arial", 12) , width=8, command=alterar_dados)
btn.place(x=160,y=490)

btn = Button(win_principal,text="Selecionar", font=("Arial", 12) , width=8, command=selecionar_dados)
btn.place(x=280,y=490)

btn = Button(win_principal,text="Excluir", font=("Arial", 12) , width=8, command=excluir_dados)
btn.place(x=400,y=490)

btn = Button(win_principal,text="Salvar", font=("Arial", 12) , width=20, command=inserir_dados)
btn.place(x=560,y=600)

win_principal.mainloop()






'''
# Função para criar a tabela "premissas"
def criar_tabela():
    # Conecta ao banco de dados
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    # Exclui a tabela "premissas" se ela já existir
    cursor.execute("DROP TABLE IF EXISTS premissas")

    # Cria a tabela "premissas" com as colunas corretas
    cursor.execute("""
        CREATE TABLE premissas (
            campo3 TEXT,
            campo4 TEXT
        )
    """)

    # Fecha a conexão com o banco de dados
    conexao.close()

# Chama a função criar_tabela() antes de inserir dados
criar_tabela()

# Função para inserir dados no banco de dados
def inserir_dados():
    # Obtém os valores digitados nos campos
    campo3 = ent_campo3.get()
    campo4 = ent_campo4.get()

    # Conecta ao banco de dados
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    # Insere os dados na tabela
    cursor.execute("INSERT INTO premissas (campo3, campo4) VALUES (?, ?)", (campo3, campo4))

    # Commit das alterações
    conexao.commit()

    # Fecha a conexão com o banco de dados
    conexao.close()

    # Teste: Recupera os registros da tabela "premissas"
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM premissas")
    registros = cursor.fetchall()

    # Exibe os registros recuperados
    for registro in registros:
        print(registro)

    # Fecha a conexão com o banco de dados
    conexao.close()

    # Limpa os campos de entrada
    ent_campo3.delete(0, END)
    ent_campo4.delete(0, END)

# Configura o botão "Inserir" para chamar a função inserir_dados() quando clicado
btn = Button(win_principal,text="Salvar", font=("Arial", 12) , width=20, command=inserir_dados)
btn.place(x=560,y=500)

#########################################
'''


