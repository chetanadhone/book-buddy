import streamlit as st
import langchain_helper

st.title("📚 Book Buddy")
mood = st.sidebar.selectbox("Pick a Mood", ("Happy", "Bored", "Sad", "Fun", "Confused", "Angry", "Lazy", "Energetic", "Reflective"))

if st.button('Begin'):
    response = langchain_helper.generate_book_names_and_description(mood)
    st.header(response['book_name'])
    st.subheader(response['book_description'])
