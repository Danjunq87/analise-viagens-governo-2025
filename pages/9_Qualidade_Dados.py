import streamlit as st
import plotly.express as px
from utils.processamento import carregar_dados

st.title("🛠️ Qualidade dos Dados")

st.caption(
    "Indicadores de qualidade da base de viagens de 2025"
)

# Carregar dados
df = carregar_dados()

# Métricas
total_registros = len(df)

registros_sigilo = len(
    df[
        df["Cargo"].isin(
            [
                "NÃO IDENTIFICADO",
                "Informações protegidas por sigilo"
            ]
        )
    ]
)

percentual_sigilo = (
    registros_sigilo / total_registros
) * 100

orgaos = df["Nome órgão solicitante"].nunique()

destinos = df["Destinos"].nunique()

cargos = df["Cargo"].nunique()

# Valores nulos
valores_nulos = (
    df.isnull()
      .sum()
      .sum()
)

# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Registros",
        f"{total_registros:,}"
    )

with col2:
    st.metric(
        "Órgãos",
        f"{orgaos:,}"
    )

with col3:
    st.metric(
        "Destinos",
        f"{destinos:,}"
    )

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Cargos",
        f"{cargos:,}"
    )

with col5:
    st.metric(
        "Valores Nulos",
        f"{valores_nulos:,}"
    )

with col6:
    st.metric(
        "% Sigilo",
        f"{percentual_sigilo:.2f}%"
    )

st.markdown("---")

st.subheader("Campos com Valores Nulos")

nulos = (
    df.isnull()
      .sum()
      .reset_index()
)

nulos.columns = [
    "Campo",
    "Quantidade Nulos"
]

nulos = nulos[
    nulos["Quantidade Nulos"] > 0
]

st.dataframe(
    nulos,
    use_container_width=True
)
qualidade = {
    "Indicador": [
        "Sigilo/Não Identificado",
        "Demais Viagens"
    ],
    "Percentual": [
        percentual_sigilo,
        100 - percentual_sigilo
    ]
}

fig = px.pie(
    qualidade,
    names="Indicador",
    values="Percentual",
    title="Participação das Viagens Sigilosas"
)

st.plotly_chart(
    fig,
    use_container_width=True
)