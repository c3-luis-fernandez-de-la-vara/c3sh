import inspect
import logging
from functools import wraps
from classes.sane_formatter import SaneFormatter
from classes.ParserWithCapturingErrors import ParserWithCapturingErrors

"""
Base class for construction CLI entrypoint like v8 <subject> <action>

It creates <subject> section for command v8 command and allow too create <actions> using decorators. Example
```
from utils_python_cli_framework import cli, CliOption
k8s_local = cli.subject(
    name='k8s-local', help='Short description', description='long multiline description', common_options=[
        CliOption(['-p', '--profile'], {'help': 'minikube profile'}),
    ]
)

@k8s_local.command()
def configure(profile):
    '''command help'''
    ...

@k8s_local.command(options=[
    CliOption(['-s', '--stop-minikube'], {'help': 'stop cluster', 'action': 'store_true', 'dest': 'stop_minikube'}),
])
def clear(profile, stop_minikube=False):
    '''command help'''
    ...
```

In this example subject `k8s-local` is created with two actions `configure` and `clear`. Both of them have parameter
`profile`. `clear` action also have optional parameter `-s`.

Second parameter of `CliOption` accepts same parameters as argparse add_argument. Such parameters should be passed
as a dict.
"""

__all__ = ['Subject']

logger = logging.getLogger()
class Subject:

    def __init__(self, cli, name, common_options, parser):
        self._cli = cli
        self._name = name
        self._cli.parsers[name + '.'] = parser
        self.parser = parser
        self.common_options = common_options

        if common_options:
            common_parser_group = self.parser.add_argument_group("Subject level arguments")
            for option in common_options or []:
                option_names = (option.names,) if isinstance(option.names, str) else option.names
                common_parser_group.add_argument(*option_names, **option.parameters)

        self._subject_parser = self.parser.add_subparsers(
            parser_class=ParserWithCapturingErrors, title='Action', dest='action')
        self.command('help', 'Show this help message')(lambda: self.parser.print_help())

    def command(self, name=None, help=None, description=None, options=None, **kwargs):
        def decorator(f):
            parser_name = f.__name__ if name is None else name
            parser = self._subject_parser.add_parser(
                name=parser_name,
                help=f.__doc__.split('\n')[0] if help is None and f.__doc__ else help,
                description=f.__doc__ if description is None and f.__doc__ else description,
                parents=[self._cli.common_parser],
                formatter_class=SaneFormatter,
                **kwargs,
            )

            if self.common_options:
                common_parser_group = parser.add_argument_group("Subject level arguments")
                for option in self.common_options:
                    option_names = (option.names,) if isinstance(option.names, str) else option.names
                    common_parser_group.add_argument(*option_names, **option.parameters)

            if options:
                parser_group = parser.add_argument_group("Action level arguments")
                for option in options:
                    option_names = (option.names,) if isinstance(option.names, str) else option.names
                    parser_group.add_argument(*option_names, **option.parameters)

            self._cli.parsers[f'{self._name}.{parser_name}'] = parser

            @wraps(f)
            def wrapper(parsed):
                setattr(f, 'parsed', parsed)
                params = {p: getattr(parsed, p, None) for p in inspect.signature(parsed.func).parameters}
                return f(**params)

            setattr(f, 'cliWrapper', wrapper)
            parser.set_defaults(func=wrapper)
            return f

        return decorator

