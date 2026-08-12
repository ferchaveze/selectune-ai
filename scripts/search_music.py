import asyncio

from openai import AsyncOpenAI
from qdrant_client import AsyncQdrantClient

from app.config.settings import settings
from app.rag.embeddings import EmbeddingService
from app.rag.repository import COLLECTION_NAME


async def main() -> None:
    query = "eerie ritualistic music for a dark nightclub"

    openai_client = AsyncOpenAI(
        api_key=settings.openai_api_key
    )

    qdrant_client = AsyncQdrantClient(
        url="http://localhost:6333"
    )

    embedding_service = EmbeddingService(openai_client)

    query_vector = await embedding_service.embed(query)

    results = await qdrant_client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=5,
        with_payload=True,
    )

    print(f'\nQuery: "{query}"\n')
    print("Results:")

    for index, result in enumerate(results.points, start=1):
        payload = result.payload

        print(
            f"{index}. "
            f"{payload['artist']} - {payload['title']} "
            f"(score={result.score:.4f})"
        )

    await openai_client.close()
    await qdrant_client.close()


if __name__ == "__main__":
    asyncio.run(main())