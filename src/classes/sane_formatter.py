import argparse

__all__ = ['SaneFormatter']

class SaneFormatter(
    argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter
):
    pass