from qdrant_client import AsyncQdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


COLLECTION_NAME = "music"
VECTOR_SIZE = 1536


class MusicRepository:
    def __init__(self, client: AsyncQdrantClient):
        self.client = client

    async def create_collection(self) -> None:
        collections = await self.client.get_collections()

        exists = any(
            collection.name == COLLECTION_NAME
            for collection in collections.collections
        )

        if not exists:
            await self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,
                    distance=Distance.COSINE,
                ),
            )

    async def upsert(
        self,
        document_id: str,
        vector: list[float],
        payload: dict,
    ) -> None:
        await self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=document_id,
                    vector=vector,
                    payload=payload,
                )
            ],
        )