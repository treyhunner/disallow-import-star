# SPDX-FileCopyrightText: 2023-present Trey Hunner <trey@treyhunner.com>
#
# SPDX-License-Identifier: MIT
import builtins
from textwrap import dedent


star_exception = ImportError(dedent("""
    import * explicitly disallowed

    April Fools!

    Learn Python tips that are actually practical from https://pym.how
""").strip())


class NoStar:
    def __getitem__(self, index):
        raise star_exception


__all__ = NoStar()


_original_import = builtins.__import__


def __import__(name, globals=None, locals=None, fromlist=(), level=0):
    if fromlist and fromlist[0] == "*":
        raise star_exception
    return _original_import(name, globals, locals, fromlist, level)


def disallow_import_star_EVERYWHERE():
    builtins.__import__ = __import__
