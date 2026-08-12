import asyncio

from qdrant_client import AsyncQdrantClient


async def main() -> None:
    client = AsyncQdrantClient(
        url="http://localhost:6333"
    )

    collections = await client.get_collections()

    print("Qdrant connection: OK")
    print(f"Collections: {collections.collections}")

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())