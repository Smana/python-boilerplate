#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Smana"
__version__ = "0.0.1"
__license__ = "APACHE 2"
import argparse
import sys


def run(args):
    """
    Function Docstring
    """
    print(vars(args).keys())


def main():
    parser = argparse.ArgumentParser(
        prog="myapp", description="%(prog)s description example", add_help=True
    )
    subparsers = parser.add_subparsers(help="commands")

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + " %s" % __version__,
    )

    parent_parser = argparse.ArgumentParser(add_help=False)

    parent_parser.add_argument(
        "-d",
        "--config-dir",
        dest="config_dir",
        default="/myap/config",
        help="Config file",
    )
    parent_parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        dest="is_verbose",
        action="store_true",
        help="Print detailed logs",
    )

    run_parser = subparsers.add_parser("run", parents=[parent_parser], help="")
    run_parser.set_defaults(func=run)

    args = parser.parse_args()

    try:
        args.func(args)
    except Exception as err:
        print("Error: ", err)
        parser.print_help()


if __name__ == "__main__":
    sys.exit(main())
