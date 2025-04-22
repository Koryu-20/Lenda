import streamlit as st
import sqlite3
import os

# Criação ou conexão com o banco de dados SQLite
conn = sqlite3.connect('Dados.db')
cursor = conn.cursor()

# Criação da tabela caso não exista
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

# Função para salvar no banco de dados
def salvar_usuario(nome, email, telefone, senha):
    cursor.execute('''
        INSERT INTO usuarios (nome, email, telefone, senha)
        VALUES (?, ?, ?, ?)
    ''', (nome, email, telefone, senha))
    conn.commit()

# Estado da sessão para armazenar dados temporariamente
if "cadastro_temp" not in st.session_state:
    st.session_state.cadastro_temp = {}

# Interface de Navegação
pagina = st.radio("Navegação", ["Cadastro", "Criar Senha", "Ver Registros"])

# Página 1 - Cadastro com HTML
if pagina == "Cadastro":
    st.title("🌟 A Lenda de Metharion - Cadastro 🌟")

    # Caminho local do HTML (deve estar no mesmo diretório)
    html_file = "Site.html"

    # Verifica se o HTML existe e carrega
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=1000, scrolling=True)
    else:
        st.error("Arquivo HTML 'Site.html' não encontrado no diretório.")

    # Formulário de captura dos dados (com Streamlit também)
    with st.form("form_cadastro"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")
        submit = st.form_submit_button("Próximo Passo ➡️")

        if submit:
            if nome and email and telefone:
                # Armazena os dados temporariamente
                st.session_state.cadastro_temp = {
                    "nome": nome,
                    "email": email,
                    "telefone": telefone
                }
                st.success("Dados cadastrados com sucesso. Agora, crie sua senha!")
                st.experimental_rerun()
            else:
                st.warning("Por favor, preencha todos os campos!")

# Página 2 - Criar senha
elif pagina == "Criar Senha":
    if st.session_state.cadastro_temp:
        st.title("🔐 Criar Senha")
        senha = st.text_input("Digite uma senha", type="password")
        confirmar = st.text_input("Confirme a senha", type="password")

        if st.button("Finalizar Cadastro"):
            if senha == confirmar and senha:
                dados = st.session_state.cadastro_temp
                salvar_usuario(dados["nome"], dados["email"], dados["telefone"], senha)
                st.success("Usuário cadastrado com sucesso!")
                st.session_state.cadastro_temp = {}
            else:
                st.error("As senhas não coincidem ou estão vazias!")
    else:
        st.warning("Você precisa preencher o cadastro antes de criar uma senha.")

# Página 3 - Ver registros
elif pagina == "Ver Registros":
    st.title("📋 Registros no Banco de Dados")
    cursor.execute("SELECT nome, email, telefone FROM usuarios")
    registros = cursor.fetchall()
    if registros:
        for r in registros:
            st.markdown(f"**👤 Nome:** {r[0]}  \n📧 Email: {r[1]}  \n📱 Telefone: {r[2]}")
            st.markdown("---")
    else:
        st.info("Nenhum registro encontrado.")
