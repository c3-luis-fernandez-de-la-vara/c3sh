#!/usr/bin/env python3

import inspect
from collections import namedtuple
from functools import wraps
import builtins
import logging
import argparse
from textwrap import dedent
from utils_local_setup import FormatWithColors
import sys

# declare exported symbols
__all__ = ['cli', 'CliOption']


class _SaneFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass






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

    # import all subjects/* handlers.
    __import__('subjects')
    cli.start()
