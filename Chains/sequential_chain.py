from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

# # Access the variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

#gpt_model = ChatOpenAI()

gemini_model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=gemini_api_key)

parser = StrOutputParser()

chain = prompt1 | gemini_model | parser | prompt2 | gemini_model | parser

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

chain.get_graph().print_ascii()