import streamlit as st
import pandas as pd

# preenche a tela toda 
st.set_page_config(layout="wide")

#leitor de csv do pandas
df_reviews = pd.read_csv("C:/Users/MaiconZ/Documents/Pitóun/datasets/customer reviews.csv")
df_top100_books = pd.read_csv("C:/Users/MaiconZ/Documents/Pitóun/datasets/Top-100 Trending Books.csv")

#unique pega o livro e exibe uma única vez
books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("books", books)

#filtro
df_book = df_top100_books[df_top100_books["book title"] == book] 
df_reviews_filter = df_reviews[df_reviews["book name"] == book] 

# o pandas puxa mais de uma informação na tabela,
# um título tem mais de uma alocação
# o iloc puxa somente a posição desejada, se 0 é 
# somente a primeira
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

#cria titulo grande
st.title(book_title)
st.subheader(book_genre)

#cria colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### :green[Price]")
    st.markdown(f"## {book_price}")
with col2:
    st.markdown("### :rainbow[Rating]")
    st.markdown(f"## ⭐ {book_rating}")
with col3:
    st.markdown("### :blue[Year]")
    st.markdown(f"## 📅 {book_year}")

#linha divisora
st.divider()

#for para percorrer apenas a coluna review
for row in df_reviews_filter.values:
    #caht _message exibe um balãozinho de rating antes do comentário
    message = st.chat_message(f"{row[4]}")
    # o ** coloca em negrito
    message.write(f"**{row[2]}**")
    message.write(row[5]) 