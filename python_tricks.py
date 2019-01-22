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

 def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1
 
 >>> my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
>>> import json
>>> print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
>>> json.dumps({all: 'yup'})
TypeError: keys must be a string
 
 >>> from collections import namedtuple
>>> Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
>>> my_car = Car('red', 3812.4)
>>> my_car.color
'red'
>>> my_car.mileage
3812.4

# We get a nice string repr for free:
>>> my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
>>> my_car.color = 'blue'
AttributeError: "can't set attribute"
 
 name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

>>> greeting(382)
"Hi Alice!"

>>> greeting(333333)
"Hi there!"
 
 >>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

>>> sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
 
 >>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}

>>> z = {**x, **y}

>>> z
{'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
>>> z = dict(x, **y)
>>> z
{'a': 1, 'c': 4, 'b': 3}
 
 >>> a = [1, 2, 3]
>>> b = a

a == b
 True
a is b
 True
 
c = list(a)
a == c
 True
a is c
 False
 
An is expression evaluates to True if two variables point to the same (identical) object. 
 An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).

Instead of building your own to-string conversion machinery, 
you’ll be better off adding the __str__ and __repr__ “dunder” methods to your class. 
 
 They are the Pythonic way to control how objects are converted to strings in different situations
 
 class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

 >>> my_car = Car('red', 37281)
>>> print(my_car)
'a red car'
>>> my_car
<__console__.Car object at 0x109ca24e0>

 >>> print(my_car)
a red car
>>> str(my_car)
'a red car'
>>> '{}'.format(my_car)
'a red car'

 class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

 >>> my_car = Car('red', 37281)
>>> print(my_car)
__str__ for Car
>>> '{}'.format(my_car)
'__str__ for Car'
>>> my_car
__repr__ for Car


class BaseValidationError(ValueError):
    pass 
class NameTooShortError(BaseValidationError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass

try:
    validate(name)
except BaseValidationError as err:
    handle_validation_error(err)

 >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> ys = list(xs)  # Make a shallow copy 
 #ys = copy.copy(xs) # shallow copy


 >>> xs.append(['new sublist'])
>>> xs
[[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
>>> ys
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

 >>> import copy
>>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> zs = copy.deepcopy(xs)
>>> xs[1][0] = 'X'
>>> xs
[[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
>>> zs
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

 
 ABC:
 ====
 
 instantiating the base class is impossible; and 
 forgetting to implement interface methods in one of the subclasses raises an error as early as possible.

 from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

 >>> c = Concrete()
TypeError:
"Can't instantiate abstract class Concrete 
with abstract methods bar"

 class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable

>>> jack = Dog('Jack')
>>> jill = Dog('Jill')
>>> jack.name, jill.name
('Jack', 'Jill')

>>> jack.num_legs, jill.num_legs
(4, 4)
>>> Dog.num_legs
4
 
 >>> Dog.num_legs = 6 
 >>> jack.num_legs, jill.num_legs
(6, 6)
 
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
 
>>> obj = MyClass()
>>> obj.method()
('instance method called', <MyClass instance at 0x11a2>)

 >>> MyClass.method(obj)
('instance method called', <MyClass instance at 0x11a2>)

 >>> obj.classmethod()
('class method called', <class MyClass at 0x11a2>)

 >>> obj.staticmethod()
'static method called'

 >>> MyClass.classmethod()
('class method called', <class MyClass at 0x11a2>)

>>> MyClass.staticmethod()
'static method called'
 
 
 class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

 

 class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

 >>> Pizza.margherita()
Pizza(['mozzarella', 'tomatoes'])

>>> Pizza.prosciutto()
Pizza(['mozzarella', 'tomatoes', 'ham'])

 
 >>> from collections import ChainMap
>>> dict1 = {'one': 1, 'two': 2}
>>> dict2 = {'three': 3, 'four': 4}
>>> chain = ChainMap(dict1, dict2)

>>> chain
ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
>>> chain['three']
3

 >>> from types import MappingProxyType
>>> writable = {'one': 1, 'two': 2}
>>> read_only = MappingProxyType(writable)

# The proxy is read-only:
>>> read_only['one']
1
>>> read_only['one'] = 23
TypeError:
"'mappingproxy' object does not support item assignment"

# Updates to the original are reflected in the proxy:
>>> writable['one'] = 42
>>> read_only
mappingproxy({'one': 42, 'two': 2})

 
 

 Stack in python
  list, collections.deque (preferred)
 
 Queues in python
  list - slow
  collection.deque - fast
  queue.queue - parallel computing 
 
 Priority Queue:
  List - sort every time a value (key,value) is inserted
  heapq – List-Based Binary Heaps
  queue.PriorityQueue – Beautiful Priority Queues - prefered
 
 
 my_items=[a,b,c]
 >>> for i, item in enumerate(my_items):
...     print(f'{i}: {item}')

0: a
1: b
2: c


values = []
for item in collection:
    values.append(expression)

values = [expression for x in collection]
 
 >>> lst = [1, 2, 3, 4, 5]
>>> lst
[1, 2, 3, 4, 5]

#   lst[start:end:step] list slicing
 
>>> lst[::2]
[1, 3, 5]
>>> numbers[::-1]
[5, 4, 3, 2, 1]  #reverse list

#list shallow copy
>>> copied_lst = lst[:]
 
>>> xs = {'a': 1, 'b': 2}
>>> ys = {'b': 3, 'c': 4}
>>> zs = dict(xs, **ys)
>>> zs
{'a': 1, 'c': 4, 'b': 3}

>>> zs = {**xs, **ys} # only in python3



