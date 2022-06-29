#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mariadb

import sys
from myapp.code import function_does_nothing
from myapp.submodule.just_another_module import function_does_nothing_too


def main():
    """
    Example main file.

    Uses at least something from mariadb so the import is not completely
    useless. In addition we import from a submodule so dockerfiles copy
    command needs to build up a directory structure.
    """
    print(f"loaded sample project with mariadb import supporting api " 
           "level {mariadb.apilevel}")

    print(function_does_nothing())
    print(function_does_nothing_too())


if __name__ == "__main__":
    sys.exit(main())
