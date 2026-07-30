import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="Bhumi's AI FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 Bhumi's AI FAQ Chatbot")

st.write("Ask me anything related to Artificial Intelligence.")

user_question = st.text_input("Enter your question:")

if st.button("Ask"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:
        answer = get_answer(user_question)

        st.success(answer)