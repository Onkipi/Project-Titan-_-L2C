from app.rag.vector_store import search_vectors
from app.rag.keyword_search import keyword_search
from app.graph.neo4j_client import run_query
from app.rag.websearch import web_search

def hybrid_retrieve(query, query_vector):
    semantic_results = search_vectors(query_vector)
    keyword_results = keyword_search(query)

    graph_results = run_query(
        "MATCH (c:Customer)-[:PLACED]->(o:Order) RETURN c,o LIMIT 5"
    )

    web_results = web_search(query)

    return {
        "semantic": semantic_results,
        "keyword": keyword_results,
        "graph": list(graph_results),
        "web": web_results
    }
