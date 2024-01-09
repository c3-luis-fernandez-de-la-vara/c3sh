#!/usr/bin/env python3

from collections import namedtuple
import logging
from util.utils_local_setup import FormatWithColors
from classes.cli import CLI
# declare exported symbols
__all__ = ['CliOption']

# This represent argument that usually added by `argparse` `parser.add_argument`.
# Parameters are used to construct argument as follow: `parser.add_argument(*names, **parameters)
CliOption = namedtuple('CliOption', ['names', 'parameters'])

cli = CLI('v8', 'V8 CLIs entrypoint')

if __name__ == '__main__':
    # Configure logger
    logger = logging.getLogger()
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = FormatWithColors('%(message)s')
    ch.setFormatter(formatter)
    logger.handlers = [ch]
    logger.setLevel(logging.INFO)
    logger.info("c3sh.py | main") 

    # import all subjects/* handlers.
    __import__('subjects')
    cli.start()
