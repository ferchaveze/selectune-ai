from openai import AsyncOpenAI


class EmbeddingService:
    def __init__(self, client: AsyncOpenAI):
        self.client = client

    async def embed(self, text: str) -> list[float]:
        response = await self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )

        return response.data[0].embedding