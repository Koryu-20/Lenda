import streamlit as st

# Definindo o título do aplicativo
st.set_page_config(page_title="A Lenda de Metharion", page_icon="🌟")

# CSS personalizado para o fundo e estilo
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: url('https://i.gifer.com/MDg5.gif') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
            padding: 20px;
        }

        h1 {
            font-size: 3rem;
            font-weight: bold;
            margin-top: 30px;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        }

        .form-container {
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            padding: 30px;
            max-width: 500px;
            margin: 40px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .form-container h2 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #ffbf47;
        }

        input[type="text"] {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #ffbf47;
            border-radius: 5px;
            font-size: 1rem;
            background-color: rgba(0, 0, 0, 0.3);
            color: white;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #ff9f00;
        }

        button {
            width: 100%;
            padding: 15px;
            background-color: #ffbf47;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #ff9f00;
        }

        .social-links {
            margin-top: 30px;
        }

        .social-links a {
            color: #ffbf47;
            margin: 10px;
            font-size: 1.4rem;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: #ff9f00;
        }

        .novidades {
            margin-top: 30px;
            font-size: 1.2rem;
            color: #ffbf47;
        }
    </style>
""", unsafe_allow_html=True)

# Título do cabeçalho
st.markdown("<h1>🌟 A Lenda de Metharion 🌟</h1>", unsafe_allow_html=True)

# Formulário de Cadastro
st.markdown('<div class="form-container"><h2>Cadastre-se para receber novidades!</h2>', unsafe_allow_html=True)

# Definindo os campos de entrada
nome = st.text_input("Nome Completo")
email = st.text_input("E-mail")
telefone = st.text_input("Telefone")

# Função para simular o envio de dados
def enviar_email(nome, email, telefone):
    st.success(f"📢 Novo cadastro de {nome} com e-mail {email} e telefone {telefone}!")

def salvar_dados(nome, email, telefone):
    st.write(f"Cadastro de {nome}, {email}, {telefone}")
    return f"Cadastro de {nome} registrado com sucesso!"

# Ao submeter o formulário
if st.button("Cadastrar"):
    if nome and email and telefone:
        resultado = salvar_dados(nome, email, telefone)
        enviar_email(nome, email, telefone)
        st.success(f"✅ {resultado} Você será notificado por e-mail sobre o novo cadastro.")
    else:
        st.error("❌ Por favor, preencha todos os campos!")

# Fechando o form-container
st.markdown('</div>', unsafe_allow_html=True)

# Seção de Redes Sociais
st.markdown("""
    <div class="social-links">
        <h3>Siga-nos nas redes sociais:</h3>
        <a href="https://instagram.com" target="_blank">Instagram</a>
        <a href="https://facebook.com" target="_blank">Facebook</a>
        <a href="https://youtube.com" target="_blank">YouTube</a>
    </div>
""", unsafe_allow_html=True)

# Seção de novidades
st.markdown("""
    <div class="novidades">
        <h3>Novidades:</h3>
        <p>Em breve, mais atualizações sobre a Lenda de Metharion. Fique ligado!</p>
    </div>
""", unsafe_allow_html=True)
