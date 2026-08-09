from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input('User Input: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    print("AI: " + response.content)