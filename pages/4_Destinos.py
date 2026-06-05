
import streamlit as st
import plotly.express as px
from utils.processamento import carregar_dados

st.title("🌎 Destinos")

df = carregar_dados()
st.sidebar.header("Filtros")

orgao = st.sidebar.selectbox(
    "Órgão",
    ["Todos"] + sorted(
        df["Nome órgão solicitante"]
        .dropna()
        .unique()
    )
)

if orgao != "Todos":
    df = df[
        df["Nome órgão solicitante"] == orgao
    ]

top_destinos = (
    df
    .groupby("Destinos")
    .agg(
        despesas_totais=("Despesas","sum")
    )
    .reset_index()
    .sort_values(
        by="despesas_totais",
        ascending=False
    )
    .head(20)
)

fig = px.bar(
    top_destinos,
    x="despesas_totais",
    y="Destinos",
    orientation="h",
    title="Top 20 Destinos com Maiores Gastos"
)
fig.update_layout(
    template="plotly_white",
    height=600
)
st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(top_destinos)
