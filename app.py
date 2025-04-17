import streamlit as st
import pandas as pd
from langchain_ollama import ChatOllama

st.title('Chatbot using LLM and Ollama')
st.write('Chat bot reolution')

with st.form('llm form'):
    text=st.text_area('Enter your question')
    submit = st.form_submit_button('Submit')

def get_response(input_text):
    model = ChatOllama(model='llama3.2')
    response= model.invoke(input_text)
    return response.content

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']= []

if submit and text:
    with st.spinner('Generating Response.....'):
        response= get_response(text)
        st.session_state['chat_history'].append({'user':text, 'ollama':response})
        st.write(response)

st.write('Chat History')
for chat in st.session_state['chat_history']:
    st.write(f'👤 User: {chat['user']}')
    st.write(f'🤖 AI Assistant : {chat['ollama']}')
    st.write('----')