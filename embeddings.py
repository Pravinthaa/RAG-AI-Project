import openai
import faiss
import numpy as np
import pandas as pd
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_embedding(text):

    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return np.array(response['data'][0]['embedding'])

def generate_embeddings(df):
    
    df["embedding"] = df["tip"].apply(get_embedding)
    

    embeddings = np.vstack(df["embedding"].to_list())
    

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
 
    faiss.write_index(index, "../data/travel_tips.index")
    df.to_pickle("../data/travel_tips.pkl")

if __name__ == "__main__":
    df = pd.read_csv("../data/travel_tips.csv")
    generate_embeddings(df)
    print("Embeddings generated and stored in FAISS!")
