from langchain_openai import ChatOpenAI, OpenAI
from typing import TypedDict, Optional, Annotated
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model ='gpt-4o')

class Review(TypedDict): 
    summary: Annotated[str, "A brief introduction of the review"]
    
    sentiment: Annotated[str, "Return sentiment of the review - either positive, negative or nuetral"]

structured_model = llm.with_structured_output(Review)

result = structured_model.invoke("The model is great, but feel bloated")
print(result)
