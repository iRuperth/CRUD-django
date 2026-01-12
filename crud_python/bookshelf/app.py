import streamlit as st
import requests

st.sidebar.title('Menu')
st.sidebar.write('Welcome to my library')

st.title('Welcome to my library')
st.write('These are my books from my API:')

response = requests.get('http://127.0.0.1:8000/api/libros')
if response.status_code == 200:
    books = response.json()
    for book in books:
        st.write(f"Title: {book['title']}")
        if st.button(f"Show details {book['id']}"):
            st.write(book)
        if st.button(f"Delete book {book['id']}"):
            delete_response = requests.delete(f"http://127.0.0.1:8000/api/libros/{book['id']}")
            if delete_response.status_code == 204:
                st.write(f"Book {book['id']} deleted")
            else:
                st.write(f"Could not delete book {book['id']}")
else:
    st.write('No books found')