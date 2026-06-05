import streamlit as st

st.set_page_config(
    page_title="Análise de Viagens 2025",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Painel de Viagens Oficiais do Governo Federal")

st.markdown("""
### Bem-vindo ao Dashboard

Este projeto apresenta uma análise das viagens oficiais do Governo Federal em 2025 utilizando dados do Portal da Transparência.

### Páginas disponíveis:

📈 Visão Geral

🔒 Sigilo e Não Identificados

🏛️ Órgãos

🌎 Destinos

👔 Cargos

---

Utilize o menu lateral para navegar entre as análises.
""")

st.info(
    "Projeto desenvolvido com Python, Pandas, Plotly e Streamlit."
)