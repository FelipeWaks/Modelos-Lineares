import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Modelos Lineares",layout='centered')

def load_data():
    data = pd.read_csv("CO2_Emissions_Canada.csv")
    data.columns = ['Marca','Modelo','Classe','Tam_Motor','Cinlindros','Cambio','Tipo_Combustivel','Consumo_Cidade','Consumo_Rodovia','Consumo_Comb_1','Consumo_Comb_2',"Emissao_Co2"]
    return data

pag_ap = st.Page(
    page="pages/apresentacao.py",
    title = "Apresentação",
    default= True


)

pag_descritiva = st.Page(
    page= "pages/descritiva.py",
    title="Descritiva"
)

pag_regressao = st.Page(
    page= "pages/dummyregression.py",
    title="Regressão"
)


pg = st.navigation(
    {
        'Info ℹ️': [pag_ap],
        'Análises 📈': [pag_descritiva,pag_regressao]
    }
)


pg.run()
