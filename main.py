from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
import os

load_dotenv()

##   ------------------------ Uncomment for Hugging Face API ----------------------- 
# api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN") 
# llm = HuggingFaceEndpoint(
#     repo_id='microsoft/Phi-3-mini-4k-instruct',
#     task="text-generation",
#     api_key=api_key)
# model = ChatHuggingFace(llm=llm)

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model ='gpt-4o')

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name", 
    ["Attention Is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", 
     "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | llm
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)
