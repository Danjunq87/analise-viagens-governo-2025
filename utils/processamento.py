import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():

    caminho = "data/viagens_amostra.csv"

    df = pd.read_csv(
        caminho,
        sep=";",
        encoding_errors="ignore",
        low_memory=False
    )

    # Converter colunas monetárias para número
    colunas_valor = [
        "Valor diárias",
        "Valor passagens",
        "Valor outros gastos"
    ]

    for coluna in colunas_valor:

        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )

        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        )

    # Substituir valores nulos por zero
    df[colunas_valor] = df[colunas_valor].fillna(0)

    # Criar coluna de despesas totais
    df["Despesas"] = (
        df["Valor diárias"]
        + df["Valor passagens"]
        + df["Valor outros gastos"]
    )

    # Cargo
    df["Cargo"] = df["Cargo"].fillna(
        "NÃO IDENTIFICADO"
    )

    # Datas
    df["Período - Data de início"] = pd.to_datetime(
        df["Período - Data de início"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    df["Período - Data de fim"] = pd.to_datetime(
        df["Período - Data de fim"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    # Mês da viagem
    df["Mês da viagem"] = (
        df["Período - Data de início"]
        .dt.month_name()
    )

    # Dias de viagem
    df["Dias de viagem"] = (
        df["Período - Data de fim"]
        - df["Período - Data de início"]
    ).dt.days

    return df