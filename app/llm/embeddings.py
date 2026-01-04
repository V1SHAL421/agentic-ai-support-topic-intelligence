import pandas as pd
import logging
from fastembed import TextEmbedding
from typing import List, Dict, Any
import numpy as np

from app.constants import KNOWLEDGE_BASE_PATH

# Set up logging
logger = logging.getLogger(__name__)

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

def parse_knowledge_base() -> List[Dict[str, Any]]:
    logger.info("Starting knowledge base parsing...")
    logger.info(f"Reading CSV file: app/data/conversations.csv")
    
    conversations_df = pd.read_csv(KNOWLEDGE_BASE_PATH, dtype={
        'conversation_id': 'int64', 
        'conversation': 'string'
    })
    
    logger.info(f"Loaded {len(conversations_df)} conversations from CSV")
    
    conversations = [
        {
            'id': int(row['conversation_id']),
            'text': row['conversation'],
            'embedding': None
        }
        for _, row in conversations_df.iterrows()
    ]
    
    logger.info(f"Parsed {len(conversations)} conversation records")
    return conversations

def convert_conversations_to_embeddings(conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    logger.info(f"Starting embedding conversion for {len(conversations)} conversations...")
    logger.info(f"Using embedding model: {EMBEDDING_MODEL}")
    
    logger.info("Initializing text embedder...")
    text_embedder = TextEmbedding(EMBEDDING_MODEL)
    logger.info("Text embedder initialized")
    
    logger.info("Extracting conversation texts...")
    texts = [conv['text'] for conv in conversations]
    logger.info(f"Extracted {len(texts)} texts for embedding")
    
    logger.info("Generating embeddings (this may take a while)...")
    embeddings = list(text_embedder.embed(documents=texts))
    logger.info(f"Generated {len(embeddings)} embeddings")
    
    logger.info("Adding embeddings to conversation data...")
    for i, conv in enumerate(conversations):
        conv['embedding'] = np.array(embeddings[i])
        if i % 10 == 0:  # Log progress every 10 conversations
            logger.info(f"Processed {i+1}/{len(conversations)} conversations")
    
    logger.info("Embedding conversion completed successfully")
    return conversations

def convert_conversation_to_embedding(conversation: str) -> np.ndarray:
    logger.info(f"Converting single conversation to embedding (length: {len(conversation)} chars)")
    logger.info(f"Using embedding model: {EMBEDDING_MODEL}")
    
    logger.info("Initializing text embedder...")
    text_embedder = TextEmbedding(EMBEDDING_MODEL)
    
    logger.info("Generating embedding...")
    embedding = next(iter(text_embedder.embed(documents=[conversation])))
    result = np.array(embedding)
    
    logger.info(f"Generated embedding with shape: {result.shape}")
    return result