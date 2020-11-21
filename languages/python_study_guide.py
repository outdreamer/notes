
    - stochastic programming: improvise a policy to maximize expected value, based on available data & probability distributions

    - dynamic programming: breaking a problem solved over multiple periods into sub problems, which are solvable given state & optimization function
        example: dijkstra algorthm for shortest path involves the assumption that knowing distance from origin to interim node is a pre-condition for knowing distance from origin to target node

    - stochastic dynamic programming: compute a policy to maximize expected value, assuming randomness


    - procedure: function with no return value (in python returns None even without a return value)

    - function:

        - docstring: first, string literal statement of the function body
        - execution: introduces a new symbol table used for the local variables of the function
            - when a function calls another function, a new local symbol table is created for that call
        - variable assignments in a function store the value in the local symbol table
        - variable references look in the local table, then local tables of enclosing functions, then the global symbol table, then the built-in names table

        - global: 
            - global & enclosing function variables cannot be directly assigned a value within a function 
            - unless a global var is named in a global statement, or an enclosing function var named in a nonlocal statement

        - parameters are passed using call by value (where the value is always an object reference, not the value of the object)

        - optional args have default values to the right of the required args
        - non-keyword arguments cant be passed after a keyword/named argument
        - arg order doesnt matter even with required args
        - defaults are executed once in consecutive calls, unless assigned a value of None as default
        - *args is a tuple of the positional optional arguments after the required argument or can store any arguments after the preceding formal parameters
        - **keywords generates a dict of the keyword/named arguments, in the order they were passed
        - *args must be before **keywords
        - named args cant be keys in **keywords dict without positional delimiter /
        - def f(positional, /, positional_or_keyword, *, keyword): # separates positional args, positional & keyword args, and keyword args for clarity

        - pass sequence of positional arguments to a function: range(*args)
        - pass dict of keyword arguments to a function: print_dict(**d)

        - function annotations about types:
            def f(var1: str, var2: str = 'default') -> str:


- new features

    - in 2.7:
        - high memory requirements: dict.items(), dict.keys() and dict.values() return a copy of this_dict list of 2-tuples (key, value)
        - dict.iteritems(), dict.iterkeys() and dict.itervalues() return an iterator over key value pairs

    - python 3 updates (from python 2)
        - Whenever two integers are divided, you get a float value (instead of an integer)
        - str is unicode by default 
        - ordering comparisons simplified
        - range uses xrange
        - exceptions enclosed in parenthesis instead of notations
        - value of variables doesnt change (instead of updating global variable in a for loop)
        - In Python 3, raw_input() function is deprecated. Further, the received data is always treated as string (rather than optionally a number)
        - lists can be cleared with clear() method
        - unpacking of remaining vars: first, *rest, last = f.readlines()
        - cross-type comparisons throw a TypeError
        - added some exceptions (FileNotFoundError, PermissionError, IsADirectoryError and TimeoutError)
             try:
                 f = open('is_it_there.txt')
             except FileNotFoundError:
        - only dict.items(), dict.keys(), and dict.values() are available, and return the view objects
        - turn a view into an iterator using iter(this_view)

    - python 3.5: 
        - added type hinting
        - @ infix operator was introduced, used by libraries such as NumPy for matrix multiplication

    - new features in python 3.6
       - dictionaries using 20% to 25% less memory when compared to Python 3.5
       - The order of elements in **kwargs now corresponds to the order in which keyword arguments were passed to the function.
       - DTrace and SystemTap probing support has been added
       - new secrets module
       - f-strings 
            Formatted string literals are prefixed with 'f' and are similar to the format strings accepted by str.format(). 
            They contain replacement fields surrounded by curly braces. 
            The replacement fields are expressions, which are evaluated at run time, and then formatted
            python 2: 'The value is {value_reference}.'.format(value_reference=value)
            python 3.6: f'The value is {value}.'
            - curly brackets can contain expressions
        - type hints/annotations syntax:
            primes: List[int] = []
            stats: Dict[str, int] = {}
        - asynchronous generators & comprehensions
        - underscores in numbers

    - new features in python 3.7
        The breakpoint() Built-In
        Data Classes
        Customization of Module Attributes
        Typing Enhancements
        Timing Precision
        The Order of Dictionaries Is Guaranteed equal to insertion order
        “async” and “await” Are Keywords
        “asyncio” Face Lift
        Context Variables
        Importing Data Files With “importlib.resources“
        Optimizations
            There is less overhead in calling many methods in the standard library.
            Method calls are up to 20% faster in general.
            The startup time of Python itself is reduced by 10-30%.
            Importing typing is 7 times faster.

    - new features in Python 3.8 version: /, :=, f"{x = y}", dict.reversed()

        Positional Only parameter(/)
        Assignment Expression(:=) for compound expressions, assigns values to variables as part of a larger expression
        f-strings now support “=”
        reversed() works with a dictionary

    - new features in python 3.9

        Proper Time Zone Support: Accessing/Investigating Time Zones
        Simpler Updating of Dictionaries
        More Flexible Decorators
        Annotated Type Hints
        A More Powerful Python Parser (Parsing expression grammer - PEG)
        String Prefix and Suffix
        Type Hint Lists and Dictionaries Directly
        Topological Sort
        Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
        New HTTP Status Codes
        Removal of Deprecated Compatibility Code

    - 2:
        - high memory requirements: dict.items(), dict.keys() and dict.values() return a copy of this_dict list of 2-tuples (key, value)
        - dict.iteritems(), dict.iterkeys() and dict.itervalues() return an iterator over key value pairs

    - 3: 
        - int/int == float, str() == unicode string, xrange => range, (exception), raw_input() => input(), list.clear(), f, *middle, l = f.readlines()
        - TypeError for cross-type comparisons, added FileNotFoundError, PermissionError, IsADirectoryError, TimeoutError
        - dict.items(), dict.keys(), and dict.values() return the view objects
        - turn a view into an iterator using iter(this_view)
        - ordering comparisons simplified
        - global variable value doesnt change
    - 3.5: @ dot product, type hinting 
    - 3.6: async generators/comprehensions, low memory dict, kwargs order preserved, dtrace/systemtap, secrets, f'formatted {strings = True}' instead of '{v1}'.format(v1=strings), type hint syntax
    - 3.7: breakpoint() built-in, data classes, module attribute customization, context variables, aync/await/asyncio, importlib.resources, faster method calls/startup time/typing import
    - 3.8: /, :=, f"{x = y}", dict.reversed()
    - 3.9: time zone, dict update, flexible decorators, type hint (annotations, lists/dicts), topological sort, gcd/lcm, new http codes, Parsing Expression Grammar parser


