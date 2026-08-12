import asyncio

from openai import AsyncOpenAI

from app.config.settings import settings
from app.rag.embeddings import EmbeddingService


async def main() -> None:
    client = AsyncOpenAI(api_key=settings.openai_api_key)

    embedding_service = EmbeddingService(client)

    vector = await embedding_service.embed(
        "dark hypnotic post-punk with driving bass"
    )

    print(f"Vector dimensions: {len(vector)}")
    print(f"First 10 values: {vector[:10]}")


if __name__ == "__main__":
    asyncio.run(main())