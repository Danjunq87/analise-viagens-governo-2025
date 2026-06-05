import pandas as pd

print("Lendo arquivo...")

df = pd.read_csv(
    "data/2025_Viagem.csv",
    encoding="Windows-1252",
    sep=";",
    decimal=","
)

print("Criando amostra...")

amostra = df.sample(
    n=100000,
    random_state=42
)

amostra.to_csv(
    "data/viagens_amostra.csv",
    index=False,
    sep=";"
)

print("Arquivo criado com sucesso!")