- benefits of using Python language:
    Object-Oriented Language
        - allows the definition of classes along with composition and inheritance
        - Python does not have access specifiers (public/private)
        - Python can be treated as procedural as well as structural language.
        - everything is an object with no values (except references)
    Dynamically Typed language
        - the Python interpreter does type checking only as code runs, and that the type of a variable is allowed to change over its lifetime
        - Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. 
            Using duck typing you do not check types at all. 
            Instead you check for the presence of a given method or attribute
            Duck typing is somewhat supported when doing static type checking of Python code
    - Python:
        - case sensitive language
        - supports multiple inheritance, unlike Java. 
            - Multiple inheritance means that a class can be derived from more than one parent classes.
        - Python allows polymorphism
            - Polymorphism means the ability to take multiple forms. 
            - So, for instance, if the parent class has a method named ABC then the child class also can have a method with the same name ABC having its own parameters and variables. 
        - supports encapsulation (binding the code and data). A Python class is an example of encapsulation
        - functions & classes are first-class objects
        - procedure: function with no return value (in python returns None even without a return value)

- main method (automatically executed on running program)
    def main():
        print("Hello World!")
    if __name__ == "__main__":
        main()

- keywords

    - with
        - used when working with unmanaged resources (like file streams)
        - allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown
        - syntactic sugar for try/finally

    - while:
        - while loop requires relevant variables to be ready
        - execute code in loop until a condition is false

        - compilation
            - when speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. 
            - Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter

        - expressions vs statements

            - In Python, a distinction between expressions and statements is rigidly enforced, which leads to duplicating some functionality.

                - List comprehensions vs. for-loops
                - Conditional expressions vs. if blocks
                - The eval() vs. exec() built-in functions (in Python 2, exec is a statement); the former is for expressions, the latter is for statements.

                - statements cannot be a part of an expression
                - list and other comprehensions or lambda expressions, all being expressions, cannot contain statements
                - a particular case of this is that an assignment statement such as a = 1 cannot form part of the conditional expression of a conditional statement (if a = 1)

        - variable assignment

            - x = 2, translates to "(generic) name x receives a reference to a separate, dynamically allocated object of numeric (int) type of value 2." This is termed binding the name to the object. Since the name's storage location doesn't contain the indicated value, it is improper to call it a variable. Names may be subsequently rebound at any time to objects of greatly varying types, including strings, procedures, complex objects with data and methods, etc. Successive assignments of a common value to multiple names, e.g., x = 2; y = 2; z = 2 result in allocating storage to (at most) three names and one numeric object, to which all three names are bound. Since a name is a generic reference holder it is unreasonable to associate a fixed data type with it. However at a given time a name will be bound to some object, which will have a type; thus there is dynamic typing.

        - variable persistence (shallow copy, reference)

            - variables are names (references to storage locations), not a copy of the information
            - to create a copy in python:
                - you can redefine it (such as if its a list, using a list comprehension)

        - sequence unpacking
            - Python features sequence unpacking wherein multiple expressions, each evaluating to anything that can be assigned to (a variable, a writable property, etc.), are associated in the identical manner to that forming tuple literals and, as a whole, are put on the left hand side of the equal sign in an assignment statement
            - the statement expects an iterable object on the right hand side of the equal sign that produces the same number of values as the provided writable expressions when iterated through, and will iterate through it, assigning each of the produced values to the corresponding expression on the left


    - basic terms & rules

        - ternary "x if c else y"
        - while: executes a block of code as long as its condition is true
            factorial = 1
            i = 2
            while i <= 10:
                factorial = factorial * i
                i += 1

        - try: allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in a finally block will always be run regardless of how the block exits.
        - raise: raise a specified exception or re-raise a caught exception
            if n < 0:
                raise ValueError('You must enter a positive number')
        - class: executes a block of code and attaches its local namespace to a class
            - Python methods have an explicit self parameter to access instance data
            - the syntax instance.method(argument) is, for normal methods and functions, syntactic sugar for Class.method(instance, argument)
        - with: encloses a code block within a context manager
            - for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it
            - allows Resource Acquisition Is Initialization (RAII)-like behavior and replaces a common try/finally idiom
        - break: exits from the loop
        - continue: skips this iteration and continues with the next item
        - pass: serves as a NOP & is needed to create an empty code block
        - assert: used during debugging to check for conditions that ought to apply
        - yield: returns a value from a generator function. From Python 2.5, yield is also an operator. This form is used to implement coroutines.
        - import: used to import modules whose functions or variables can be used in the current program
            - import <module name> [as <alias>]
            - from <module name> import *
            - from <module name> import <definition 1> [as <alias 1>], <definition 2> [as <alias 2>]
        - try/except: for isolating non-essential errors so they dont interrupt execution - try one line that can fail at a time
        - coroutine: for suspending & resuming operation (related to synchronous operations)
        - list/generator comprehension: x = [ a for a in otherlist]
        - equivalence checks:
            - In Python, == compares by value, versus Java, which compares numerics by value and objects by reference
            - Python's is operator may be used to compare object identities (comparison by reference)
            - In Python, comparisons may be chained, for example a <= b <= c.
        - anonymous functions:
            - Anonymous functions are implemented using lambda expressions; however, these are limited in that the body can only be one expression


