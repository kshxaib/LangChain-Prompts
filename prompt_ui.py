from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI()

st.header("Research Tool")

# User selects the research paper
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# User selects the explanation style
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# User selects the explanation length
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


# PromptTemplate = reusable template for creating dynamic prompts
# {paper_input}, {style_input}, {length_input} are dynamic variables
template = PromptTemplate(
   template="""
      Please summarize the research paper titled "{paper_input}" with the following specifications:
         Explanation Style: {style_input}  
         Explanation Length: {length_input}  
      1. Mathematical Details:  
            - Include relevant mathematical equations if present in the paper.  
            - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
      2. Analogies:  
            - Use relatable analogies to simplify complex ideas.  
      If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
      Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,

   # Variables that will be replaced with actual user input
   input_variables=['paper_input', 'style_input','length_input'],

   # Validates that template variables match input_variables
   validate_template=True
)


# invoke() fills the PromptTemplate variables with actual values
# Creates the final dynamic prompt
prompt = template.invoke({
   'paper_input': paper_input,
   'style_input':style_input,
   'length_input':length_input
})


if st.button("Explain"):
   response = model.invoke(prompt)  # Send the generated prompt to the Chat Model
   st.write(response.content)