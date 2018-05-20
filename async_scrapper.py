import time
import asyncio
import aiohttp


URLS = [
    'https://en.wikipedia.org/wiki/China',
    'https://en.wikipedia.org/wiki/India',
    'https://en.wikipedia.org/wiki/Indonesia',
    'https://en.wikipedia.org/wiki/Pakistan',
    'https://en.wikipedia.org/wiki/Bangladesh',
    'https://en.wikipedia.org/wiki/Russia',
    'https://en.wikipedia.org/wiki/Japan',
    'https://en.wikipedia.org/wiki/Philippines',
    'https://en.wikipedia.org/wiki/Vietnam',
    'https://en.wikipedia.org/wiki/Iran',
    'https://en.wikipedia.org/wiki/Turkey',
    'https://en.wikipedia.org/wiki/Thailand',
    'https://en.wikipedia.org/wiki/Myanmar',
    'https://en.wikipedia.org/wiki/South_Korea',
    'https://en.wikipedia.org/wiki/Iraq',
]
WORD = 'the'


async def get_url_text(session: aiohttp.ClientSession, url: str):
    response = await session.get(url)
    text = await response.text()
    print(f'Got response from {url}')
    return text


async def main():
    session =  aiohttp.ClientSession()
    tasks = [(get_url_text(session, url)) for url in URLS]
    responses = await asyncio.gather(*tasks)
    await session.close()

    for response, url in zip(responses, URLS):
        word_count = response.count(WORD)
        print(f'URL {url} has word "{WORD}" {word_count} times')

    return responses

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    t0 = time.time()
    loop.run_until_complete(main())
    t1 = time.time()
    loop.close()

    print(f'Time spent: {t1-t0:.2f}')
