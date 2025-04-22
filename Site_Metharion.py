import streamlit as st

# Configura a página com layout wide
st.set_page_config(page_title="A Lenda de Metharion", layout="centered")

# Estilização (adaptando o CSS do HTML para Streamlit)
st.markdown(
    """
    <style>
    body {
        background: url('https://i.gifer.com/MDg5.gif') no-repeat center center fixed;
        background-size: cover;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 15px;
        color: white;
    }
    h1, h2, h3, p, label {
        color: white !important;
        text-align: center;
    }
    .form-title, .stTextInput label {
        color: #ffbf47 !important;  /* Laranja nas frases e labels */
    }
    .stButton button {
        background-color: #ffbf47 !important; /* Laranja no botão */
        color: white !important;
    }
    .stButton button:hover {
        background-color: #ff9f00 !important; /* Laranja mais intenso no hover */
    }
    .stTextInput input {
        color: white !important;
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: 2px solid #ffbf47 !important;
    }
    .stTextInput input:focus {
        border-color: #ff9f00 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown("<h1>🌟 A Lenda de Metharion 🌟</h1>", unsafe_allow_html=True)

# Título do formulário
st.markdown("<h2 class='form-title'>Cadastre-se para receber novidades!</h2>", unsafe_allow_html=True)

# Formulário
with st.form("formulario_metharion"):
    nome = st.text_input("Nome Completo")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    enviar = st.form_submit_button("Cadastrar")

# Lógica de validação e resposta
if enviar:
    if nome.strip() and email.strip() and telefone.strip():
        st.success(f"✅ Cadastro de {nome} registrado com sucesso!")
        st.info("📧 Você será notificado por e-mail sobre o novo cadastro.")
    else:
        st.error("❌ Por favor, preencha todos os campos!")

# Redes sociais
st.markdown("### Siga-nos nas redes sociais:")
st.markdown("""
<a href="https://instagram.com" target="_blank">Instagram</a> | 
<a href="https://facebook.com" target="_blank">Facebook</a> | 
<a href="https://youtube.com" target="_blank">YouTube</a>
""", unsafe_allow_html=True)

# Novidades
st.markdown("### Novidades:")
st.markdown("Em breve, mais atualizações sobre a Lenda de Metharion. Fique ligado!")
