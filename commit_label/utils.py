#!/usr/bin/env python
# coding: utf-8

import os
import delegator


def _run(cmd):

    return delegator.run(cmd).out.strip()


def git(cmd):

    shell_cmd = "git {0}".format(cmd)
    return _run(shell_cmd)


def boolify(string):

    return True if string == "true" else False


def is_inside_work_tree():

    return boolify(git("rev-parse --is-inside-work-tree"))


def get_hook_dir():

    source = os.path.relpath(
        os.path.join(__file__, "../../hook")
    )

    git_dir = git("rev-parse --git-dir")
    dest = os.path.join(git_dir, "hooks")

    return source, dest
