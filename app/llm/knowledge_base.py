import logging
from qdrant_client import QdrantClient
from app.llm.embeddings import convert_conversation_to_embedding, convert_conversations_to_embeddings, parse_knowledge_base
from app.llm.vector_db import VectorDB

# Set up logging
logger = logging.getLogger(__name__)

def retrieve_knowledge(query: str) -> str:
    logger.info(f"Starting knowledge retrieval for query: {query[:100]}...")
    
    logger.info("Parsing knowledge base...")
    conversations = parse_knowledge_base()
    logger.info(f"Parsed {len(conversations)} conversations from knowledge base")
    
    logger.info("Converting conversations to embeddings...")
    conversations_with_embeddings = convert_conversations_to_embeddings(conversations)
    logger.info("Conversations converted to embeddings successfully")
    
    logger.info("Initializing vector database...")
    vector_db = VectorDB(
        client=QdrantClient(":memory:"), 
        collection_name="conversations", 
        conversations=conversations_with_embeddings
    )
    logger.info("Vector database initialized")
    
    logger.info("Converting query to embedding...")
    query_embedding = convert_conversation_to_embedding(query)
    logger.info("Query embedding generated")
    
    logger.info("Searching for similar conversations...")
    results = vector_db.search_vectors(query_vector=query_embedding)
    logger.info(f"Found {len(results)} similar conversations")
    
    if results and len(results) > 0 and results[0].payload:
        result_text = results[0].payload.get('conversation_text', 'No conversation text found')
        logger.info(f"Returning top result: {len(result_text)} characters")
        return result_text
    
    logger.warning("No relevant knowledge found")
    return "No relevant knowledge found."