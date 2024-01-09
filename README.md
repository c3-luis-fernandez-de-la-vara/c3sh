# c3sh
ishell cli client for c3 server

## overview

c3 client Python CLI.
Usage:

'c3sh <subject> <action> <parameters>'

command `help` accepted at any level.

### structure:
```
|--c3sh.py
|--subjects/
|---------/*.py
```
### adding new command as `subject`
```
k8s_coredns = cli.subject(
    name='k8s-coredns',
    help='<one line description',
    description='<detailed description of the subject>',
    common_options=[
        CliOption(['-c', '--context'], {'help': 'K8s context to use. If not specified current context will be used'})
        <list of options that would be added to all subject actions>
    ]
)

@k8s_coredns.command()
def info(context=None):
    '''Help message of info action'''


@k8s_coredns.command(options=[
    CliOption(['host'], {'help': 'Host name that need to be resolved'}),
])
def rewrite(host, context=None):
    '''Help message for rewrite action'''
```