- testing

    - process debugging
          - terminal/bash: 
            - tracing probe markers: DTrace, SystemTap

          - python
            - sys.settrace(tracefunction) # trace a function
            - pdb.set_trace() # start tracing
            - traceback.print_exc() # print exception stack trace

        - code debugging
          - python
            - pdb:  python -m pdb script.py

          - exception debugging
            - python
              - printing stack trace
                  except: 
                      traceback.print_exc()

    - linting: 
        - 'pylint script.py'

    - security:
        - bandit -r script

    - coverage
        - with tests: 
            coverage run -m pytest
            coverage run -m unittest discover

    - doc test

          test embedded tests in docstrings with doctest.testmod
            import doctest
            doctest.testmod()

    - unit:

        - nose: 'python -m nose2'

        - pytest: 'pytest'
            - supports assert, filters test cases, can re-run from last failing test rather than start
            - assert sum([1, 2, 3]) == 6, "Should be 6"

        - unittest: 'python -m unittest test' or unittest.main()

        import unittest
        # unittest will test all the methods whose name starts with 'test'

        class SampleTest(unittest.TestCase):
           def test(self):
              self.assertTrue(True)
              self.assertEqual(1 in [0,1,2], True)
              with self.assertRaises(ZeroDivisionError):
                average([])

        if __name__ == '__main__':  
            unittest.main()

- compilation
    - when speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. 
    - Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter

- types: 

    - type Checking
        - Adding type hints like this has no runtime effect: they are only hints and are not enforced on their own
        - mypy & pycharm do static type checking that can catch type errors from type hints
            - mypy script.py

    - type hints
        from typing import Annotated
        def speed(
            distance: Annotated[float, "feet"], time: Annotated[float, "seconds"]
        ) -> Annotated[float, "miles per hour"]:


        - types impact variable assignment, return values and function calling

            - from Python 3.5, the syntax of the language allows specifying static types but they are not checked in the default implementation, CPython
            - An experimental optional static type checker named mypy supports compile-time type checking

            - strong (compile time type checking) vs weakly/loosely typed (may convert types at runtime)
            - dynamic (runtime type safety checking) vs static typed (source code type safety checking)
            - duck typing: evaluating allowed/possible behavior at runtime

            - Python uses duck typing and has typed objects but untyped variable names. 
            - Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that the given object is not of a suitable type. 
            - Despite being dynamically typed, Python is strongly typed, forbidding operations that are not well-defined (for example, adding a number to a string)

            - immutable types:

                - bool

                - str: A character string: sequence of Unicode codepoints 
                    - "Wikipedia"
                    - """Spanning
                    multiple
                    lines"""

                    - string formatting

                        - Python has a "string format" operator %. 
                            - This functions analogous to printf format strings in C

                            - "spam=%s eggs=%d" % ("blah", 2)
                                - evaluates to: "spam=blah eggs=2"

                            - In Python 3 and 2.6+, this was supplemented by the format() method of the str class:
                                - "spam={0} eggs={1}".format("blah", 2) 

                            - Python 3.6 added "f-strings": 
                                - blah = "blah"; eggs = 2; f'spam={blah} eggs={eggs}'

                        - Python has various kinds of string literals:

                            - Strings delimited by single or double quote marks. 
                                - Unlike in Unix shells, Perl and Perl-influenced languages, single quote marks and double quote marks function identically. 
                                - Both kinds of string use the backslash (\) as an escape character. 
                                - String interpolation became available in Python 3.6 as "formatted string literals"
                            - Triple-quoted strings, which begin and end with a series of three single or double quote marks. 
                                - They may span multiple lines and function like here documents in shells, Perl and Ruby
                            - Raw string varieties, denoted by prefixing the string literal with an r. 
                                - Escape sequences are not interpreted; hence raw strings are useful where literal backslashes are common, such as regular expressions and Windows-style paths

                - tuple: Can contain mixed types 
                    - (4.0, 'string', True)
                    - ('single element',)
                    - ()

                    Python makes a distinction between lists and tuples. Lists are written as [1, 2, 3], are mutable, and cannot be used as the keys of dictionaries (dictionary keys must be immutable in Python)
                    Tuples are written as (1, 2, 3), are immutable and thus can be used as the keys of dictionaries, provided all elements of the tuple are immutable
                    The + operator can be used to concatenate two tuples, which does not directly modify their contents, but rather produces a new tuple containing the elements of both provided tuples
                    Thus, given the variable t initially equal to (1, 2, 3), executing t = t + (4, 5) first evaluates t + (4, 5), which yields (1, 2, 3, 4, 5), which is then assigned back to t, thereby effectively "modifying the contents" of t, while conforming to the immutable nature of tuple objects
                    Parentheses are optional for tuples in unambiguous contexts

                - bytes: sequence of bytes:
                    - b"Some ASCII"
                    - bytes([119, 105, 107, 105])

                - complex: 3+2.7j

                - float: Double precision floating point number. The precision is machine dependent but in practice is 64 bits.
                    - 3.1415927
                - ellipses: An ellipsis placeholder to be used as an index in NumPy arrays, not accessible by name
                    - ...
                    - Ellipsis

                - frozenset: Unordered set, contains no duplicates; can contain mixed types, if hashable 
                    - frozenset([4.0, 'string', True])

                - NoneType: absence of a value
                    - None

                - NotImplementedType: A placeholder that can be returned from overloaded operators to indicate unsupported operand types
                    - NotImplemented

                - range: A Sequence of numbers commonly used for looping specific number of times in for loops
                    - range(10, -5, -2)

            - mutable types:
                - dict: keys must be a hashable type 
                - list
                - set: Unordered set, contains no duplicates; can contain mixed types, if hashable 
                    - {4.0, 'string', True}
                    - set()

                - bytearray: sequence of bytes:
                    - bytearray(b"Some ASCII")
                    - bytearray([119, 105, 107, 105])

            - number types:
                - float (real number)
                - int (integer)
                - complex

            - immutable & mutable types:
                Immutable means the state cannot be modified after creation. Examples are: int, float, bool, string and tuple.
                Mutable means the state can be modified after creation. Examples are list, dict, set, & bytearray

            - other data types

                        - bytearray: sequence of bytes:
                            - bytearray(b"Some ASCII")
                            - bytearray([119, 105, 107, 105])

                        - bytes: sequence of bytes:
                            - b"Some ASCII"
                            - bytes([119, 105, 107, 105])

                        - complex: 3+2.7j

                        - float: Double precision floating point number. The precision is machine dependent but in practice is 64 bits.
                            - 3.1415927
                        - ellipses: An ellipsis placeholder to be used as an index in NumPy arrays, not accessible by name
                            - ...
                            - Ellipsis

                        - frozenset: Unordered set, contains no duplicates; can contain mixed types, if hashable 
                            - frozenset([4.0, 'string', True])

                        - NoneType: absence of a value
                            - None

                        - NotImplementedType: A placeholder that can be returned from overloaded operators to indicate unsupported operand types
                            - NotImplemented

                        - range: A Sequen

