import streamlit as st
import langchain_helper

st.set_page_config(page_title="Book Buddy", layout='wide')

st.title("📚 Your Book Buddy is right here!")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Find a book based on your mood ✨")
    mood = st.selectbox("Pick your current mood",
                        ("Happy", "Bored", "Sad", "Fun", "Confused", "Angry", "Lazy", "Energetic", "Reflective")
                        )

with col2:
    st.write("")  # spacing
    st.write("")  # spacing
    st.write("")  # spacing
    st.write("")  # spacing
    st.write("")  # spacing
    generate = st.button("Get Recommendation 🚀")

if generate:
    with st.spinner("Finding the perfect book for you... 📖"):
        response = langchain_helper.generate_book_names_and_description(mood)

    st.success("Here’s something you might love ❤")

    st.subheader("📖 Your Recommendation")

    st.markdown(f"""
        <div style="
            padding: 20px;
            border-radius: 20px;
            background-color: #CF869A;
            margin-top: 20px;
        ">
            <p style="font-size:14px;">
                {response['personality']}
            </p>
            <hr style="border: 1px solid #444; margin: 10px 0;">
            <p style="font-size:18px;">
                {response['bookName']}
            </p>
        </div>
    """, unsafe_allow_html=True)

# if st.button('Begin'):
#     response = langchain_helper.generate_book_names_and_description(mood)
#     st.header(response['book_name'])
#     st.subheader(response['book_description'])
