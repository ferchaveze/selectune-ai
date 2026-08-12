import asyncio

from qdrant_client import AsyncQdrantClient

from app.rag.repository import MusicRepository


async def main() -> None:
    client = AsyncQdrantClient(
        url="http://localhost:6333"
    )

    repository = MusicRepository(client)

    await repository.create_collection()

    collections = await client.get_collections()

    print("Collections:")
    for collection in collections.collections:
        print(f"- {collection.name}")

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())