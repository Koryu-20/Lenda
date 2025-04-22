import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    body {
        background: url('https://i.gifer.com/MDg5.gif') no-repeat center center fixed;
        background-size: cover;
    }
    .stApp {
        background-color: rgba(0,0,0,0.7);
        padding: 2rem;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>🌟 A Lenda de Metharion 🌟</h1>", unsafe_allow_html=True)

st.markdown("### Cadastre-se para receber novidades!", unsafe_allow_html=True)

# Formulário de entrada
with st.form(key='form_cadastro'):
    nome = st.text_input("Nome completo")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    submit = st.form_submit_button("Cadastrar")

# Validação
if submit:
    if nome and email and telefone:
        st.success(f"✅ Cadastro de {nome} realizado com sucesso!")
        st.info("Você será notificado por e-mail sobre o novo cadastro.")
    else:
        st.error("❌ Por favor, preencha todos os campos corretamente.")
