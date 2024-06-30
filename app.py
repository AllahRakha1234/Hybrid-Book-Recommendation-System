import streamlit as st
import numpy as np
from data_upload import model, collab_pivot, books_names_list, req_updated_books, content_similarity

st.header('Book Recommender System')

selected_book = st.selectbox('Select a book:', books_names_list)

def get_collaborative_based_recommendations(selected_book, top_n):
    book_id = req_updated_books[req_updated_books['title'] == selected_book].index[0]
    distance, suggestion = model.kneighbors(collab_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors= top_n )
    collab_books_isbn = collab_pivot.index[suggestion[0]]  
    return collab_books_isbn

def get_content_based_recommendations(title, top_n):
    index = req_updated_books[req_updated_books['title'] == title].index[0]
    similarity_scores = content_similarity[index]
    similar_indices = similarity_scores.argsort()[::-1][1:top_n + 1]
    content_books_isbn = req_updated_books.loc[similar_indices, 'isbn'].values
    return content_books_isbn

def hybrid_recommendations(selected_book, top_n):
    collab_books_isbn = get_collaborative_based_recommendations(selected_book, top_n)
    content_books_isbn = get_content_based_recommendations(selected_book, top_n)
    
    collab_books_isbn = [isbn.replace("'", "") for isbn in collab_books_isbn]
    content_books_isbn = [isbn.replace("'", "") for isbn in content_books_isbn]
    books_isbn = list(set(collab_books_isbn) | set(content_books_isbn))
    
    books_isbn = books_isbn[:top_n]
    books = req_updated_books[req_updated_books['isbn'].isin(books_isbn)]
    books_titles = books['title'].tolist()
    books_url = books['coverImg'].tolist()
    books_genres = books['genres'].tolist()
    books_rating = books['rating'].tolist()
    
    return books_titles, books_url, books_genres, books_rating

# Add custom CSS
st.markdown(
    """
    <style>
    .book-container {
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .book-image {
        flex-grow: 1;
    }
    .book-genres {
        margin-top: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

if st.button('Show Recommendation'):
    recommended_books, books_url, books_genres, books_rating = hybrid_recommendations(selected_book, 6)
    cols = st.columns(5)

    for i in range(1, 6):
        with cols[i-1]:
            st.text(recommended_books[i])
            st.markdown(f'<div class="book-container"><img src="{books_url[i]}" class="book-image" width="120"><div class="book-genres">{", ".join(books_genres[i])}</div></div>', unsafe_allow_html=True)


print("Done")
