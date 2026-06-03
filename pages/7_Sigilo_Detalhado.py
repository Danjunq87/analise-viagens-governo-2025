import streamlit as st
import pandas as pd
import plotly.express as px
from utils.processamento import carregar_dados

st.title("🔒 Sigilo Detalhado")

st.caption(
    "Análise das viagens classificadas como 'NÃO IDENTIFICADO' ou 'Informações protegidas por sigilo'"
)

# Carrega dados
df = carregar_dados()

# Filtra apenas sigilo
df_sigilo = df[
    df["Cargo"].isin([
        "NÃO IDENTIFICADO",
        "Informações protegidas por sigilo"
    ])
]

# Indicadores
total_sigilo = df_sigilo["Despesas"].sum()

qtd_sigilo = len(df_sigilo)

custo_medio_sigilo = total_sigilo / qtd_sigilo

percentual_sigilo = (
    total_sigilo /
    df["Despesas"].sum()
) * 100

# Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Gasto Total",
    f"R$ {total_sigilo/1_000_000_000:.2f} Bi"
)

col2.metric(
    "Viagens",
    f"{qtd_sigilo:,}"
)

col3.metric(
    "Custo Médio",
    f"R$ {custo_medio_sigilo:,.0f}"
)

col4.metric(
    "% dos Gastos Totais",
    f"{percentual_sigilo:.1f}%"
)

st.markdown("---")

# Top órgãos
top_orgaos = (
    df_sigilo
    .groupby("Nome órgão solicitante")
    .agg(
        despesas_totais=("Despesas", "sum"),
        viagens=("Nome", "count")
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
    title="Top 10 Órgãos com Gastos Sigilosos"
)

fig.update_layout(
    template="plotly_white",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Detalhamento")

st.dataframe(
    top_orgaos,
    use_container_width=True
)