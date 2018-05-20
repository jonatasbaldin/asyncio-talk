from slydes import Presentation, Template


talk = Presentation()
template = Template()


@talk.add_slide
def introduction():
    title = 'await a minute, let me async that for you'
    text = '''
    $ whoami
    Jonatas Baldin
    traveller, developer, blogger and vlogger wanna be
    [future] works @ Stack Builders

    $ find
    Twitter: @jonatasbaldin
    GitHub: @jonatasbaldin
    Instagram: @jonatasbaldin
    [insert_media_here]: @jonatasbaldin
    '''

    return template.default(title, text) 


@talk.add_slide
def why_am_i_here():
    title = 'why am I here?'
    text = '''
    > Got a remote job to start travelling
    > Came to Sri Lanka for a company trip
    > Made a tweet asking around about Python communities in Asia
    > Augustine got in touch (thanks mate!)
    > I'm here!
    '''

    return template.default(title, text)


@talk.add_slide
def simple_sync_example():
    title = 'here\'s a sync example'
    text = '''
    > Let's start with the sync planet

    > What happens with a task that lasts for some seconds?
    '''
    return template.default(title, text)


@talk.add_slide
def simple_sync_code():
    title = 'here\'s a sync example'
    text = '''
    import time


    def task_one():
        print('> Starting task_one')
        time.sleep(2)
        print('> Finish task_one')


    def task_two():
        print('> Starting task_two')
        time.sleep(2)
        print('> Finish task_two')


    def main():
        task_one()
        task_two()


    if __name__ == '__main__':
        main()
    '''
    return template.default(title, text)


@talk.add_slide
def the_synchronous_planet():
    title = 'the synchronous Python planet'
    text = '''
    > The Python's default mode
    > Runs a single thread in a single process
    > Everything runs line by line
    > The Global Interpreter Lock – GIL
    '''

    return template.default(title, text)


@talk.add_slide
def the_multiprocess_planet():
    title = 'the multiprocess Python planet'
    text = '''
    > It's actually parallelism
    > Multiple processes, one GIL per process
    > Go that route for CPU Bound applications

    > Not our topic today, but lot's of information on the Internet!
    '''

    return template.default(title, text)


@talk.add_slide
def the_thread_planet():
    title = 'the thread Python planet and the callback moon'
    text = '''
    > In this new planet, things kinda work at the same time
    > (but not really, damm you GIL!)

    > All about splitting the work in multiple threads
    > using a single process

    > Thread issues:
        - CPU Context Switching
        - Race Conditions
        - Dead Locks
        - Resource Starvation

    > Green Threads (Gevent)
    > Callbacks (Tornardo)

    > Use it if you have IO Bound problems (network, files etc)
    '''

    return template.default(title, text)


@talk.add_slide
def the_asynchronous_planet():
    title = 'the asynchronous Python planet'
    text = '''
    > Let's `finally` talk about asyncio

    > Originally an external library
    > Oficially standard library in Python 3.4
    > Async/await keywords introduced in Python 3.5

    > "Cooperative Concurrent Programming"

    > Used for IO Bound problems (network, files etc)
    > Single thread in a single process
    > No more CPU Context Switching
    > No more threads (and all their difficulties)
    > It's pretty ;)
    '''

    return template.default(title, text)


@talk.add_slide
def the_asynchronous_planet_how():
    title = 'the asynchronous Python planet'
    text = '''
    > What you really need know:
        - async/await syntax
        - Coroutines
        - Event loop
        - Blocking/Non Blocking calls

    > How could we improve the slow task from before?
    '''

    return template.default(title, text)


@talk.add_slide
def simple_async_code():
    title = 'the asynchronous Python planet'
    text = '''
    import asyncio
    import time


    async def task_one():
        print('> Starting task_one')
        asyncio.sleep(2)
        print('> Finish task_one')


    async def task_two():
        print('> Starting task_two')
        asyncio.sleep(2)
        print('> Finish task_two')


    async def main():
        await task_one()
        await task_two()


    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
    '''

    return template.default(title, text)


@talk.add_slide
def the_scrapper_example():
    title = 'the scrapper example'
    text = '''
    > Let's try a scrapper, sync and async
    '''

    return template.default(title, text)


@talk.add_slide
def the_asynchronous_planet_where():
    title = 'the asynchronous Python planet'
    text = '''
    > Where should you use it?
        - ✓ I/O Bound applications
        - ✓ Concurrent tasks

    > Where not to use it?
        - ✖ CPU Bound applications
        - ✖ CLI and user scripts
        - ✖ New devs
    '''

    return template.default(title, text)


@talk.add_slide
def caveats():
    title = 'caveats (or things that maybe bite you)'
    text = '''
    > Try to go FULL async

    > ✓ sync calling sync
    > ✖ sync calling async
    > ✖✖✖ async calling sync
    > ❤ async calling async

    > There's A LOT under the hood
        - event loops
        - event loop policies
        - awaitables
        - coroutine functions
        - old style coroutine functions
        - coroutines
        - coroutine wrappers
        - generators
        - futures
        - concurrent futures
        - tasks
        - handles
        - executors
        - transports
        - protocols
    '''

    return template.default(title, text)


@talk.add_slide
def libs_resources():
    title = 'nice libs to play with'
    text = '''
    > aiohttp - web client/server
    > sanic - async Flask
    > aiomqp - async queues
    > asyncpg - async PostgreSQL
    > peewee-async - async ORM
    > pytest-asyionc - because you need tests
    > curio/uvloop/trio - another asyncio approaches
    '''
    return template.default(title, text)


@talk.add_slide
def final_thoughts():
    title = 'final shower thoughts'
    text = '''
    > If yo go async, go all the way
    > Play around, feel it
    > The lib you need may still be just sync, take care
    > It's kinda new in the beginning, it will improve a lot
    
    > But it's stable and production ready, so go!
    '''

    return template.default(title, text)


@talk.add_slide
def thanks():
    title = 'thanks so much Mumbai!'
    text = '''

    > Presentation made with Slydes
    > https://github.com/jonatasbaldin/slydes

    > Find me on social media
    Twitter: @jonatasbaldin
    GitHub: @jonatasbaldin
    Instagram: @jonatasbaldin
    [insert_media_here]: @jonatasbaldin

    Questions?
    '''
    return template.default(title, text)
