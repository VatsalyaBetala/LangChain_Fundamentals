from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model = 'gpt-4o', api_key=api_key)

chat_history = []

while True: 
    message = input("You: ")
    chat_history.append(HumanMessage(content=message))
    if message == 'exit': 
        break
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f'AI: {result.content}')
