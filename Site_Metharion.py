import streamlit as st
import requests

# Defina a URL do arquivo HTML no GitHub
url = "https://raw.githubusercontent.com/Koryu-20/Lenda/main/Site.html"

# Requisita o conteúdo do arquivo HTML
response = requests.get(url)

# Verifique se o arquivo foi encontrado
if response.status_code == 200:
    html_content = response.text
else:
    html_content = "Erro ao carregar o arquivo HTML."

# Exibe o conteúdo HTML no Streamlit
st.components.v1.html(html_content, height=600)
