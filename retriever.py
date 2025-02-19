import faiss
import numpy as np
import pandas as pd
from embeddings import get_embedding

class TravelTipsRetriever:
    def __init__(self):
        self.df = pd.read_pickle("../data/travel_tips.pkl")
        self.index = faiss.read_index("../data/travel_tips.index")

    def retrieve(self, query, top_k=3):
        query_embedding = get_embedding(query).reshape(1, -1)
        distances, indices = self.index.search(query_embedding, top_k)
        results = self.df.iloc[indices[0]]
        return results[["destination", "category", "tip"]].to_dict(orient='records')


if __name__ == "__main__":
    retriever = TravelTipsRetriever()
    query = "Best food places in Paris"
    print(retriever.retrieve(query))

