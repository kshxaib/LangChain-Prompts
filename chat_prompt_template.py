from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

model = ChatOpenAI()

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic} in 2 lines.')
])

prompt = chat_template.invoke({'domain': 'AI', 'topic': 'Machine Learning'})

response = model.invoke(prompt)

print(response.content)