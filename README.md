# Alysida - Previsão de entrega das mercadorias

![Alysyda](alysida.jpg)

O site de Alysida está em http://alysida.com.br/?p=6

## Os dados

Inicialmente, os dados de localização e saída, e localização e chegada, vindos do **Alysida Blockchain**, são registados num dataset. 
A partir de um determinado número de registro, esse dataset é submetido a um algoritmo de machine learning para que aprenda a prever a data de chegada das próximas remessas.

![previsa](previsa.jpg)

## O programa

Executar inicialmente a instalação dos programas

```
pip install -r requirements.txt

```
Serão instalados os programas

- streamlit
- protobuf
- datetime
- yfinance
- numpy
- pystan==2.19.1.1
- plotly
- matplotlib
- fbprophet==0.5
- holidays==0.9.12
- pandas

## Executar o programa

```
streamlit run blockTrajeto2
```
## No Streamlit

Este programa pode ser visto no Streamlit em 

https://share.streamlit.io/luiscarloseiras/alysidaprevisao/main/blockTrajeto2.py


<p align="center">
  <img src="cropped-ALYSIDA-1.png">
</p>
