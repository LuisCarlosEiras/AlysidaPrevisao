# Projeto Alysida. Previsão de entrega da cadeia de suprimentos. 

# Imports
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

# Define a data de inicio para coleta  de dados
INICIO = "01/01/2015"

# Define a data de fim para coleta de dados (data de hoje, execucao do script)
HOJE = date.today().strftime("%d/%m/%Y")

# Define o titulo do Dashboard
st.title("Projeto Alysida. Previsao de entrega da cadeia de suprimentos")

# Define o arquivo com os trajetos das entregas 
trajetos = ('trajeto1.csv','trajeto2.csv','trajeto3.csv')

# Define de qual trajeto usaremos os dados por vez
trajeto_selecionado = st.selectbox('Selecione o arquivo de trajeto para as previsao de rotas:', trajetos)

# Mensagem de carga dos dados
mensagem = st.text('Carregando os dados...')

# Conversao de campo data
df = pd.read_csv(trajeto_selecionado, sep=';')
df['ds'] = pd.to_datetime(df.ds, format='%d/%m/%Y')
df.head()

# Mensagem de encerramento da carga dos dados
mensagem.text('Carregando os dados...Concluido!')

# Sub-titulo
st.subheader('Visualizacao dos Dados Brutos')




# Prepara os dados para as previsões com o pacote Prophet
df_treino = df[['ds','y']]
#df_treino = df_treino.rename(columns = {"Date": "ds", "Close": "y"})
st.write(df_treino.tail())

st.subheader('Previsao com Machine Learning')
# Cria o modelo
modelo = Prophet()

# Treina o modelo
modelo.fit(df_treino)

# Define o horizonte de previsão
num_anos = st.slider('Horizonte de Previsao (de 1 a 4 anos):', 1, 4)

# Calcula o periodo em dias
periodo = num_anos * 365

# Prepara as datas futuras para as previsões
futuro = modelo.make_future_dataframe(periods = periodo)

# Faz as previsões
forecast = modelo.predict(futuro)

# Sub-titulo
st.subheader('Dados Previstos')

# Dados previstos
st.write(forecast.tail())
    
# Titulo
st.subheader('Previsao de entrega da mercadoria a partir do trajeto')

# Plot
grafico2 = plot_plotly(modelo, forecast)
st.plotly_chart(grafico2)

# Referências
# st.write("""Referência: 
# Mini Projeto 2, Data App, Dashboard Financeiro Interativo e em Tempo Real Para Previsão de Ativos Financeiros, 
# Capitulo 5 - Visualização de Dados e Dashboards com Python, Curso Visualização de Dados e Design de Dashboards, Data Science Academy.""")

# Fim
