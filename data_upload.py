import pickle
import streamlit as st
import numpy as np


model = pickle.load(open('artifacts3/model.pkl', 'rb'))
# collab_data = pickle.load(open('artifacts3/collab_data.pkl', 'rb'))
collab_pivot = pickle.load(open('artifacts3/collab_pivot.pkl', 'rb'))
# req_content_data = pickle.load(open('artifacts3/req_content_data.pkl', 'rb'))
books_names_list = pickle.load(open('artifacts3/books_names_list.pkl', 'rb'))
req_updated_books = pickle.load(open('artifacts3/req_updated_books.pkl', 'rb'))
content_similarity = pickle.load(open('artifacts3/content_similarity.pkl', 'rb'))

print("Begin")