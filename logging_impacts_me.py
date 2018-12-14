#!/usr/bin/env python3

#import time
import argparse
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

def logme():
    #time.sleep(10)
    print('I was executed ☠')
    return 'loggging all the things...'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d",
                         action='store_true',
                         help="Debug mode (very verbose)",
                        )

    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

print('hello')
logging.debug('{}'.format(logme()))
print('bye')
