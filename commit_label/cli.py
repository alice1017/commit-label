#!/usr/bin/env python
# coding: utf-8

from argparse import (
    ArgumentParser,
    RawDescriptionHelpFormatter
)

description = ("The commit-label is the git hook to put a label "
               "beginning of the commit message.")

description += """

List of the Labels:
WROTE - Use when wrote the document such as `README`.
FIXED - Use when fixed the bugs or issues.
IMPLEMENTED - Use when added the new feature.
ENHANCED - Use when implemented feature enhanced.
TESTED - Use when wrote the unit test.
ELEASED - Use when released to the product.
"""

parser = ArgumentParser(
    prog="commit-label",
    formatter_class=RawDescriptionHelpFormatter,
    description=description
)

subparser = parser.add_subparsers(dest="cmd")

init_parser = subparser.add_parser(
    "init",
    help="Install pre-commit hook to your repository.")
