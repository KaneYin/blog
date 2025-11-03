# How to define a function

In python, a function is defined using the `def` keyword, followed by a function name and parentheses.

Syntax:
```python
def func_name(parameter):
	do_something
	return return_val
```

Example:
```python
def greet():  
  print("Hello from a function")
```

## Parameter and Arguments
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The terms _parameter_ and _argument_ can be used for the same thing: information that are passed into a function.

> **From a function's perspective:
> 
> A parameter is the variable listed inside the parentheses in the function definition.
> 
> An argument** is the actual value that is sent to the function when it is called.

### Default parameter values
You can assign default values to parameters, If the function is called without an argument, it uses the default value:
```python
def my_function(name = "friend"):  
  print("Hello", name)  
  
my_function("Emil")  
my_function("Tobias")  
my_function()  
my_function("Linus")
```

### Keyword Arguments

You can send arguments with the key= value syntax.
```python
def my_function(animal, name):  
  print("I have a", animal)  
  print("My", animal + "'s name is", name)  
  
my_function(animal = "dog", name = "Buddy")
```

This way, with keyword arguments, the order of the arguments does not matter.

### Positional Arguments

When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:

```python
def my_function(animal, name):  
  print("I have a", animal)  
  print("My", animal + "'s name is", name)  
  
my_function("dog", "Buddy")
```

### Mixing Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call.

However, positional arguments must come before keyword arguments:

```python
def my_function(animal, name, age):  
  print("I have a", age, "year old", animal, "named", name)  
  
my_function("dog", name = "Buddy", age = 5)
```

### Passing different data types
You can send any data type as an argument to a function (string, number, list, dictionary, etc).
The data type will be preserved inside the function:
```python
def my_function(fruits):
	for fruit in fruits:
		print(friut)
		

my_fruits = ["apple", "banana", "cherry"]  
my_function(my_fruits)
```

### Positional only arguments
You can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add `, /` after the arguments:

```python
def my_function(name, /):  
  print("Hello", name)  
  
my_function("Emil")
```

### Keyword only arguments
To specify that a function can have only keyword arguments, add `*,` _before_ the arguments:
```python
def my_function(*, name):  
  print("Hello", name)  
  
my_function(name = "Emil")
```


## Function Names
Function names follow the same rules as variable names in Python:
- A function name must start with a letter or underscore
- A function name can only contain letters, numbers, and underscores
- Function names are case-sensitive

## Return values
Functions can send data back to the code that called them using the `return` statement.

When a function reaches a `return` statement, it stops executing and sends the result back:
```python
def my_function(x, y):
	retrun x+y

result = my_function(5, 3)
print(result)
```
### Returning different data types
Functions can return any data type, including lists, tuples, dictionaries, and more.
```python
def my_function():  
  **return ["apple", "banana", "cherry"]**  
  
fruits = my_function()  
print(fruits[0])  
print(fruits[1])  
print(fruits[2])
```

### None type
If we do not define the return values of a function, the function will return the none by default.
```python
def say():
    print("hi")

result = say()
print(type(result))
```

The program will output the `<class 'NoneType'>`.


## The pass statement
Function definitions cannot be empty. If you need to create a function placeholder without any code, use the `pass` statement:

```python
def my_function():  
  pass
```


# How to call a function
```python
func_name(parameter)
```

We can call the same function multiple times.


# Python \*args and \*\*kwargs
By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

\*args and \*\*kwargs allow functions to accept a unknown number of arguments.
## Arbitrary Arguments - \* args
If you do not know how many arguments will be passed into your function, add a `*` before the parameter name.

This way, the function will receive a _tuple_ of arguments and can access the items accordingly:

```python
def my_function(*kids):  
  print("The youngest child is " + kids[2])  
  
my_function("Emil", "Tobias", "Linus")****
```

### What is \*args?
The `*args` parameter allows a function to accept any number of positional arguments.

Inside the function, `args` becomes a tuple containing all the passed arguments:

```python
def my_function(*args):  
  print("Type:", type(args))  
  print("First argument:", args[0])  
  print("Second argument:", args[1])  
  print("All arguments:", args)  
  
my_function("Emil", "Tobias", "Linus")
```

### Using \ *args with Regular Arguments

We can combine regular parameters with \*args.
Regular parameters must come before \*args.

```python
def my_function(greeting, *names):  
  for name in names:  
    print(greeting, name)  
  
my_function("Hello", "Emil", "Tobias", "Linus")
```

## Arbitrary Keyword Arguments \*\*kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks `**` before the parameter name.

This way, the function will receive a _dictionary_ of arguments and can access the items accordingly:
```python
def my_function(****kid**):  
  print("His last name is " + kid["lname"])  
  
my_function(fname = "Tobias", lname = "Refsnes")
```


### What is \*\*kwargs
The `**kwargs` parameter allows a function to accept any number of keyword arguments.

Inside the function, `kwargs` becomes a dictionary containing all the keyword arguments:


TODO

# Python Scope
A variable is only available from inside the region it is created. This is called **scope**.

## Local Scope
A variable created inside a function belongs to the _local scope_ of that function, and can only be used inside that function. The variable `x` is not available outside the function, but it is available for any function inside the function:

```python
def myfunc():  
  x = 300  
  def myinnerfunc():  
    print(x)  
  myinnerfunc()  
  
myfunc()
```

## Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

```python
x = 300  
  
def myfunc():  
  print(x)  
  
myfunc()  
  
print(x)
```

## Variables with same names inside and outside of function
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
```python
x = 300  
  
def myfunc():  
  x = 200  
  print(x)  
  
myfunc()  
  
print(x)
```

## Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.

The `global` keyword makes the variable global.

```python
def myfunc():  
  global x  
  x = 300  
  
myfunc()  
  
print(x)
```

## Nonlocal keyword

The `nonlocal` keyword is used to work with variables inside nested functions.
The `nonlocal` keyword makes the variable belong to the outer function.

# Python Decorators
Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.
## Basic Decorator
 
```python
# decorator function
def changecase(func):  
  def myinner():  
    return func().upper()  
  return myinner  
  
# define the function that will use the decorator
@changecase  
def myfunction():  
  return "Hello Sally"  
  
print(myfunction())
```

```output
HELLO SALLY
```

By placing `@changecase` directly above the function definition, the function `myfunction` is being "decorated" with the `changecase` function.

The function `changecase` is the decorator.

The function `myfunction` is the function that gets decorated.

## What happened inside the decorator
when we use the `@decorator`, actually it is the same as below:
```python
myfunction = changecase(myfunction)
```

## Why we need decorator
1. 代码复用性：相同的功能可以应用到多个函数上。
2. 不修改原函数：保持原函数的纯净性

## Multiple decorator calls

A decorator can be called multiple times, just place the decorator above the function you want to decorate

```python
def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def myfunction():
    return "hello world"

@changecase
def otherfunction():
    return "I am speed!"

print(myfunction())
print(otherfunction())
```
## Arguments in the decorated function
Function that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

```python
def changecase(func):
	def myinner(x):
		return func(x).upper()
	return myinner
	
@changecase
def myfunction(nam):
	return "Hello " + nam

print(myfunction("John"))
```

