import streamlit as st
import plotly.express as px
from utils.processamento import carregar_dados

st.title("📊 Painel Executivo")

st.caption(
    "Resumo estratégico das viagens oficiais do Governo Federal - 2025"
)

# Carregar dados
df = carregar_dados()

# Métricas principais
total_viagens = len(df)

gasto_total = df["Despesas"].sum()

custo_medio = gasto_total / total_viagens

# Sigilo
df_sigilo = df[
    df["Cargo"].isin(
        [
            "NÃO IDENTIFICADO",
            "Informações protegidas por sigilo"
        ]
    )
]

percentual_sigilo = (
    len(df_sigilo) / total_viagens
) * 100

# Top órgão
top_orgao = (
    df.groupby("Nome órgão solicitante")["Despesas"]
      .sum()
      .sort_values(ascending=False)
)

# Top destino
top_destino = (
    df["Destinos"]
    .value_counts()
)

# Cards principais
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Viagens",
    f"{total_viagens:,}"
)

col2.metric(
    "Gasto Total",
    f"R$ {gasto_total/1_000_000_000:.2f} Bi"
)

col3.metric(
    "Custo Médio",
    f"R$ {custo_medio:,.0f}"
)

col4.metric(
    "% Sigilo",
    f"{percentual_sigilo:.2f}%"
)

st.markdown("---")

# Insights
st.subheader("📌 Destaques")

st.success(
    f"""
    Órgão com maior gasto:

    {top_orgao.index[0]}

    Total: R$ {top_orgao.iloc[0]:,.2f}
    """
)

st.info(
    f"""
    Destino mais frequente:

    {top_destino.index[0]}

    Total de viagens:
    {top_destino.iloc[0]:,}
    """
)

st.warning(
    f"""
    Viagens classificadas como sigilo ou não identificadas:

    {len(df_sigilo):,}

    Representam {percentual_sigilo:.2f}% das viagens.
    """
)

st.markdown("---")

# Top 10 órgãos
top10 = (
    df.groupby("Nome órgão solicitante")
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
    top10,
    x="despesas_totais",
    y="Nome órgão solicitante",
    orientation="h",
    title="Top 10 Órgãos por Despesa"
)

fig.update_layout(
    template="plotly_white",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)