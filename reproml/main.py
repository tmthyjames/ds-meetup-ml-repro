#!/usr/bin/env python
import click

from .__about__ import __version__
from .etl import commands as etl_commands
from .ml import commands as ml_commands


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


def main():
    cli.add_command(etl_commands.etl)
    cli.add_command(ml_commands.ml)
    cli()


if __name__ == "__main__":
    main()
