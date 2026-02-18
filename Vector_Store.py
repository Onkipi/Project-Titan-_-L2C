import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

def add_vectors(vectors):
    index.add(np.array(vectors).astype("float32"))

def search_vectors(query_vector, k=5):
    D, I = index.search(np.array([query_vector]).astype("float32"), k)
    return I
