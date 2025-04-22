import streamlit as st

# Configuração da página
st.set_page_config(page_title="A Lenda de Metharion", layout="centered")

# Estilização com CSS, preservando o design do HTML
st.markdown(
    """
    <style>
        /* Reset de margens e padding */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Cor de fundo e fonte */
        body {
            font-family: 'Arial', sans-serif;
            background: url('https://i.gifer.com/MDg5.gif') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
            padding: 20px;
        }

        /* Cabeçalho */
        h1 {
            font-size: 3rem;
            font-weight: bold;
            margin-top: 30px;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        }

        /* Formulário de Cadastro */
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

        /* Estilo para links de redes sociais */
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

        /* Novidades */
        .novidades {
            margin-top: 30px;
            font-size: 1.2rem;
            color: #ffbf47;
        }

        /* Mensagem de status */
        #mensagemStatus {
            font-size: 1.2rem;
            margin-top: 20px;
        }

        /* Responsividade */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }

            .form-container {
                padding: 20px;
                margin: 20px auto;
            }

            .social-links a {
                font-size: 1.2rem;
            }

            .novidades {
                font-size: 1.1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True
)

# Título principal
st.markdown("<h1>🌟 A Lenda de Metharion 🌟</h1>", unsafe_allow_html=True)

# Formulário
with st.form(key='formCadastro'):
    st.markdown("<h2>Cadastre-se para receber novidades!</h2>", unsafe_allow_html=True)

    nome = st.text_input("Nome Completo", placeholder="Digite seu nome")
    email = st.text_input("E-mail", placeholder="Digite seu e-mail")
    telefone = st.text_input("Telefone", placeholder="Digite seu telefone")
    
    # Botão de envio do formulário
    enviar = st.form_submit_button("Cadastrar")

    # Lógica de validação e resposta
    if enviar:
        if nome and email and telefone:
            st.success(f"✅ Cadastro de {nome} registrado com sucesso!")
            st.info("📧 Você será notificado por e-mail sobre o novo cadastro.")
        else:
            st.error("❌ Por favor, preencha todos os campos!")

# Seção de redes sociais
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