- operators

    - basic math operations:

            - Addition, subtraction, and multiplication are the same, but the behavior of division differs. 
            - There are two types of divisions in Python. They are floor division (or integer division) // and floating point/division

            - Python has the usual symbols for arithmetic operators (+, -, *, /), and the remainder operator % (where the remainder can be negative, e.g. 4 % -3 == -2)
                - It also has ** for exponentiation, e.g. 5**3 == 125 and 9**0.5 == 3.0, and a matrix multiply @ operator.
                - These operators work like in traditional math; with the same precedence rules, the operators infix ( + and - can also be unary to represent positive and negative numbers respectively)
                - Additionally, it has a unary operator (~), which essentially inverts all the bits of its one argument
                - For integers, this means ~x=-x-1
                - Other operators include bitwise shift operators x << y, which shifts x to the left y places, the same as x*(2**y) , and x >> y, which shifts x to the right y places, the same as x//(2**y)

            - The behavior of division has changed significantly over time so that division between integers produces floating point results

                Python 2.1 and earlier use the C division behavior. The / operator is integer division if both operands are integers, and floating-point division otherwise. Integer division rounds towards 0, e.g. 7/3 == 2 and -7/3 == -2.
                Python 2.2 changes integer division to round towards negative infinity, e.g. 7/3 == 2 and -7/3 == -3. The floor division // operator is introduced. So 7//3 == 2, -7//3 == -3, 7.5//3 == 2.0 and -7.5//3 == -3.0. Adding from __future__ import division causes a module to use Python 3.0 rules for division (see next).
                Python 3.0 changes / to always be floating-point division, e.g. 5/2 == 2.5.

            - In Python terms, / before version 3.0 is classic division, / in versions 3.0 and higher is true division, and // is floor division.

            - Rounding towards negative infinity, though different from most languages, adds consistency
                - For instance, it means that the equation (a + b)//b == a//b + 1 is always true
                - It also means that the equation b*(a//b) + a%b == a is valid for both positive and negative values of a
                - However, maintaining the validity of this equation means that while the result of a%b is, as expected, in the half-open interval [0, b), where b is a positive integer, it has to lie in the interval (b, 0] when b is negative

            - Python provides a round function for rounding a float to the nearest integer. For tie-breaking, versions before 3 use round-away-from-zero: round(0.5) is 1.0, round(-0.5) is −1.0
            - Python 3 uses round to even: round(1.5) is 2, round(2.5) is 2

            - Python allows boolean expressions with multiple equality relations in a manner that is consistent with general use in mathematics
                - For example, the expression a < b < c tests whether a is less than b and b is less than c

            - C-derived languages interpret this expression differently: in C, the expression would first evaluate a < b, resulting in 0 or 1, and that result would then be compared with c

            - Python has extensive built-in support for arbitrary-precision arithmetic
            - Integers are transparently switched from the machine-supported maximum fixed-precision (usually 32 or 64 bits), belonging to the python type int, to arbitrary precision, belonging to the Python type long, where needed
            - The latter have an "L" suffix in their textual representation
            - In Python 3, the distinction between the int and long types was eliminated; this behavior is now entirely contained by the int class
            - The Decimal type/class in module decimal (since version 2.4) provides decimal floating point numbers to arbitrary precision and several rounding modes
            - The Fraction type in module fractions (since version 2.6) provides arbitrary precision for rational numbers 

        - operators:

            - Python also added the ** operator for exponentiation.
            - From Python 3.5, the new @ infix operator was introduced. It is intended to be used by libraries such as NumPy for matrix multiplication
            - From Python 3.8, the syntax :=, called the 'walrus operator' was introduced. It assigns values to variables as part of a larger expression

        - integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float
        - operators with mixed type operands convert the integer operand to floating point
        - division always returns a floating point number: 17 / 3 = 5.6667
            - floor division to get an integer result: 17 // 3 = 5
            - calculate the remainder: 17 % 3 = 2
        - exponents: x ** 2 is x squared
        - while and if statements can contain any operators, not just comparisons
        - numerical operators: <, >, <=, >=
            - comparison operators: is (check if same object), in (check if value in sequence)
                - boolean operators: and, or, not 
                    - 'not' has the highest priority and 'or' the lowest: A and not B or C == (A and (not B)) or C
                - 'and' and 'or' are short-circuit operators, whose evaluation stops as soon as the outcome is determined
                    - if A and C are true but B is false, A and B and C does not evaluate the expression C
        - assignment inside expressions must be done with the walrus operator :=
        - sequences are compared based on left to right ordering, one pair at a time:
            - [1, 3] is less than [1, 4]
            - [1, 3] is less than [1, 3, -1] because of the length


- debugging

    - sys.settrace(tracefunction) # trace a function
    - pdb.set_trace() # start tracing
    - except: 
        traceback.print_exc() # print exception stack trace
    - tracing probe markers with DTrace or SystemTap script on CPython implementation
    - pdb:  python -m pdb script.py

- accessing web resources

    from urllib.request import urlopen
    with urlopen(url) as response:
        for line in response:

- check variable

        - var1 is var2:
            if var1 points to the same object as var2

        - exists: 
            if 'var1' in locals() or 'var1' in globals():

        - is none:
            if var1 is None:

        - is true: 
            if var1 is True:

        - is not false or 0: 
            if var1:

        - object has an attribute: 
            if hasattr(obj, 'attr1'):
            'attr1' in dir(obj) 

- memory
    - Python uses its private heap space to manage the memory. 
        Basically, all the objects and data structures are stored in the private heap space. 
        Even the programmer can not access this private space as the interpreter takes care of this space. 
        Python also has an inbuilt garbage collector, which recycles all the unused memory, freeing the memory for the heap space.
    - Python’s memory allocation/deallocation is automatic
    - Python uses two strategies for memory allocation:
        - Reference counting: When the reference count becomes zero, the object is deallocated
        - Garbage collection:  Python schedules garbage collection based upon a threshold of object allocations/deallocations. 
            - When the number of allocations minus the number of deallocations is greater than the threshold number, the garbage collector is run
    - reference counting for most objects
    - garbage collection to eliminate cycles
    - memory is freed shortly after the last reference to it has been eliminated
    - to track objects only during usage, use weakref to avoid creating a reference, so its automatically removed from the weakref table & calls the weakref callback (ie, for caching)
    - garbage collector, which recycles unused memory so that it can be available to the heap space
    - on exit:
        Whenever Python exits (especially Python modules with circular object references, or objects referenced from the global namespaces) are not always de-allocated or freed.
        It is impossible to de-allocate those portions of memory that are reserved by the C library.
        On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other object.

- PEP 8 is a Python style guide

- Python is a partially compiled language and partially interpreted language. 
    - The compilation part is done first on execution, which generates byte code
    - internally this byte code gets converted by the python vm according to the platform (machine & os)
    - An interpreted language is any programming language which is not in machine level code before runtime

- Pickling is the go-to method of serializing and unserializing objects in Python
    - store: pickle.dump(obj, f)
    - load: loaded_obj = pickle.load(f)

- ORMs (object relational mapping):
    - map data models (usually in an app) to database tables and simplifies database transactions.
    - SQLAlchemy is typically used in the context of Flask, and Django has it’s own ORM.

- condition checking
    - Any takes a sequence and returns true if any element in the sequence is true: any(list1) = True if any item in list1 is true
    - All returns true only if all elements in the sequence are true: all(list1) = True if all items in list1 are true

- module vs. package
    - A module is a file (or collection of files) that can be imported together: import sklearn
    - A package is a namespace directory containing multiple module files
    - So packages are modules, but not all modules are packages.
    - from M import * does not import objects whose name starts with an underscore (internal methods)
        - single/double underscore prefix mimics protected/private access specifiers
    - name mangling: inside class FooBar, attribute '__boo' becomes '_FooBar__boo'
    - “magic” objects or attributes that live in user-controlled namespaces. E.g. __init__, __import__ or __file__.
        - The __init__ method is called automatically whenever a new object/class instance is initiated to allocate memory

- pass vs. continue vs. break
    - pass means do nothing, used to fill an otherwise empty class, function or if-statement
    - continue halts execution for the current element, and continues to the next element in the loop
    - break breaks the loop and the sequence is not longer iterated over

- args vs. kwargs:
    *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 
    **kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments

    - parameters are passed using call by value (where the value is an object reference, not the value of the object)

        - optional args have default values to the right of the required args
        - non-keyword arguments cant be passed after a keyword/named argument
        - arg order doesnt matter even with required args
        - defaults are executed once in consecutive calls, unless assigned a value of None as default
        - *args is a tuple of the positional optional arguments after the required argument or can store any arguments after the preceding formal parameters
        - **keywords generates a dict of the keyword/named arguments, in the order they were passed
        - *args must be before **keywords
        - named args cant be keys in **keywords dict without positional delimiter /
        - def f(positional, /, positional_or_keyword, *, keyword): # separates positional args, positional & keyword args, and keyword args for clarity

        - pass sequence of positional arguments to a function: range(*args)
        - pass dict of keyword arguments to a function: print_dict(**d)

        - function annotations about types:
            def f(var1: str, var2: str = 'default') -> str:


- reference vs. shallow copy vs. deep copy:

    - reference: after setting a var equal to another variable, updating the original variable will appear to update the new variable, bc they point to the same object
        li1 = [['a'],['b'],['c']]
        li2 = li1.append(['d'])
        print(li2) # [['a'], ['b'], ['c'], ['d']]

    - shallow copy:
        - li2 = list(li1)
        - li2 = li1.copy()

        - shallow copies create a new object containing references to the original object
        - new attributes or items added wont propagate to the new object, but changing the original items/attributes (that already existed at copy time) 
            of the original object will propagate the changes to the new object

    - deep copy: creates two independent objects
        import copy
        li5 = [['a'],['b'],['c']]
        li6 = copy.deepcopy(li5)

    - shallow copy: in python, assignments dont actually copy objects, they create a binding between an object & target, so changes are reflected in both objects
    - for mutable objects, an actual (deep) copy may be created so one may be changed without changing the other


- Does python call by reference or call by value?

    - Everything in Python is an object and all variables hold references to the objects. 
    The reference values are according to the functions; as a result, you cannot change the value of the references. However, you can change the objects if it is mutable

    - all names call by reference, but:
        - some memory locations hold objects, and
        - other memory locations hold pointers to other memory locations

    - example: if you delete x, the x name is removed, but y and z still point to the 'some text' object
        x = 'some text'
        y = x
        x is y #=> True
        del x # this deletes the 'x' name but does nothing to the object in memory
        z = y
        y is z #=> True

    - example: if you modify the object, it creates a new object to hold the new version creating a new name that is the same name, and the original object & pointer to it is unchanged
        def add_chars(str1):
            # new name, same object
            str2 = str1
            # creates a new name (with same name as the first) AND object
            str1 += 's' 

- monkey patch only refers to dynamic modifications of a class or module at run-time, like replacing a function with another

- class usage

    - Self refers to the instance of the class itself, enabling methods to access & set attributes of the object (class instance)
        In Python, this is explicitly included as the first parameter. However, this is not the case in Java where it’s optional.  
        It helps to differentiate between the methods and attributes of a class with local variables.
        ***
        The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called.

    - make a new class Audi that inherits a class Car by passing it as a param to the new class Audi:
        class Audi(Car):
            pass

    class Car :
        def __init__(self, color, speed):
            ''' executed on instantiating a car object '''
            self.color = color
            self.speed = speed

    car = Car('red','100mph')
    car.speed # set to '100mph' on instantiation

- oop method types

    Instance methods : accept self parameter and relate to a specific instance of the class.
    Static methods : use @staticmethod decorator, are not related to a specific instance, and are self-contained (don’t modify class or instance attributes)
    Class methods : accept cls parameter and can modify the class itself

    class CoffeeShop:
        specialty = 'espresso'
        
        def __init__(self, coffee_price):
            self.coffee_price = coffee_price
        
        # instance method
        def make_coffee(self):
            print(f'Making {self.specialty} for ${self.coffee_price}')
        
        # static method    
        @staticmethod
        def check_weather():
            print('Its sunny')    # class method

        @classmethod
        def change_specialty(cls, specialty):
            cls.specialty = specialty


- equivalence checks:
            - is checks identity and == checks equality

            - In Python, == compares by value, versus Java, which compares numerics by value and objects by reference
            - Python's is operator may be used to compare object identities (comparison by reference)
            - In Python, comparisons may be chained, for example a <= b <= c.

- with: encloses a code block within a context manager
            - for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it
            - allows Resource Acquisition Is Initialization (RAII)-like behavior and replaces a common try/finally idiom
        

- call function by name:

    import module_name
    result = getattr(module_name, 'function_name')()



- interpolation 
    print("%15.5f, %15.5f" %(pz,pt))
    print("%s %s" %('Hello','World',))
    print('Hello %s! This is %s.'%(name,program))
    print(‘Hello %(name)s! This is %(program)s.’%(name,program))
    #% takes only one argument, so the arguments have to be in a tuple ()
    #format() is an alternative to %:
    print('Hello, {}'.format(name))
    print('Hello {name}!This is{program}.'.format(name=name,program=program))
    #Template strings are another alternative:
    from string import Template
    new = Template('Hello $name! This is $program.')
    print(new.substitute(name= name,program=program))
    #3.6 has literal strings to use variable names, and even execute operations inside brackets
    print(f'Hello {name}! This is {program}')
    print(f'12 multiply 3 is {a * b}.')

                - format(input, format)
                    format(math.pi, '.2f') = '3.14'

                - "%(var1)s" % dict
                    '%(var1)s' % {'var1': "Python"} # s specifies string type

                - str.format(expr_or_vars)
                    "{int1}".format(expression_for_n)
                    "{0}".format(1+2)
                    '{0} = {1}'.format(var1, var2)

                - f""
                    f"{var1!expression_key}" == f"{expression(var1)}"
                    f"{var1!r}." == f"{repr(var1)}."

                - f"{expr}"
                    f"{var1:{type_arg1}.{type_arg2}}" 
                    var1 = decimal.Decimal("12.34567")
                    f" {var1:{width}.{precision}}" # nested field example

                - f"{var1:format}"
                    var1 = 1024
                    f"{var1:#0x}" = '0x400' # uses format specifier
- random
    - random.randrange(start, stop, step)
    - random.random() for random float between 0 inclusive and 1
    - choice(sequence) for random item in sequence


- decorator

    - log_function_called() executes some code (print(f'{func} called.')) before calling the function func() passed in. Then it return the inner code-prepending function it defined
        def logging(func):
          def log_function_called():
            print(f'{func} called.')
            func()
          return log_function_called

        @logging
        def new_function():
            print('this will be executed after printing "new_function called" in log_function_called()')

        ''' is the same as:
        log_function_called(new_function)
        def new_function():
            print('this will be executed after printing "new_function called" in log_function_called()')
        '''

- string multiplication: 'cat' * 3 = 'catcatcat'
- concatenate numpy arrays: 
    import numpy as np
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    np.concatenate((a,b)) # array([1, 2, 3, 4, 5, 6])
- list multiplication: [1,2,3] * 2 == [1, 2, 3, 1, 2, 3]
- list addition: [1,2] + [3,4,5] == [1, 2, 3, 4, 5]

- index gives first occurrence position by default

- list.insert(index, obj) 

- list.remove(obj)

- cmp(list1, list2) to compare two lists


- returns a new list or iterator
    - sorted
        - Python uses Tim Sort algorithm for sorting. It’s a stable sorting whose worst case is O(N log N). 
        It’s a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data
        - "sort" a dictionary, returning a sorted list of key-value tuples: sorted(dictionary.items())
        - sorted returns a new list built from an iterable
        - Sorts are guaranteed to be stable. That means that when multiple records have the same key, their original order is preserved.

    - reversed
        - returns a reversed iterator object
        
- list methods: do not return a new list, it changes the original list:
    - list1.reverse(): li.reverse() 
    - list1.append: list1.append(1) # modifies list, doesnt return new list
    - list1.extend: list1.extend([1,2]) # modifies list, doesnt return new list
    - list1.sort(): 
        - uses timsort: First sort small pieces using Insertion Sort, then merges the pieces using merge of merge sort.
        - does not alter the iterable that is passed, but returns a new iterable which is sorted form of the iterable passed in the function.


- round: round(5.12345,3) == 5.123

- repr(object): generates str representation of an object or one that would generate the same object if passed to eval()


- slice: list[start:stop:step_interval]

    - Slices take elements from the start index up to, but not including, the stop index. 
     - The third slice parameter, called step or stride, allows elements to be skipped and reversed. 
     - Slice indexes may be omitted, for example a[:] returns a copy of the entire list. 
     - Each element of a slice is a shallow copy

    - everything except last char: var[:-1]
    - reverse var[::-1]
    - a[:2] == [a[0] ... a[2 - 1]] # up to but not including 2
    - a[8:] == [a[8] ...]] # including 8, to & including the end
    - a[2:8] == [a[2] ... a[8 - 1]] # up to but not including 8
    - a[2:8:2] == [a[2] ... a[8 - 2]] # up to but not including last digit, a[8 - 1], which is skipped by the step interval

            - Slices take elements from the start index up to, but not including, the stop index. 
            - The third slice parameter, called step or stride, allows elements to be skipped and reversed. 
            - Slice indexes may be omitted, for example a[:] returns a copy of the entire list. 
            - Each element of a slice is a shallow copy

                a[-1]      # last item in the array
                a[-2:]     # last two items in the array
                a[2:]      # everything after first two items
                a[:2]      # first two items
                a[:-2]     # everything except the last two items

                a[::-1]    # all items in the array, reversed
                a[1::-1]   # the first two items, reversed
                a[:-3:-1]  # the last two items, reversed
                a[-3::-1]  # everything except the last two items, reversed



