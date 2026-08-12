import asyncio

from openai import AsyncOpenAI
from qdrant_client import AsyncQdrantClient

from app.config.settings import settings
from app.rag.documents import MUSIC_DOCUMENTS
from app.rag.embeddings import EmbeddingService
from app.rag.repository import MusicRepository


async def main() -> None:
    openai_client = AsyncOpenAI(
        api_key=settings.openai_api_key
    )

    qdrant_client = AsyncQdrantClient(
        url="http://localhost:6333"
    )

    embedding_service = EmbeddingService(openai_client)
    repository = MusicRepository(qdrant_client)

    await repository.create_collection()

    for document in MUSIC_DOCUMENTS:
        text = (
            f"{document.artist} - {document.title}. "
            f"Genres: {', '.join(document.genre)}. "
            f"Moods: {', '.join(document.mood)}. "
            f"{document.description}"
        )

        vector = await embedding_service.embed(text)

        payload = {
            "artist": document.artist,
            "title": document.title,
            "genre": document.genre,
            "mood": document.mood,
            "description": document.description,
        }

        await repository.upsert(
            document_id=document.id,
            vector=vector,
            payload=payload,
        )

        print(f"Indexed: {document.artist} - {document.title}")

    await openai_client.close()
    await qdrant_client.close()


if __name__ == "__main__":
    asyncio.run(main())