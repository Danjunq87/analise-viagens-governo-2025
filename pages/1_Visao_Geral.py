import streamlit as st
from utils.processamento import carregar_dados

st.title("📊 Dashboard Executivo")
st.caption(
    "Fonte: Portal da Transparência do Governo Federal"
)
df = carregar_dados()

# Métricas principais
total_viagens = len(df)

total_gastos = df["Despesas"].sum()

custo_medio = total_gastos / total_viagens

df_sigilo = df[
    df["Cargo"].isin(
        [
            "NÃO IDENTIFICADO",
            "Informações protegidas por sigilo"
        ]
    )
]

percentual_sigilo = (
    df_sigilo["Despesas"].sum()
    / total_gastos
) * 100

# Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total de Viagens",
    f"{total_viagens:,}"
)

col2.metric(
    "Gastos Totais",
    f"R$ {total_gastos/1_000_000_000:.2f} Bi"
)

col3.metric(
    "Custo Médio",
    f"R$ {custo_medio:,.0f}"
)

col4.metric(
    "% Sigilo",
    f"{percentual_sigilo:.1f}%"
)

st.markdown("---")
percentual_viagens_sigilo = (
    len(df_sigilo) / len(df)
) * 100

st.warning(
    """
    ⚠️ Mais da metade das viagens registradas em 2025
    foram classificadas como "NÃO IDENTIFICADO" ou
    "Informações protegidas por sigilo".

    Essas viagens representam aproximadamente
    51,56% do total de viagens registradas.
    """
)

st.subheader("Resumo Executivo")

st.write(f"""
Foram registradas **{total_viagens:,} viagens**
com um gasto total de
**R$ {total_gastos/1_000_000_000:.2f} bilhões**.

As viagens classificadas como
**sigilo ou não identificadas**
representam aproximadamente
**{percentual_sigilo:.1f}%**
dos gastos totais.
""")