- to pass a function as an argument, use function_name, as opposed to calling with function_name()

- tuple (immutable) = ()
    - can contain mutable objects like lists
    - accessed with sequence unpacking rather than iterating

- Tuple comprehension is not possible in Python because it will end up in a generator, not a tuple comprehension.
- A lambda function is an anonymous function. This function can have any number of parameters but, can have just one statement
    lambda x, y : x + y

- list comprehensions: map(lambda x: x**2, sequence)

    - consist of brackets around [an expression, then a for clause, then possibly more for or if clauses], resulting in a list
    - the expressions can be complex & can contain nested functions 
    - the order of operations in a list comprehension is the same as it would be in a loop
    - use when you want a list thats had a function applied to its sequence items or iterable, or is a subset of a sequence satisfying a condition rather than loops:
        squares = []
        for x in range(10):
            squares.append(x**2)

    list comprehensions are faster:
        squares = [x**2 for x in range(10)]
                = map(lambda x: x**2, range(10))

    this creates a list of tuples:
        list_of_tuples = [(x, y) for x in [1] for y in [3,4] if x != y] #[(1, 3), (1, 4)]

    this transposes rows & columns of a matrix (list of lists):
    matrix = [
        [1, 2, 3],
        [7, 8, 9],
    ]
    [[row[i] for row in matrix] for i in range(2)] #[ [1,7], [2,8], [3,9] ]


