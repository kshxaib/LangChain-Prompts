from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain and LangGraph in simple and short")
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)