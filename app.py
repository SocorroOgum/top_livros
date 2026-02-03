import streamlit as st
import pandas as pd
import plotly.express as px

#seta o layout para preencher a janela
st.set_page_config(layout="wide")

#atribui a uma classe o leitor de CSV do pandas
df_reviews = pd.read_csv("C:/Users/MaiconZ/Documents/Pitóun/datasets/customer reviews.csv")
df_top100_books = pd.read_csv("C:/Users/MaiconZ/Documents/Pitóun/datasets/Top-100 Trending Books.csv")

#define um valor máximo e mínimo de preços de livros, de acordo com o CSV
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

#cria um slider de barrinha, com sidebar ou sem sidebar
barrinha = st.sidebar.slider("Dedilha aqui", price_min, price_max, price_max)
#Regula a tabela pra ficar menor ou igual ao valor da barrinha 
df_books = df_top100_books[df_top100_books["book price"] <= barrinha]

#executa a tabela
df_books

#cria tabela, com base no ano de publicação e preço do livro
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

#streamlit consegue criar 2 colunas com esse comando
col1, col2 =st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
