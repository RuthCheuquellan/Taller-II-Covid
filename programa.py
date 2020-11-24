import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt

st.title("Titulo de aplicacion");

##############################################################################################
################################      NUEVO CODIGO PRUEVA     ################################
##############################################################################################



##############################   CASOS POR COMUNA DE REGION    ################################
url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna.csv"
ko=pd.read_csv(url)
ko=ko[ko["Comuna"]!="Total"]
############################# SELECTOR REGION  ################
option2 = st.selectbox(
    'Seleciona Region',
     ko["Region"].unique())
url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna_std.csv"
fech =pd.read_csv(url)
############################ SELECTOR FECHA  ###################
option3 = st.selectbox(#selector que aun esta en proseso
    'Seleciona Fecha',
     fech["Fecha"].unique())
ko=ko.rename(columns={'Comuna':'index'}).set_index('index')
h1=ko[ko["Region"]==option2]
ke=h1[option3]
############################  GRAFICO DE BARRAS  ##################
st.bar_chart(ke)

'fffffffff'
url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna_std.csv"
pero=pd.read_csv(url);
comuna=pero["Comuna"].unique()
pero=pero[pero["Comuna"]!="Total"]
option = st.selectbox(#selector que aun esta en proseso
    'Seleciona comuna',
     pero["Comuna"].unique())

url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna_std.csv"
ff=pd.read_csv(url)
ff=ff[ff['Comuna']==option]
ff=ff.rename(columns={'Fecha':'index'}).set_index('index')
st.line_chart(ff['Casos fallecidos'])

