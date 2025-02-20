import openai
import os

# Load OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key:
    print("✅ OpenAI API Key is set up successfully!")
else:
    print("❌ Error: OpenAI API Key is not set. Please check your environment variables.")
