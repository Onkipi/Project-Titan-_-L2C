from rank_bm25 import BM25Okapi

documents = ["contract policy", "pricing strategy", "EU compliance"]

bm25 = BM25Okapi([doc.split() for doc in documents])

def keyword_search(query):
    scores = bm25.get_scores(query.split())
    return scores
