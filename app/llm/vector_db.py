import numpy as np
import logging
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from typing import List, Dict, Any

# Set up logging
logger = logging.getLogger(__name__)

class VectorDB:
    def __init__(self, client: QdrantClient, collection_name: str, conversations: List[Dict[str, Any]]):
        logger.info(f"Initializing VectorDB with collection: {collection_name}")
        logger.info(f"Processing {len(conversations)} conversations")
        
        self.client = client
        self.collection_name = collection_name
        self.conversations = conversations
        self.embedding_dim = len(conversations[0]['embedding']) if conversations else 0
        
        logger.info(f"Embedding dimension: {self.embedding_dim}")
        
        self._create_collection()
        self._insert_vectors()
        
        logger.info("VectorDB initialization completed")

    def _create_collection(self):
        logger.info(f"Creating collection: {self.collection_name}")
        
        try:
            self.client.get_collection(self.collection_name)
            logger.info("Collection already exists")
        except:
            logger.info("Collection doesn't exist, creating new one...")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=self.embedding_dim, distance=Distance.COSINE)
            )
            logger.info("Collection created successfully")

    def _insert_vectors(self):
        logger.info(f"Inserting {len(self.conversations)} vectors into collection")
        
        points = []
        for i, conv in enumerate(self.conversations):
            point = PointStruct(
                id=conv['id'],
                vector=conv['embedding'].tolist(),
                payload={
                    "conversation_id": conv['id'],
                    "conversation_text": conv['text'][:500],
                    "source": "conversation_data"
                }
            )
            points.append(point)
            
            if i % 50 == 0:  # Log progress every 50 points
                logger.info(f"Prepared {i+1}/{len(self.conversations)} points")
        
        logger.info("Upserting points to Qdrant...")
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        logger.info("Vector insertion completed successfully")

    def search_vectors(self, query_vector: np.ndarray, top_k: int = 5):
        logger.info(f"Searching for {top_k} similar vectors")
        logger.info(f"Query vector shape: {query_vector.shape}")

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector.tolist(),
            limit=top_k,
            with_payload=True
        )
        
        logger.info(f"Found {len(results.points)} results")
        return results.points