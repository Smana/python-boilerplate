#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Smana"
__version__ = "0.0.1"
__license__ = "APACHE 2"

import sys

import click

from myapp.utils import get_kwarg_value_or_empty

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def greeter(**kwargs):
    output = "{0}, {1}!".format(kwargs["greeting"], kwargs["name"])
    name = get_kwarg_value_or_empty(kwargs, "name")
    print("Name is ", name)
    if kwargs["caps"]:
        output = output.upper()
    print(output)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def myapp():
    pass


@myapp.command()
@click.argument("name", required=True)
@click.option(
    "--greeting", default="Hello", help="word to use for the greeting"
)
@click.option("--caps", is_flag=True, help="uppercase the output")
def hello(**kwargs):
    greeter(**kwargs)


@myapp.command()
@click.argument("name")
@click.option(
    "--greeting", default="Goodbye", help="word to use for the greeting"
)
@click.option("--caps", is_flag=True, help="uppercase the output")
def goodbye(**kwargs):
    greeter(**kwargs)


if __name__ == "__main__":
    sys.exit(myapp())
