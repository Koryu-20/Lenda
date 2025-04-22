import streamlit as st
import streamlit.components.v1 as components

# Lê o conteúdo do arquivo HTML
with open("Site.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Exibe o HTML no Streamlit com largura maior
components.html(html_content, height=700, width=1200, scrolling=True)
