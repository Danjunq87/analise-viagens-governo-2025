import streamlit as st
import plotly.express as px
from utils.processamento import carregar_dados

st.title("📈 Evolução Mensal")
st.caption(
    "Fonte: Portal da Transparência do Governo Federal"
)

df = carregar_dados()
ordem_meses = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

gastos_mes = (
    df.groupby("Mês da viagem")
      .agg(gastos=("Despesas", "sum"))
      .reset_index()
)

fig = px.line(
    gastos_mes,
    x="Mês da viagem",
    y="gastos",
    markers=True,
    title="Gastos por Mês"
)

fig.update_layout(
    template="plotly_white",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)