- ternary: 
    a if condition else b

- dictionary comprehension 
    d = {k:v for k,v in alphabet.items()} 

- list comprehension with condition
    [e for x in y if c]
    list(filter(lambda x: c, map(lambda x: e, y)))

- ternary expression
    [x if x % 2 == 0 else None for x in range(10)]
    
- ternary expression in list comprehension with condition:
    [x if x > 2 else '*' for x in range(10) if x % 2 == 0]

- exceptions

    try:
        # try this (monitor for errors)
    except:
        # if try block fails (executed when error occurs)
    else:
        # if try block succeeds (no exception), execute this as an alternate to the exception
    finally:
        # always do this
        # Finally block is used to do the required cleanup activities of objects/variables.

    - "except NameError, err:" became "except NameError as err:"
    - the else part of try-except-else is executed when no exception occurs

- division
    - integer division: 3 / 2 = 1.5 (float)
    - floor division: 3 // 2 = 1
    - Floor divisions are NOT integer divisions. A floor division will return -2 for -3 / 2, while an integer division should return -1

- strings: 
    - strings are unicode by default in python 3,
    - python3 has byte & bytearray data types
    - binary: bin(5) == '0b101'
    - remove all whitespace: ''.join(s.split()) # faster without creating new list: s.replace(' ', '')
    - '123a'.isnumeric() == False
    - '123a'.isalpha() == False
    - '123abc'.isalnum() == True

