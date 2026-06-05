
import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():

    caminho = "data/viagens_amostra.csv"

   df = pd.read_csv(
    caminho,
    sep=";",
    decimal=",",
    encoding_errors="ignore"
)

    df["Despesas"] = (
        df["Valor diárias"]
        + df["Valor passagens"]
        + df["Valor outros gastos"]
    )

    df["Cargo"] = df["Cargo"].fillna(
        "NÃO IDENTIFICADO"
    )

    df["Período - Data de início"] = pd.to_datetime(
        df["Período - Data de início"],
        format="%d/%m/%Y"
    )

    df["Período - Data de fim"] = pd.to_datetime(
        df["Período - Data de fim"],
        format="%d/%m/%Y"
    )

    df["Mês da viagem"] = (
        df["Período - Data de início"]
        .dt.month_name()
    )

    df["Dias de viagem"] = (
        df["Período - Data de fim"]
        - df["Período - Data de início"]
    ).dt.days

    return df
