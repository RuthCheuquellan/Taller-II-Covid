import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime

st.title("Titulo de aplicacion");
st.write("Here's our first attempt at using data to create a table:")





url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto61/serie_fallecidos_comuna.csv"
pero=pd.read_csv(url);
comuna=pero["Comuna"].unique()
option = st.selectbox(]#selector que aun esta en proseso
    'Seleciona comuna',
     pero["Comuna"].unique())
#pero12

nuevo=pero["2020-09-07"].unique()#extraigo los datos del dia 7 de septempbre
                                 #fallecido por comuna pero no muestra las comunas
st.bar_chart(nuevo)#imprimo el grafico


"Tabla fallecidos por comuna"
url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto61/serie_fallecidos_comuna.csv"
tabla1=pd.read_csv(url);#se leen los datos de la pagina y se guardan en una variable
tabla1#Imprimo la tabla por pantalla


"Tabla positividad por comuna"
url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto65/PositividadPorComuna.csv"
tabla2=pd.read_csv(url);#se leen los datos de la pagina y se guardan en una variable
tabla2#Imprimo la tabla por pantalla
