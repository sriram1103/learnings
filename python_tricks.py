assert 0 <= price <= product['price']
    return price

assert syntax:
assert_stmt ::= "assert" expression1 ["," expression2]
assert(1 == 2, 'This should fail')

names = [
...     'Alice',
...     'Bob',
...     'Dilbert'
... ]

Define dict for easy maintanence

with open('hello.txt', 'w') as f:
    f.write('hello, world!')
    
Python calls __enter__ when execution enters the context of the with statement 
and it’s time to acquire the resource. When execution leaves the context again, Python calls __exit__ to free up the resource.

from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

>>> with managed_file('hello.txt') as f:
...     f.write('hello, world!')
...     f.write('bye now')


 "_var":
 
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23 
        
t = Test()
>>> t.foo
11
>>> t._bar
23


# my_module.py:

def external_func():
    return 23

def _internal_func():
    return 42

>>> from my_module import *
>>> external_func()
23
>>> _internal_func()
NameError: "name '_internal_func' is not defined"


>>> import my_module
>>> my_module.external_func()
23
>>> my_module._internal_func()
42

 "var_":
 
Sometimes the most fitting name for a variable is already taken by a keyword in the Python language. 
Therefore, names like class or def cannot be used as variable names in Python. 
In this case, you can append a single underscore to break the naming conflict:

"__var":

A double underscore prefix causes the Python interpreter to rewrite the attribute name 
in order to avoid naming conflicts in subclasses.

class Test:
    def __init__(self):
        self.__var = 42

>>> t = Test()
>>> dir(t)
['_Test__var', '__class__', '__delattr__', '__dict__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 
 t.__var
 >> t.__var variable undefined
 
 t._Test__var
 >> 42
 
 
 class Ex(Test):
  def __init__(self):
   self.__var = 12

t2 = Ex()

 >>> dir(t2)
['_Ex__var', '_Test__var', '__class__',..

"_": 
>>> for _ in range(32):
...     print('Hello, World.')

Single Trailing Underscore “var_”: 
Used by convention to avoid naming conflicts with Python keywords. 

Double Leading Underscore “__var”: 
Triggers name mangling when used in a class context. 
Enforced by the Python interpreter. 

Double Leading and Trailing Underscore “__var__”: 

Indicates special methods defined by the Python language. 
Avoid this naming scheme for your own attributes. 

Single Underscore “_”: 
Sometimes used as a name for temporary or insignificant variables (“don’t care”). 
Also, it represents the result of the last expression in a Python REPL session.


>>> '%x' % errno
'badc0ffee'

>>> 'Hey %s, there is a 0x%x error!' % (name, errno)
'Hey Bob, there is a 0xbadc0ffee error!'


>>> 'Hello, {}'.format(name)
'Hello, Bob'

>>> 'Hey {name}, there is a 0x{errno:x} error!'.format(
...     name=name, errno=errno)
'Hey Bob, there is a 0xbadc0ffee error!'

>>> a = 5
>>> b = 10
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'


>>> from string import Template
>>> t = Template('Hey, $name!')
>>> t.substitute(name=name)
'Hey, Bob!'


>>> tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
>>> sorted(tuples, key=lambda x: x[1])
[(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]


def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
