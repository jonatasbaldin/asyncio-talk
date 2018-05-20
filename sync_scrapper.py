import time
import requests


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


def get_url_text(url: str):
    response = requests.get(url)
    print(f'Got response from {url}')
    return response.text


def main():
    for url in URLS:
        text = get_url_text(url)
        word_count = text.count(WORD)
        print(f'URL {url} has word "{WORD}" {word_count} times')


if __name__ == '__main__':
    t0 = time.time()
    main()
    t1 = time.time()

    print(f'Time spent: {t1-t0:.2f}')
