import builtins
import argparse
import sys
from textwrap import dedent
import logging
from classes.ParserWithCapturingErrors import ParserWithCapturingErrors
from classes.subject import Subject
from classes.sane_formatter import SaneFormatter
from util.utils_local_setup import FormatWithColors

__all__ = ["CLI"]

logger = logging.getLogger()
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = FormatWithColors("%(message)s")
ch.setFormatter(formatter)
logger.handlers = [ch]
logger.setLevel(logging.INFO)

class CLI:
    """Main entry point of CLI. It used too construct <subjects> and to parse command line arguments."""

    def __new__(cls, *args, **kwargs):
        logger.info("cli.py | __new__ | ensuring singleton for cli")
        """Ensure CLI is singleton"""
        if not hasattr(builtins, "__c3sh_instance__"):
            setattr(builtins, "__c3sh_instance__", super(CLI, cls).__new__(cls))
            getattr(builtins, "__c3sh_instance__").__init(*args, **kwargs)
        return getattr(builtins, "__c3sh_instance__")

    def __init(self, prog, description, formatter_class=SaneFormatter, **kwargs):
        self.common_parser = argparse.ArgumentParser(add_help=False)

        common_parser_group = self.common_parser.add_argument_group("Global arguments")

        common_parser_group.add_argument(
            "-d",
            "--debug",
            action="store_true",
            help="Show additional output",
            default=argparse.SUPPRESS,
        )
        common_parser_group.add_argument(
            "-m",
            "--no-colors",
            action="store_true",
            help="Disable colors in outputs",
            default=argparse.SUPPRESS,
        )

        self._parser = ParserWithCapturingErrors(
            prog=prog,
            description=description,
            formatter_class=formatter_class,
            parents=[self.common_parser],
            **kwargs,
        )

        self.subparsers = self._parser.add_subparsers(
            title="Subject", parser_class=ParserWithCapturingErrors, dest="subject"
        )
        self.parsers = {}

        self.subparsers.add_parser("help", help="Shows current help message")

    def subject(
        self, name, formatter_class=SaneFormatter, common_options=None, **kwargs
    ) -> Subject:
        if "description" in kwargs:
            kwargs["description"] = dedent(kwargs["description"])

        return Subject(
            self,
            name,
            common_options,
            self.subparsers.add_parser(
                name,
                formatter_class=formatter_class,
                parents=[self.common_parser],
                **kwargs,
            ),
        )

    def start(self, args=None):
        if args is None:
            args = sys.argv[1:]

        parsed_arg, unrecognized = self._parser.parse_known_args(args)

        if unrecognized:
            parser_name = f"{getattr(parsed_arg, 'subject', '')}.{getattr(parsed_arg, 'action', '')}"
            self.parsers.get(parser_name, self._parser).print_help()
            if "help" in unrecognized:
                sys.exit(0)
            unrecognized = ", ".join(unrecognized)
            logger.error(f"Unrecognized arguments: {unrecognized}")
            sys.exit(2)

        if getattr(parsed_arg, "debug", False):
            logger.setLevel(logging.DEBUG)
            logger.debug("Enable debugging mode")

        if getattr(parsed_arg, "no_colors", False):
            formatter.no_colors(True)

        if (
            getattr(parsed_arg, "subject", None) == "help"
            or getattr(parsed_arg, "subject", None) is None
        ):
            self._parser.print_help()
            sys.exit(0)

        if getattr(parsed_arg, "action", None) is None:
            self.parsers[f"{getattr(parsed_arg, 'subject')}."].print_help()
            sys.exit(0)

        parsed_arg.func(parsed_arg)
