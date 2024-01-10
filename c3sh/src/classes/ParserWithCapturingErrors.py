
import argparse
import logging
import sys

__all__ = ['ParserWithCapturingErrors']
logger = logging.getLogger()
class ParserWithCapturingErrors(argparse.ArgumentParser):
    def error(self, message):
        logger.error(f'Command line options parsing failure: {message}')
        self.print_help()
        sys.exit(2)
