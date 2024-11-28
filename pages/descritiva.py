import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_app.py import load_data()


df = load_data()

st.title("Vizualização")
with st.expander('Dados'):
    st.write('**Dados Brutos**')
    df


val_y = ['Consumo_Cidade','Consumo_Rodovia',"Emissao_Co2"]
val_x = ['Marca','Modelo','Classe','Tam_Motor','Cinlindros','Cambio','Tipo_Combustivel']

st.markdown(""" 

    ### Box-Plot

""")

col1, col2 = st.columns(2)

with col1: 
    y = st.selectbox("Variável do Eixo Y",val_y)

with col2:
    x = st.selectbox("Variável do Eixo X",val_x)

var_desejadas = st.multiselect(f"Selecione os elementos da variável **{x}**",df[x].unique(),placeholder="Escolha uma ou mais")

df_ = df[df[x].isin(var_desejadas)]

if(st.button("Gerar Box-Plot")):
    if(len(var_desejadas)==0):
        st.warning("Selecione pelo menos uma opção")
    else:
        fig = px.box(df_,x=x,y=y,points='suspectedoutliers')
        st.plotly_chart(fig,use_container_width=True)



st.markdown(""" 

    ### Scatter-Plot

""")


col3, col4 = st.columns(2)
with col3:
     #Permite selecionar Todas as variáveis numéricas
     y = st.selectbox("Variável do Eixo Y",val_y,key="Scatter-Y")

with col4:
    #Permite selecionar as Variáveis numéricas com excessao da que foi escolhida acima
    x = st.selectbox("Variável do Eixo X",[item for item in val_y if item != y],key="Scatter-X")

#Cor dos pontos será definida por essa variável
categoria = st.selectbox("Variável Categórica",val_x)

#Quis elementos da categoria devem ser incluidos 

var_desejadas_scatter_plot = st.multiselect(f"Selecione os elementos da variável **{categoria}**",df[categoria].unique(),placeholder="Escolha uma ou mais",key="muilti2")

#Dados para o plot
df_ = df[df[categoria].isin(var_desejadas_scatter_plot)]

if(st.button("Gerar Scatter-Plot:",key="botao2")):
    if(len(var_desejadas_scatter_plot)==0):
        st.warning("Selecione pelo menos uma opção")
    else:
        fig2 = px.scatter(y=y,x=x,color=categoria,data_frame=df_)
        st.plotly_chart(fig2)
