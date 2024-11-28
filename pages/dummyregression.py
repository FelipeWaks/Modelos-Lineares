import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt



df = load_data()

st.title("Regressão")

#Possíveis escolhas do usuário

respostas = ["Emissao_Co2", 'Consumo_Cidade', 'Consumo_Rodovia']
transforms = ["Nenhuma","log(y)","1/y"]
marcas_desejadas = st.multiselect("Selecione as Marcas",df['Marca'].unique(),placeholder="Escolha uma ou mais Marcas")


df = df[df['Marca'].isin(marcas_desejadas)]

X = pd.get_dummies(df['Marca'],drop_first=True,dtype= 'int')




X['(Intercept)'] = 1
cols = X.columns.tolist()
cols = cols[-1:] + cols[:-1]
X = X[cols]


# Caixa de seleção múltipla
resposta = st.selectbox('Escolha a variável resposta', respostas)
transform = st.selectbox('Selecione a transformação',transforms)
y = df[resposta]
if(transform=='log(y)'):
    y = np.log(y)
if(transform=='1/y'):
    y = 1/y

if(st.button("Executar Regressão")):
    
    #Executa a regressao
    result = sm.OLS(y,X).fit()
    st.write((result.summary()))
    
    #Guarda resíduos e valores ajustados
    residuos = result.resid
    valores_ajustados = result.fittedvalues
    
    #Histograma

    hist, ax = plt.subplots()
    qqplot, ax2 = plt.subplots()
    sns.histplot(residuos,ax=ax)
    ax.set_xlabel("Valor dos Resíduos")
    ax.set_ylabel("Contagem")
    ax.set_title("Histograma dos Resíduos")

    st.pyplot(hist)
    
    #Q-Q plot
    sm.qqplot(residuos,line='s',ax = ax2)
    ax2.set_xlabel("Quantis Teóricos")
    ax2.set_ylabel("Quantis Amostrais")
    ax2.set_title("Q-Q Plot")
    st.pyplot(qqplot)

    #Resíduos Vs Ajustados
    res_vs_ajust, ax3 = plt.subplots()
    ax3.scatter(valores_ajustados, residuos, color='blue', alpha=0.6)
    ax3.axhline(y=0, color='r', linestyle='--')
    ax3.set_title("Resíduos vs Ajustados")
    ax3.set_xlabel("Valores Ajustados")
    ax3.set_ylabel("Resíduos")
    st.pyplot(res_vs_ajust)
