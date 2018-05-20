# asyncio-talk

*await a minute, let me async that for you*

This is a talk about Python Asyncio, presented at the Mumbai Tech Meetup. The presentation was made with [Slydes](https://github.com/jonatasbaldin/slydes). 

### Running the Talk
Install the dependencies:
```bash
pipenv install
```

Run the talk in a Python Interpreter:
```python
from talk import talk

talk.next()
...
```

### Examples
To run the examples, just type `pipenv run python <file>`

* `sync_example.py` and `async_example.py`: Really simple demonstration of the asyncio lib.
* `sync_scrapper.py` and `async_scrapper.py`: Counting the word `the` in 15 Wikipedia sites.
