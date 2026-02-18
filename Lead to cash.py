from app.rag.hybrid_retriever import hybrid_retrieve

def l2c_decision_engine(query, embedding):
    results = hybrid_retrieve(query, embedding)
    return {"decision_context": results}
