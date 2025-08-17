from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# # Access the variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=gemini_api_key)


# # Initialize Gemini model
# model_gemini = genai.GenerativeModel("gemini-1.5-flash")
# response = model_gemini.generate_content("Explain how AI works")
# print(response.text)

# using langchain_google_genai
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=gemini_api_key)
result = model.invoke('What is the capital of India')

print(result.content)