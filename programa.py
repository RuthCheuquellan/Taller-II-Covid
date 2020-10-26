import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime

st.title("Titulo de aplicacion");
st.write("Here's our first attempt at using data to create a table:")



if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
c=pd.read_csv(url)
st.line_chart(c["Maule"])


url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto61/serie_fallecidos_comuna.csv"
gu=pd.read_csv(url)




#gu=gu.drop(["CIE 10"],axis=1)
#gu=gu.drop(["Region"],axis=1)
#gu
#countries =gu[""].dropna().unique()

#st.line_chart(gu[gu['Comuna'] == country])
#gu[gu['Comuna'] == country]





left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")


ji=gu.drop(["Region","CIE 10"])

values = st.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
filas = gu.iloc[6]
e=0;
j=0
nombreC=""
datosM={"",""}
nose = gu["Comuna"].unique()
for i in range(len(filas)):
    st.write(nombreC)
    if i==0:
        nombreC=filas[0]
    if i>2:


    e=e+1


