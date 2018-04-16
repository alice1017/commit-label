#!/usr/bin/env python
# coding: utf-8

import sys

from .cli import parser


def install_hook():

    pass


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)

    args = parser.parse_args()
    print args

    if args.cmd == "init":

        result_code = install_hook()
        sys.exit(result_code)


if __name__ == "__main__":

    main()
