
"""
catarob
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation

How to use the documentation
----------------------------
We recommend exploring the docstrings using
`IPython <http://ipython.scipy.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.

The docstring examples assume that `catarob` has been imported as `cb`::

  >>> import catarob as cp

Use the built-in ``help`` function to view a function's docstring::

  >>> help(cb.lib.cvnumpy)
  ... # doctest: +SKIP

Available subpackages
---------------------
core
    Core functions used by gui
lib
    Basic functions used by several sub-packages.
gui
    Graphical interface that use core functions
"""

import lib
import core
import gui

    