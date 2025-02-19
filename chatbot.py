import openai
from retriever import TravelTipsRetriever
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(query):
  
    retriever = TravelTipsRetriever()
    retrieved_tips = retriever.retrieve(query)

    if not retrieved_tips:
        return "Sorry, I couldn't find any travel tips for that destination."

    
    context = "\n".join([f"{tip['destination']} ({tip['category']}): {tip['tip']}" for tip in retrieved_tips])

   
    prompt = f"Here are some travel tips:\n{context}\n\nBased on this information, summarize useful travel tips for: {query}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    query = input("Ask a travel question: ")
    print(generate_response(query))
