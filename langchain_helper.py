import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("GROQ_API_KEY") or st.secrets("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key
)


#hard-coded to check the working
# def generate_book_names_and_description(mood):
#     return{
#         'book_name': 'book1',
#         'book_description': 'abcdefghijklmno',
#         'book_genres': 'abc, def, ghi'
#     }


def generate_book_names_and_description(mood):
    # Chain 1: Book name
    prompt_temp_name = PromptTemplate.from_template(
        'Suggest me an engaging book for a {mood} mood.'
    )

    name_chain = prompt_temp_name | llm
    name_response = name_chain.invoke({"mood": mood})
    book_name = name_response.content.strip()

    # Chain 2: Book description
    prompt_temp_description = PromptTemplate.from_template(
        'Provide a brief summary of the book {book_name}. Include a point why one should pick this book'
    )

    description_chain = prompt_temp_description | llm
    description_response = description_chain.invoke({'book_name': book_name})
    book_description = description_response.content.strip()

    return {
        'book_name': book_name,
        'book_description': book_description
    }


if __name__ == "__main__":
    print(generate_book_names_and_description('Sad'))