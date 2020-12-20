import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt


##########################     OBTENCION DE DATOS      ##################################
@st.cache
def GET_CFPC():
    url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna.csv"  
    return pd.read_csv(url)
@st.cache
def GET_CFPC_STD():
    url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna_std.csv"
    return pd.read_csv(url)
@st.cache
def GET_NNPC():
    url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto63/NNotificacionPorComuna.csv"
    return pd.read_csv(url)
@st.cache
def GET_NNPC_STD():
    url="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto63/NNotificacionPorComuna_std.csv"
    return pd.read_csv(url)
@st.cache
def GET_TTSC():
    URL="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto68/tasa_test_semanal_comunal.csv"
    return pd.read_csv(URL)


st.title("GRAFICOS MUERTES POR COMUNA");

##############################################################################################
################################      NUEVO CODIGO PRUEVA     ################################
##############################################################################################


##############################   CASOS POR COMUNA DE REGION    ################################
ko=GET_CFPC()
ko=ko[ko["Comuna"]!="Total"]
############################# SELECTOR REGION  ################
st.sidebar.title("Selector muertes por Region")
option2 = st.sidebar.selectbox(
    'Seleciona Region',
     ko["Region"].unique())

############################ SELECTOR FECHA  ###################
fech=GET_CFPC_STD()
option3 = st.sidebar.selectbox(#selector que aun esta en proseso
    'Seleciona Fecha',
     fech["Fecha"].unique())
ko=ko.rename(columns={'Comuna':'index'}).set_index('index')

h1=ko[ko["Region"]==option2]
ke=h1[option3]
############################  GRAFICO DE BARRAS  ##################
st.bar_chart(ke)


st.sidebar.title("Selector muertes por comuna")
if st.sidebar.checkbox('Comparacion Comunas Muertes'):
    pero=GET_CFPC_STD()
    comuna=pero["Comuna"].unique()
    pero=pero[pero["Comuna"]!="Total"]
    opcion1 = st.sidebar.selectbox(#selector que aun esta en proseso
        'Seleciona comuna 1',
         pero["Comuna"].unique())
    opcion2 = st.sidebar.selectbox(#selector que aun esta en proseso
        'Seleciona comuna 2',
         pero["Comuna"].unique())
    ff=GET_CFPC_STD()
    ff=ff.rename(columns={'Fecha':'index'}).set_index('index')
    ff1=ff[ff['Comuna']==opcion1]
    ff2=ff[ff['Comuna']==opcion2]
    r1=ff1['Casos fallecidos']
    r2=ff2['Casos fallecidos']

    ########################  CRECION DE GRAFICO    ############################
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(r1, label=opcion1)  # Plot some data on the axes.
    ax.plot(r2, label=opcion2)
    plt.xticks(rotation=90)
    plt.xticks(fontsize=7)
    ax.set_xlabel('Fechas')  # Add an x-label to the axes.
    ax.set_ylabel('Muerte')  # Add a y-label to the axes.
    ax.set_title("Grafico Muertes por comuna")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    fig

##########################################################################################################

##############################   CASOS POR COMUNA DE REGION    ################################

st.title("POSITIVIDAD POR COMUNA");

testP=GET_NNPC()
st.sidebar.title("Selector positividad por region")
selectR = st.sidebar.selectbox(
    'Selecionafe Region',
     testP["Region"].unique())


fechT =GET_NNPC_STD()
############################ SELECTOR FECHA  ###################
selectF = st.sidebar.selectbox(#selector que aun esta en proseso
    'fe Fecha',
     fechT["Fecha"].unique())

testP=testP.rename(columns={'Comuna':'index'}).set_index('index')
T1=testP[testP["Region"]==selectR]
k2=T1[selectF]
############################  GRAFICO DE BARRAS  ##################
st.bar_chart(k2)




comP=GET_TTSC()
st.sidebar.title("Selector positividad por comuna")
if st.sidebar.checkbox('Comparacion Test Comuna'): 
    selectCP1 = st.sidebar.selectbox(#selector que aun esta en proseso
        'Seleciona Comuna Test 1',
         comP["Comuna"].unique())
    selectCP2 = st.sidebar.selectbox(#selector que aun esta en proseso
        'Seleciona Comuna Test 2',
         comP["Comuna"].unique())
    comP1=GET_TTSC()
    comP1=comP1.rename(columns={'fecha':'index'}).set_index('index')
    comP01=comP1[comP1['Comuna']==selectCP1]
    comP02=comP1[comP1['Comuna']==selectCP2]
    rt1=comP01['tasatest']
    rt2=comP02['tasatest']
    rt1=rt1.reset_index(drop=True)
    rt2=rt2.reset_index(drop=True)
    #########################    GRECION DE GRAFICO   ####################
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(rt1, label=selectCP1)  # Plot some data on the axes.
    ax.plot(rt2, label=selectCP2)
    plt.xticks(rotation=90)
    plt.xticks(fontsize=7)
    ax.set_xlabel('Dias')  # Add an x-label to the axes.
    ax.set_ylabel('Porcentaje Positividad por 1000 Test')  # Add a y-label to the axes.
    ax.set_title("Grafico Porcentaje contagios por comuna")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    fig






