# SPDX-FileCopyrightText: 2023-present Trey Hunner <trey@treyhunner.com>
#
# SPDX-License-Identifier: MIT
from disallow_import_star import __all__
import pytest


def test_looping_over_all_fails():
    with pytest.raises(ImportError):
        list(__all__)


def test_no_star_import_allowed():
    with pytest.raises(ImportError):
        exec("from disallow_import_star import *")
