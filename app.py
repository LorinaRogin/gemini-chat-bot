import streamlit as st
import google.generativeai as genai


st.title("welcome to my app")

genai.configure(api_key="AIzaSyD570VEOlHQB2Veu040gEj9BVUbu_iYXVg")

text = st.text_input("ask something:")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)