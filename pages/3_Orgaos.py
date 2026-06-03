import streamlit as st
import plotly.express as px
from utils.processamento import carregar_dados

st.title("🏛️ Órgãos com Maiores Gastos")

st.caption(
    "Fonte: Portal da Transparência do Governo Federal"
)

df = carregar_dados()

top_orgaos = (
    df
    .groupby("Nome órgão solicitante")
    .agg(
        despesas_totais=("Despesas", "sum")
    )
    .reset_index()
    .sort_values(
        by="despesas_totais",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_orgaos,
    x="despesas_totais",
    y="Nome órgão solicitante",
    orientation="h",
    title="Top 10 Órgãos com Maiores Gastos"
)

fig.update_layout(
    template="plotly_white",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    top_orgaos,
    use_container_width=True
)