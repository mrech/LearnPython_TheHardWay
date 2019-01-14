# MODULE LEVEL DUNDER NAMES (two leading/two trailing underscores)

"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys

# should be placed after the module docstring but before any import 
# statements except from __future__ imports.

