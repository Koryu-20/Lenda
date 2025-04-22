import streamlit as st
import streamlit.components.v1 as components

# Lê o conteúdo do HTML
with open("Site.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Exibe o HTML ocupando largura total da tela
components.html(
    html_content,
    height=800,
    width=0,  # permite que ocupe 100% da largura
    scrolling=True
)
