import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI as Google
import os
from langchain import PromptTemplate, LLMChain

st.set_page_config(page_title='Tweet Generator', page_icon='🐣💀🤫', layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Tweet Generator")

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
model = Google(model = "gemini-1.5-flash-latest")

tweet_template = """
Give me {language} in {number} about {topic}
Please follow the below instructions:
The main game is roblox the game are games inside of roblox
give answer to the question{language} 

"""
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic', 'language'])

with st.form(key = 'tweets'):
    topic = st.text_input("Game(in roblox): ")
    number = st.number_input("Number of results: ", value = 1, step = 1, max_value = 10, min_value = 1)
    language = st.text_input("Question: ")
    submit = st.form_submit_button("Generate")

if submit:
    tweet_chain = tweet_prompt | model
    response = tweet_chain.invoke({"number": number,
                                   "topic": topic,
                                   "language": language,})
    st.write(response.content)
