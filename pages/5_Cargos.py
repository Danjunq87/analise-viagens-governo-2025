
import streamlit as st
import plotly.express as px
from utils.processamento import carregar_dados

st.title("👔 Cargos")
st.caption(
    "Fonte: Portal da Transparência do Governo Federal"
)
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

top_cargos = (
    df
    .groupby("Cargo")
    .agg(
        despesa_media=("Despesas","mean"),
        quantidade_viagens=("Nome","count")
    )
    .reset_index()
)

top_cargos = (
    top_cargos[
        top_cargos["quantidade_viagens"] >= 50
    ]
    .sort_values(
        by="despesa_media",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_cargos,
    x="despesa_media",
    y="Cargo",
    orientation="h",
    title="Top 10 Cargos por Despesa Média"
)
fig.update_layout(
    template="plotly_white",
    height=600
)
st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(top_cargos)
