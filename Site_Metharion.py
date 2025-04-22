import streamlit as st
import streamlit.components.v1 as components

# Lê o conteúdo do arquivo HTML
with open("Site.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Exibe o HTML ocupando 100% da largura da tela
components.html(
    html_content,
    height=700,
    width=0,  # necessário para permitir largura customizada
    scrolling=True
)
