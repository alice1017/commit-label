#!/usr/bin/env python
# coding: utf-8

import os
import sys
import shutil

from .cli import parser
from .utils import (
    is_inside_work_tree,
    get_hook_dir
)


def install_hook(hook_file):

    if not is_inside_work_tree():
        raise IOError("Here is not the git repository.")

    source_dir, dest_dir = get_hook_dir()

    source_path = os.path.join(source_dir, hook_file)
    dest_path = os.path.join(dest_dir, hook_file)

    if os.path.isfile(dest_path):

        print "{0} hook already installed.".format(hook_file)
        print "Do you update hook script? ",

        confirm = raw_input("[y/n] ")
        if confirm != "y":
            return 1

    shutil.copy(source_path, dest_path)

    print "done."


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)

    args = parser.parse_args()
    hook_file = "prepare-commit-msg"

    if args.cmd == "init":

        result_code = install_hook(hook_file)
        sys.exit(result_code)


if __name__ == "__main__":

    main()