- dict keys as list: 
    - dictionary.keys()
    - [k for k, v in dictionary.items()]
    - list(dictionary)

- The dir() function is used to display the defined symbols.
- help() function is used to display the documentation string

- remove, del, pop:
    - remove() remove the first matching value: list1.remove('itemname')
    - del removes an element by index: del list1[0]
    - pop() removes an element by index and returns that element: list1.pop(5) == list1[5], removing list1[5] from list1 in the process

- xrange:
    - python 3 implements the faster xrange by default as the range function, otherwise in 2.7 specifying xrange is faster
        range() – This returns a list of numbers created using range() function.
        xrange() – This function returns the generator object that can be used to display numbers only by looping.
        The only particular range is displayed on demand and hence called lazy evaluation.

- generator vs. iterator

    - Iterators are the collection of items
    - Python iterator implements __itr__ and the next() method to iterate the stored elements

    - generators: Functions that return an iterable set of items using yield
        - example: xrange
        - It does not implements __itr__ and next() method and reduces other overheads as well.
        - The yield keyword pauses the current execution by saving its states and then resumes from the same when required.

    - next
        next(generator)
        generator.next()

    - avoiding for loop nesting

        def iterate_multi(*lists):
            for i in range(min(map(len,lists))):
                yield tuple(v[i] for v in lists)

        for v1, v2, v3 in iterate_multi(list1,list2,list3):
            print(str(v1) + "," + str(v2) + "," + str(v3))

