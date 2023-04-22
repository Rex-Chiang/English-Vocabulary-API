import json
import asyncio
import aiohttp

def request_vocabulary_api(session, vocabulary_data):
    url = "https://english-vocabulary-api.fly.dev/api/vocabulary/"
    return session.post(url, json=vocabulary_data)

async def upload_vocabularies():
    async with aiohttp.ClientSession() as session:
        tasks = []

        with open("vocabularies") as file:
            for vocabulary_data in file.read().splitlines():
                tasks.append(request_vocabulary_api(session, json.loads(vocabulary_data)))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(upload_vocabularies())