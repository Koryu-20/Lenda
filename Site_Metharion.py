import streamlit as st
import sqlite3
import os
import streamlit.components.v1 as components

# Banco de Dados
def init_db():
    if not os.path.exists("Dados.db"):
        conn = sqlite3.connect("Dados.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

def salvar_dados(nome, email, telefone, senha):
    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, telefone, senha) VALUES (?, ?, ?, ?)",
                   (nome, email, telefone, senha))
    conn.commit()
    conn.close()

# Inicializa o banco se não existir
init_db()

# Exibe o HTML da interface
with open("Site.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=400)

# Formulário com Streamlit
st.subheader("Preencha os dados abaixo:")

with st.form("form_usuario"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    senha = st.text_input("Senha", type="password")
    
    enviar = st.form_submit_button("Enviar")

if enviar:
    if nome and email and telefone and senha:
        salvar_dados(nome, email, telefone, senha)
        st.success("✅ Dados salvos com sucesso!")
    else:
        st.warning("⚠️ Preencha todos os campos!")
