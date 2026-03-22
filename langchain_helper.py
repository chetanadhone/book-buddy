import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()
# Added the API key in streamlit > settings > secrets
api_key = os.getenv("GROQ_API_KEY") or st.secrets("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key
)


def generate_book_names_and_description(mood):
    # Chain 1: Personality generator based on mood
    prompt_temp_personality = PromptTemplate.from_template(
        'I am in a {mood} mood. Describe the following in 2 lines:'
        'book personality'
        'book mindset'
        'emotional needs in terms of books'
    )

    personality_chain = prompt_temp_personality | llm
    personality = personality_chain.invoke({"mood": mood}).content.strip()

    # Chain 2: Book recommendation based on Personality
    prompt_temp_bookName = PromptTemplate.from_template(
        'Based on {personality}, suggest only one book for me to read'
        'Give its summary in 3 lines only'
        'Describe in 3 pointers why it is a best pick for me'
    )

    bookName_chain = prompt_temp_bookName | llm
    bookName = bookName_chain.invoke({'personality': personality}).content.strip()

    return {
        'personality': personality,
        'bookName': bookName
    }


if __name__ == "__main__":
    print(generate_book_names_and_description('Sad'))