from neo4j import GraphDatabase
from app.core.config import settings

driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
)

def run_query(query, params=None):
    with driver.session() as session:
        return session.run(query, params)
