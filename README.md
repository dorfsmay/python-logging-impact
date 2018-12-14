# python-logging-impact
Demonstration of how python logging can unexpectdly impact your code performance

*Python logging statements are executed regardless of logging level*

It turns out that code in a `logging.debug()` call is executed regardless of
what level logging is set out. If you run the script in this repo without
options, "I was executed" is still printed.

This can have a huge performance impact on your code. I discovered this issue while
implementing an object based double linked list to solve
[Advent of Code 2018 day 9 problem](https://adventofcode.com/2018/day/9). 
I originally had a `__str__` method which allowed to print a helpful
representation of each object in the list, calling the str() functions which
made my solution to slow to solve part 2 of the problem.



