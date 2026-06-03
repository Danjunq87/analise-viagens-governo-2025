
import streamlit as st
from utils.processamento import carregar_dados

df = carregar_dados()

st.title("🔒 Viagens com Sigilo ou Não Identificadas")
st.caption(
    "Fonte: Portal da Transparência do Governo Federal"
)

df_sigilo = df[
    df["Cargo"].isin([
        "NÃO IDENTIFICADO",
        "Informações protegidas por sigilo"
    ])
]

total_gastos = df["Despesas"].sum()
total_sigilo = df_sigilo["Despesas"].sum()

percentual_gastos = (
    total_sigilo / total_gastos
) * 100

total_viagens = len(df)
viagens_sigilo = len(df_sigilo)

percentual_viagens = (
    viagens_sigilo / total_viagens
) * 100

custo_medio_sigilo = (
    total_sigilo / viagens_sigilo
)

custo_medio_geral = (
    total_gastos / total_viagens
)

col1, col2 = st.columns(2)

col1.metric(
    "% dos Gastos",
    f"{percentual_gastos:.2f}%"
)

col2.metric(
    "% das Viagens",
    f"{percentual_viagens:.2f}%"
)

st.markdown("---")

st.metric(
    "Custo Médio (Sigilo/Não Identificado)",
    f"R$ {custo_medio_sigilo:,.2f}"
)

st.metric(
    "Custo Médio Geral",
    f"R$ {custo_medio_geral:,.2f}"
)
