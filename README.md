# python-logging-impact
Demonstration of possible impact performances when passing functions to logging.

## Python logging statements executed regardless of logging level
Logging statements (`logging.info`, `logging.debug`, etc...) are executed, that's how they determine the log level and decide to proceed further or not.

## Function composition eagerness
Python is eager when doing function composition, logme() is executed before being passed to logging.debug.

https://stackoverflow.com/questions/53782625/why-are-logging-statement-in-python-evaluated-regardless-of-level/53783577

## Solutions
1. Use the Python % string formating + variables:
    logging.debug = debug(msg, *args, **kwargs)
2. Make the argument lazylly evaluated? Still exploring...

## Original Problem statement
If you run the script in this repo without
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

