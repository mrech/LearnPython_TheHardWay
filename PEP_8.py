# Shift + Alt + F: formatting with autopep8
# INDENTATION

# YES
# Aligned with opening delimiter.

from typing import TypeVar
from subprocess import Popen, PIPE
import sys
import os
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.


foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# NO
# Arguments on first line forbidden when not using vertical alignment.

foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Further indentation required as indentation is not distinguishable


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Optional:
# Hanging indents *may* be indented to other than 4 spaces.


foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# No extra indentation.
if (this_is_one_thing and
        that_is_another_thing):
    do_something()

# add a comment, which will provide some distinction in editors
# supporting syntax highlighting.

if (this_is_one_thing and
        that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

# The closing bracket
my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd'
)

# TABS OR SPACES
# Spaces are the preferred indentation method.

# MAXIMUM LINE LENGTH
# Limit all lines to a maximum of 79 characters (and docstrings/comments to 72).

# Long lines can be broken over multiple lines by wrapping expressions in parentheses.
# This is preferred to using a backslash for line continuation.

# Tough multiple with-statements cannot use implicit continuation -> \

with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

# SHOULD A LINE BREAK BEFORE OR AFTER A BINARY OPERATOR

# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# Knuth's style is suggested.
# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# It's important to keep internal consistency

# BLANK LINES
# top-level function and class definitions with two blank lines
# method definitions inside a class are surrounded by a single blank line
# use blank lines in functions, sparingly, to indicate logical sections

# SOURCE FILE ENCODING
# Python 3 (UTF-8)
# using \x, \u, \U, or \N escapes is the preferred way to include non-ASCII
# data in string literals.
# PEP 3131

# IMPORTS
# Imports always put at the top of the file
'''
1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

You should put a blank line between each group of imports.
'''
# Absolute imports are recommended import mypkg.sibling
# explicit relative imports are an alternative from . import sibling

# importing a class from a class-containing module
# from myclass import myclass
# if it causes clashes, then spell them explicitly:
# import myclass -> than use myclass.MyClass

# STRING QUOTES
# Pick ' or " and stick with it
# For triple-quoted strings use """ be consistent with PEP 257

# WHITESPACE IN EXPRESSIONS AND STATEMENTS
# NO white space immediately inside parentheses
spam(ham[1], {eggs: 2})

# NO white space between a trailing comma and a flose parenthesis
foo = (0,)

# NO immediatly before a comma, semicolon, or colon:
if x == 4:
    print("x, y; x, y = y, x")

# YES
ham = [1, 2, 5, 6, 7, 8, 9]
lower = 1
upper = 5
offset = 1

# when a slice parameter is omitted, the space is omitted.
# ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
# ham[lower:upper], ham[lower:upper:], ham[lower::step]
# colons must have the same amount of spacing applied
ham[lower+offset:upper+offset]
# ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
# ham[lower + offset : upper + offset]

# NO immediately before the open parenthesis
spam(1)
det['key'] = lst[index]

# one space around an assignment/binary operator
x = 1
y = 2
long_variable = 3

# if operators with different priorities are used, consider adding whitespace
# around the operators with the lowest priority

# Yes:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a*b)

# Function annotations


def munge(input: AnyStr): ...


def munge() -> AnyStr: ...

# Don't use spaces around the = sign when used to indicate a keyword argument,
# or when used to indicate a default value for an unannotated function parameter.


def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# combining an argument annotation with a default value
# do use spaces around the = sign


def munge(input: AnyStr, sep: AnyStr = None, limit=1000):


# Compound statements (multiple statements on the same line) are generally discouraged
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()

# never putmulti-clause statements on the same line

if foo == 'blah':
    do_blah_thing()
for x in lst:
    total += x
while t < 10:
    t = delay()

# When to Use Trailing Commas, mandatory when making a tuple of one element

FILES = ('setup.cfg',)

# When trailing commas are redundant, they are often helpful when a version control
# system is used, when a list of values, arguments or imported items is expected
# to be extended over time.

FILES = [
    'setup.cfg',
    'tox.ini',
]
initialize(FILES,
           error=True,
           )


# COMMENTS
# Keep the comments up-to-date when the code changes

# You should use two spaces after a sentence-ending
# period in multi- sentence comments, except after the final sentence

# Each line of a block comment starts with a
# # and a single space (unless it is indented text inside the comment)
# Paragraphs inside a block comment are separated by a line containing a single #

# Inline comments used sparingly
# Separated by at least two spaces from the statement

"""docstrings"""

"""Return a foobang

Optional plotz says to frobnicate the bizbaz first
"""
# A docstring is a string literal that occurs as the first statement in a
# module, function, class, or method definition.
# string becomes the __doc__ special attribute of that object.


# NAMING CONVENTIONS
# https://www.python.org/dev/peps/pep-0008/#pet-peeves
# Package and Module Names
# MODULE and FUNCTION and VARIABLE and METHOD: short, all-lowercase name,
# with underscore ex: my_awesome_hair
# CLASS and EXCEPTION: CapWords ex: SuperGoldFactory
# Variable Names: short names with CapWords


VT_co = TypeVar('VT_co', covariant=True)

# self for the first argument to instance methods
# cls for the first argument to class methods
# CONSTANT defined on a module level: in capital letters with underscores
# e.g. MAX_OVERFLOW

# DESIGNING FOR INHERITANCE (?)
# PUBLIC AND INTERNAL INTERFACES


def f(x): return 2*x


try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None


try:
    process_data()
except Exception as exc:
    raise DataProcessingFailedError(str(exc))


try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

x = 2+45

# Be consistent in return statements.


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None


def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

# Use string methods instead of the string module.
# Use ''.startswith() and ''.endswith() instead of
# string slicing to check for prefixes or suffixes.


if foo.startswith('bar')

obj = 'hello'

if isinstance(obj, int):

    # FUNCTION ANNOTATIONS
