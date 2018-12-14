# python-logging-impact
Demonstration of how python logging can unexpectdly impact your code performance

**Python logging statements are executed regardless of logging level**

It turns out that code in a `logging.debug()` call is executed regardless of
what level logging is set at. If you run the script in this repo without
options, "I was executed" is still printed. Compare:
`logging_impacts_me.py`
vs
`logging_impacts_me.py -d`

This can have a huge performance impact on your code. I discovered this issue while
implementing an object based double linked list to solve
[Advent of Code 2018 day 9 problem](https://adventofcode.com/2018/day/9). 
I originally had an `__str__` method which allowed to print a helpful
representation of each object in the list while debugging, calling the str() functions which
made my solution too slow to solve part 2 of the problem in a reasonable amount of time.



