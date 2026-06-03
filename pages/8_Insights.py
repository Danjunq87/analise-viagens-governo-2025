import streamlit as st
from utils.processamento import carregar_dados

st.title("🧠 Insights Automáticos")

st.caption(
    "Principais conclusões encontradas nos dados de viagens de 2025"
)

# Carrega dados
df = carregar_dados()

# Gasto total
gasto_total = df["Despesas"].sum()

# Órgão com maior gasto
orgao_top = (
    df.groupby("Nome órgão solicitante")["Despesas"]
      .sum()
      .sort_values(ascending=False)
)

orgao_nome = orgao_top.index[0]
orgao_valor = orgao_top.iloc[0]

# Destino mais frequente
destino_top = (
    df["Destinos"]
    .value_counts()
)

destino_nome = destino_top.index[0]
destino_qtd = destino_top.iloc[0]

# Cargo com maior despesa média
cargo_top = (
    df.groupby("Cargo")["Despesas"]
      .mean()
      .sort_values(ascending=False)
)

cargo_nome = cargo_top.index[0]
cargo_valor = cargo_top.iloc[0]

# Sigilo
df_sigilo = df[
    df["Cargo"].isin([
        "NÃO IDENTIFICADO",
        "Informações protegidas por sigilo"
    ])
]

percentual_sigilo = (
    df_sigilo["Despesas"].sum()
    / gasto_total
) * 100

# Quantidade de viagens
total_viagens = len(df)

viagens_sigilo = len(df_sigilo)

# Cards
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total de Viagens",
        f"{total_viagens:,}"
    )

with col2:
    st.metric(
        "Gasto Total",
        f"R$ {gasto_total/1_000_000_000:.2f} Bi"
    )

st.markdown("---")

st.subheader("Principais Descobertas")

st.success(
    f"""
    🏛️ O órgão com maior gasto em viagens foi:

    {orgao_nome}

    Total gasto: R$ {orgao_valor:,.2f}
    """
)

st.info(
    f"""
    🌎 O destino mais frequente foi:

    {destino_nome}

    Total de viagens: {destino_qtd:,}
    """
)

st.warning(
    f"""
    👔 O cargo com maior despesa média foi:

    {cargo_nome}

    Média: R$ {cargo_valor:,.2f}
    """
)

st.error(
    f"""
    🔒 Viagens classificadas como sigilo ou não identificadas representam:

    {percentual_sigilo:.2f}% dos gastos totais

    Quantidade de viagens: {viagens_sigilo:,}
    """
)

st.markdown("---")

st.subheader("Resumo Executivo")

st.write(
    f"""
    Em 2025 foram registradas {total_viagens:,} viagens oficiais,
    totalizando R$ {gasto_total/1_000_000_000:.2f} bilhões em despesas.

    O órgão com maior gasto foi '{orgao_nome}'.

    O destino mais frequente foi '{destino_nome}'.

    As viagens classificadas como sigilo ou não identificadas
    responderam por {percentual_sigilo:.2f}% do total gasto.
    """
)
st.markdown("---")

st.subheader("📌 Achados Relevantes")

st.success(
    """
    Foram analisadas mais de 807 mil viagens oficiais
    realizadas por 207 órgãos públicos diferentes.
    """
)

st.warning(
    """
    Mais da metade das viagens registradas (51,56%)
    foram classificadas como sigilo ou não identificadas.
    """
)

st.info(
    """
    A base contém quase 37 mil destinos diferentes,
    indicando ampla dispersão geográfica das viagens.
    """
)

st.error(
    """
    Foram encontrados 6.387 valores ausentes,
    demonstrando a importância do tratamento e
    validação dos dados antes da análise.
    """
)