#useful list functions:

- reversed: loop over a reversed sequence
    for i in reversed(this_list):

- del:
    this_list = [0,1,2,3,4]
    del this_list[2:4] #removes items from this_list starting at position 2 and up to but not including 4
    this_list = [0,1,4]

- zip: make a list of tuples, using lists with the same element count
    a = ['a','b','c']
    b = [1,2,3]
    [(k,v) for k,v in zip(a,b)] # [('a', 1), ('b', 2), ('c', 3)]

    - use zip to iterate through lists at the same time:
        for list1_item, list2_item in zip(list1, list2):

    - useful for transposing a matrix
        x = [1, 2, 3]
        y = [4, 5, 6]
        zipped = zip(x, y) #[(1, 4), (2, 5), (3, 6)]
        #to unzip a list, which means getting back the original sequences/iterables from the zipped list of tuples
        x2, y2 = zip(*zipped) #returns x2 = (1, 2, 3) and y2 = (4, 5, 6), so cast to a list to check equivalence with original variables
        x == list(x2) and y == list(y2) #True

filter(function, iterable): iterates over a sequence, adding each item to a new sequence if the function returns true for that item
        def add_three(x):
            if x % 2 == 0:
                return True        
            return False
        li = [1,2,3,4,5,6,7,8]
        [i for i in filter(add_three, li)] # [2,4,6,8]

    # compute a sequence of numbers divisible by 3 or 5:
        def is_divisible_by_3_or_5(x): return x % 3 == 0 or x % 5 == 0

    # filter a sequence based on which sequence items obey the condition determined in the function (return true from the function):
        filter(is_divisible_by_3_or_5, range(2, 10)) #[3, 5, 6, 9]

map(function, iterable): iterates over returned values from applying a function to every element in a sequence
    li = [1,2,3]
    [i for i in map(add_three, li)] # [4,5,6]
    # apply a function to every item in a sequence:
        def cube(x): return x*x*x
        map(cube, range(1, 6)) #[1, 8, 27, 64, 125]

    #pass multiple sequences, so that the number of sequences = the number of arguments in the multiply function being applied
        def multiply(x,y): return x*y
        map(multiply, range(1, 6), range(6, 11)) 

reduce(function, iterable): iterates over a sequence, using output of current operation as input to next operation
    def add_three(x,y):
        return x + y
    li = [1,2,3,5]
    reduce(add_three, li) # 11 = (((1 + 2) + 3) + 5)
    #a starting value in the sequence can be passed as an argument to reduce 
    reduce(add_three, range(1, 5), 0)
    #a sequence of length one would return that value, or an exception if empty
    reduce(add_three, [1]) # = 1


- timer
    #instantiate Timer object from timeit module
    t1 = Timer("test1()", "from __main__ import test1")
    #run operation with Timer object
    t1.timeit(number=1000)
    print("concat operation", t1.timeit(number=1000), "milliseconds")
    #time.time() from time module
    print('start time', time.time())


