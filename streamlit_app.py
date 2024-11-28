import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Modelos Lineares",layout='centered')
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
