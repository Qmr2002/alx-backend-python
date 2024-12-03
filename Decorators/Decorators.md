### **Python Functions**

**Concept:**  
Functions in Python transform given inputs into outputs or perform actions (side effects). Here's a basic example of a function returning a value based on the input:

```python
def add_one(number):
    return number + 1

# Test the function
result = add_one(2)
print(result)  # Output: 3
```

**Explanation:**  
- `add_one` takes a number as input and returns the number incremented by 1.
- Functions like this return values without side effects.  
  Example of a function with side effects is `print()`:
  ```python
  print("Hello")  # Outputs 'Hello' but returns None.
  ```

---

### **First-Class Functions**

**Concept:**  
Functions in Python are **first-class objects**, meaning they can be assigned to variables, passed as arguments, or returned by other functions.

**Example:**
```python
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

# Test the functions
print(greet_bob(say_hello))   # Output: Hello Bob
print(greet_bob(be_awesome)) # Output: Yo Bob, together we're the awesomest!
```

**Explanation:**  
- `greet_bob` accepts another function as its argument (`say_hello` or `be_awesome`) and calls it with "Bob".
- When you write `greet_bob(say_hello)`, `say_hello` is passed **as a reference** (not executed immediately).
- Adding parentheses, like `say_hello()`, would execute the function and pass its return value instead.

---

### **Inner Functions**

**Concept:**  
Functions can be defined **inside other functions**, creating **local scope** for these inner functions.

**Example:**
```python
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

# Test the function
parent()
```

**Output:**
```
Printing from parent()
Printing from second_child()
Printing from first_child()
```

**Explanation:**
- `first_child` and `second_child` are defined inside `parent` and can only be accessed within `parent`.
- Trying to call `first_child()` outside `parent` will raise an error:
  ```python
  first_child()  # NameError: name 'first_child' is not defined
  ```

---

### **Functions as Return Values**

**Concept:**  
Functions can return other functions, which allows dynamic behavior.

**Example:**
```python
def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child

# Test the function
first = parent(1)
second = parent(2)

print(first)          # Output: <function parent.<locals>.first_child>
print(second)         # Output: <function parent.<locals>.second_child>

print(first())        # Output: Hi, I'm Elias
print(second())       # Output: Call me Ester
```

**Explanation:**  
- `parent` dynamically returns one of its inner functions based on the input.
- The returned function reference (`first` or `second`) can be called later.
- Writing `first()` executes the function `first_child`, returning "Hi, I'm Elias".

**Important Note:**  
- Without parentheses, `first_child` is returned as a reference.
- With parentheses, `first_child()` executes the function and returns its result.

---

### Summary Table

| Feature                  | Example                                                                                  | Output                                               |
|--------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Basic Function**       | `add_one(2)`                                                                             | `3`                                                 |
| **First-Class Functions**| `greet_bob(say_hello)`                                                                   | `Hello Bob`                                         |
| **Inner Functions**      | `parent()` (with calls to `second_child()` and `first_child()`)                          | Prints messages from parent and its children.       |
| **Function Returns**     | `first = parent(1); print(first())`                                                      | `Hi, I'm Elias`                                     |


---


## **What Are Decorators?**
A decorator in Python is a function that takes another function as input and extends or alters its behavior without modifying the original function’s code.

Decorators are built on three core concepts:
1. **Functions as first-class objects** (can be passed around or returned by other functions).
2. **Inner functions** (functions defined within another function).
3. **Higher-order functions** (functions that take other functions as arguments or return them).

---

### **Basic Example of a Decorator**

```python
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)
say_whee()
```

**Output:**
```
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

**Explanation:**
- `decorator(func)` wraps `say_whee` in a new function `wrapper`, which adds behavior before and after calling the original `func()`.
- The redefinition `say_whee = decorator(say_whee)` means `say_whee` now points to the `wrapper()` function.

---

### **Using @ Syntax (Syntactic Sugar)**

Python provides a shorthand to apply a decorator using the `@` symbol:

```python
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

say_whee()
```

**Output:**
```
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

**Explanation:**
- The `@decorator` syntax is equivalent to `say_whee = decorator(say_whee)`.
- It simplifies the process and makes code cleaner.

---

### **Conditional Decorators**

Decorators can modify behavior dynamically, such as only running a function during certain hours:

```python
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            print("Hush, it's nighttime.")
    return wrapper

@not_during_the_night
def say_whee():
    print("Whee!")

say_whee()
```

**Output:**  
If called during the day:
```
Whee!
```

If called at night:
```
Hush, it's nighttime.
```

**Explanation:**  
- The `wrapper()` checks the current hour using `datetime.now().hour`.
- If the time is between 7 AM and 10 PM, it calls the original function; otherwise, it suppresses it.

---

### **Reusing Decorators**

You can create reusable decorators for consistent behavior across multiple functions.  

Example of a decorator that runs a function twice:
```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()
```

**Output:**
```
Whee!
Whee!
```

**Explanation:**
- `do_twice` calls the original function twice within the `wrapper_do_twice`.

---

### **Decorating Functions With Arguments**

If the decorated function takes arguments, you need to use `*args` and `**kwargs` to pass them:

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")
```

**Output:**
```
Hello World
Hello World
```

**Explanation:**
- The `*args` and `**kwargs` allow `wrapper_do_twice` to accept any number of positional and keyword arguments and pass them to `func`.

---

### **Combining Multiple Decorators**

You can stack multiple decorators on a single function:

```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@do_twice
@uppercase
def greet(name):
    return f"Hello {name}"

print(greet("World"))
```

**Output:**
```
HELLO WORLD
HELLO WORLD
```

**Explanation:**
- The `@uppercase` decorator modifies the return value of the function to uppercase.
- The `@do_twice` decorator runs the uppercase-modified function twice.

---

### **Key Points to Remember**
1. **A decorator is a function** that modifies another function’s behavior.
2. **@ Syntax:** Simplifies applying a decorator to a function.
3. **Inner wrapper functions** allow you to add additional logic before or after calling the original function.
4. Use `*args` and `**kwargs` in wrappers to handle functions with arguments.
5. Decorators are reusable and can be stacked to combine effects.

---

### Summary Table

| Feature                        | Example                               | Output                                                                 |
|--------------------------------|---------------------------------------|-----------------------------------------------------------------------|
| **Basic Decorator**            | `@decorator`                         | Prints messages before and after the function call.                   |
| **Conditional Execution**      | `@not_during_the_night`              | Skips function execution during nighttime.                            |
| **Repeating Function Calls**   | `@do_twice`                          | Executes the function twice.                                          |
| **With Arguments**             | `@do_twice` on `greet(name)`         | Passes arguments and executes the function twice.                     |
| **Combining Decorators**       | `@do_twice` + `@uppercase` on greet  | Modifies the result (uppercase) and executes the modified function twice. |



---

### **Another Practical Decorator: Debugging Functions**

Now let’s create a decorator to debug functions by printing their arguments and return values. This is incredibly useful for understanding what’s happening inside your code.

**Code:**

```python
import functools

def debug(func):
    """Print the function signature and return value."""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                     # Represent positional arguments
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] # Represent keyword arguments
        signature = ", ".join(args_repr + kwargs_repr)          # Join all arguments
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)                           # Call the original function
        print(f"{func.__name__!r} returned {value!r}")          # Print the return value
        return value
    return wrapper_debug
```

Here’s how the `@debug` decorator works:

1. It constructs a string representation of the positional and keyword arguments passed to the function.
2. Before the function runs, it prints the function name and arguments.
3. After the function runs, it prints the returned value.

**Example Usage:**

```python
@debug
def make_greeting(name, age=None):
    if age:
        return f"Hi {name}! You are {age} years old."
    else:
        return f"Hi {name}!"

make_greeting("Alice", age=30)
make_greeting("Bob")
```

**Output:**
```
Calling make_greeting('Alice', age=30)
'make_greeting' returned 'Hi Alice! You are 30 years old.'
Calling make_greeting('Bob')
'make_greeting' returned 'Hi Bob!'
```

---

### **Combining Multiple Decorators**

What happens if you want to use multiple decorators on the same function? They stack in the order they are applied, from the closest to the function outward. For example:

```python
@timer
@debug
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])

waste_some_time(5)
```

**Output:**
```
Calling waste_some_time(5)
Finished waste_some_time() in 0.0015 secs
'waste_some_time' returned None
```

Here, the `@debug` decorator logs the function signature and return value, while the `@timer` decorator logs the runtime.

---

### **Using Decorators With Arguments**

Sometimes, decorators need their own arguments. For instance, let’s create a decorator to repeat a function a configurable number of times:

**Code:**

```python
import functools

def repeat(num_times):
    """Repeat the decorated function a number of times."""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
```

**Example Usage:**

```python
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}!")

greet("Alice")
```

**Output:**
```
Hello Alice!
Hello Alice!
Hello Alice!
```

Here’s what happens:

1. `@repeat(num_times=3)` creates a decorator that repeats the function three times.
2. The inner `decorator_repeat` wraps the function and repeats its call.

---

### **Key Takeaways**

- **Return Values**: Always ensure the decorator’s wrapper function returns the decorated function’s return value unless intentionally modifying it.
- **`@functools.wraps`**: Always use `@functools.wraps` to preserve metadata about the original function.
- **Debugging**: Decorators like `@debug` make tracking function calls and returns much easier.
- **Combining**: Multiple decorators can be stacked for layered behavior.
- **Custom Arguments**: Decorators can be parameterized for dynamic functionality.



----


### **Further Enhancements and Practical Examples for Decorators**

Now that you’ve mastered the basics of debugging, timing, and slowing down code using decorators, let’s expand on these ideas and explore more advanced use cases. This section introduces argument-based decorators, caching, and other practical implementations.

---

### **Customizing Decorators With Arguments**

You can modify the `@slow_down` decorator to allow for a variable sleep time. To achieve this, create a decorator that accepts arguments:

**Code:**

```python
import functools
import time

def slow_down(rate=1):
    """Sleep for a given number of seconds before calling the function."""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down
    return decorator_slow_down
```

**Usage:**

```python
@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)
```

**Output:**
```
3
(wait 2 seconds)
2
(wait 2 seconds)
1
(wait 2 seconds)
Liftoff!
```

This version of `@slow_down` introduces flexibility by allowing you to specify the rate as an argument.

---

### **Adding Memoization With Caching**

Caching is a common optimization technique, and decorators make it easy to implement. Here’s how you can create a `@cache` decorator using Python’s built-in `functools.lru_cache`:

**Code:**

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Usage:**

```python
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765
```

The `@functools.lru_cache` decorator automatically caches results for a function, so repeated calls with the same arguments are much faster.

---

### **Advanced Debugging With Timing**

Combine `@debug` and `@timer` to simultaneously track arguments, return values, and execution time:

**Code:**

```python
@debug
@timer
def complex_calculation(x, y):
    time.sleep(0.5)  # Simulate a long calculation
    return x * y + x / y
```

**Usage:**

```python
result = complex_calculation(10, 5)
```

**Output:**
```
Calling complex_calculation(10, 5)
Finished complex_calculation() in 0.5003 secs
'complex_calculation' returned 22.0
```

---

### **Access Control With Decorators**

Use a decorator to enforce access control. For example, you might want to ensure a user has the proper permissions before calling a function:

**Code:**

```python
def requires_permission(permission):
    def decorator_requires_permission(func):
        @functools.wraps(func)
        def wrapper_requires_permission(user, *args, **kwargs):
            if user.get("role") != permission:
                raise PermissionError(f"User does not have {permission} permissions.")
            return func(user, *args, **kwargs)
        return wrapper_requires_permission
    return decorator_requires_permission
```

**Usage:**

```python
@requires_permission("admin")
def delete_user(user, user_to_delete):
    print(f"{user['name']} deleted {user_to_delete}.")

admin_user = {"name": "Alice", "role": "admin"}
guest_user = {"name": "Bob", "role": "guest"}

delete_user(admin_user, "Charlie")  # Works
delete_user(guest_user, "Charlie")  # Raises PermissionError
```

---

### **Handling Recursive Functions With Decorators**

As seen with `@slow_down`, decorators can seamlessly handle recursive functions like the Fibonacci sequence:

**Code:**

```python
@slow_down(rate=0.2)
def fibonacci_recursive(n):
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(5))
```

**Output:**
```
(wait 0.2 seconds for each step)
5
```

The decorator slows down each recursive call, making it easier to observe the flow of execution.

---

### **Key Takeaways**

1. **Parameterized Decorators**: Enhance flexibility by creating decorators that accept arguments, like `@slow_down(rate=2)`.
2. **Combining Decorators**: Stack decorators like `@debug` and `@timer` for more comprehensive tracking.
3. **Caching**: Use `@functools.lru_cache` for performance improvements, especially with recursive functions.
4. **Access Control**: Decorators can enforce user permissions for secure function execution.
5. **Practical Debugging**: Use `@debug` in combination with other decorators to deeply understand function behavior.

---


### Registering Plugins

We will use the decorator to register functions as plugins. These functions can then be dynamically called from a dictionary of registered plugins.

#### Code Example:

```python
# decorators.py
PLUGINS = dict()

def register(func):
    """Register a function as a plugin"""
    PLUGINS[func.__name__] = func
    return func
```

This decorator registers functions into the `PLUGINS` dictionary, using the function's name as the key.

### Applying the Plugin System

You can register functions as plugins using the `@register` decorator. Here’s how to do it:

```python
# main.py
from decorators import register, PLUGINS

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"
```

In this example, two functions, `say_hello` and `be_awesome`, are registered as plugins in the `PLUGINS` dictionary.

#### Output of the `PLUGINS` dictionary:

```python
>>> PLUGINS
{'say_hello': <function say_hello at 0x7f768eae6730>,
 'be_awesome': <function be_awesome at 0x7f768eae67b8>}
```

This shows that both `say_hello` and `be_awesome` functions have been successfully registered in the dictionary.

### Using Registered Plugins

Now, let’s randomly pick a plugin and call it:

```python
import random

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

# Example usage:
>>> randomly_greet("Alice")
Using 'say_hello'
'Hello Alice'
```

**Explanation:**
- The `randomly_greet` function selects a function randomly from the `PLUGINS` dictionary and calls it with the given name.
- The output indicates that the function `say_hello` was chosen, and it returns `"Hello Alice"`.

### Authenticating Users with Flask

A common use case for decorators is user authentication. Here, we will create a `login_required` decorator that ensures the user is logged in before accessing certain routes in a Flask application.

#### Code Example:

```python
# secret_app.py
import functools
from flask import Flask, g, request, redirect, url_for

app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:  # Simulate checking if a user is logged in
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    return "This is a secret page!"
```

**Explanation:**
- The `login_required` decorator checks if `g.user` is `None`, which simulates whether a user is logged in or not.
- If the user is not logged in, they are redirected to the login page.
- If the user is logged in, the decorated function `secret()` is called.

#### Example Output:

When accessing `/secret`, if the user is not logged in:

```python
>>> g.user = None
>>> secret()
Redirecting to /login?next=%2Fsecret
```

If the user is logged in:

```python
>>> g.user = 'Alice'
>>> secret()
'This is a secret page!'
```

### Fancy Decorators: Decorating Classes

Decorators can also be used with classes. Python provides built-in decorators such as `@classmethod`, `@staticmethod`, and `@property`, but you can also define your own custom class decorators.

#### Code Example:

Here’s an example using custom decorators on a class’s methods.

```python
# class_decorators.py
from decorators import debug, timer

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([number**2 for number in range(self.max_num)])
```

**Explanation:**
- The `@debug` decorator logs information about the function calls, and `@timer` measures how long a function takes to execute.

#### Example Output:

```python
>>> from class_decorators import TimeWaster

>>> tw = TimeWaster(1000)
Calling __init__(<time_waster.TimeWaster object at 0x7efccce03908>, 1000)
__init__() returned None

>>> tw.waste_time(999)
Finished waste_time() in 0.3376 secs
```

- When `TimeWaster(1000)` is called, the `@debug` decorator logs the call to `__init__`.
- The `@timer` decorator logs the time it takes to execute `waste_time`.

### Decorating Entire Classes

You can apply decorators to an entire class. For example, the `@dataclass` decorator automatically adds special methods like `__init__`, `__repr__`, etc., to a class.

#### Code Example:

```python
from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str
```

**Explanation:**
- The `@dataclass` decorator automatically generates an `__init__` and `__repr__` method for the `PlayingCard` class.

#### Example Output:

```python
>>> card = PlayingCard("King", "Hearts")
>>> card
PlayingCard(rank='King', suit='Hearts')
```

- The `@dataclass` decorator has automatically provided a useful `__repr__` method for the `PlayingCard` class.

### Nesting Decorators

You can stack multiple decorators on top of each other. Let’s see how the order of decorators affects the result.

#### Code Example:

```python
# decorators.py
def debug(func):
    """Print function call details"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

def do_twice(func):
    """Call the function twice"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
```

Now, let’s apply both `@debug` and `@do_twice` to a function.

#### Code Example:

```python
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```

Here, we apply `@debug` after `@do_twice`. This means that `@debug` will print the details of the call, while `@do_twice` will ensure the function is executed twice.

#### Example Output:

```python
>>> greet("Yadi")
Calling greet(('Yadi',), {})
Hello Yadi
Hello Yadi
greet() returned None
```

Now, let’s change the order:

```python
@do_twice
@debug
def greet(name):
    print(f"Hello {name}")
```

#### Example Output:

```python
>>> greet("Yadi")
Calling greet(('Yadi',), {})
Hello Yadi
Calling greet(('Yadi',), {})
Hello Yadi
greet() returned None
```

- When `@do_twice` is applied first, it causes `greet()` to be called twice. The `@debug` decorator prints the details for each call.

### Conclusion

Decorators provide a powerful mechanism in Python for modifying the behavior of functions and classes. They can be used for various purposes such as:

- Registering plugins dynamically.
- Enforcing authentication in web applications.
- Enhancing classes and methods with additional behavior.
- Stacking multiple decorators to create complex functionality.

----


Let's walk through the implementation of decorators with arguments, covering both the required features and optional arguments. I'll explain the code with the necessary details, including expected behavior and outputs.

### Defining Decorators with Arguments

When you want to pass arguments to a decorator, you need an additional outer function. This allows the decorator to accept arguments before it returns the actual decorator that wraps the function. Here’s how you can implement a `@repeat` decorator that repeats the execution of a function a specified number of times.

### Code Example:

```python
import functools

# Decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)  # Call the decorated function
            return value
        return wrapper_repeat
    return decorator_repeat
```

**Explanation:**
- `repeat(num_times)` is the outer function that takes `num_times` as an argument. This is the number of times the function will be called.
- `decorator_repeat(func)` is the actual decorator function that wraps the original function (`func`) with the logic to repeat the function call.
- `wrapper_repeat(*args, **kwargs)` is the inner function that calls the decorated function multiple times (`num_times`).

### Using the `@repeat` Decorator

Now, you can use the `@repeat` decorator to repeat a function a given number of times. For example:

```python
from decorators import repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

# Output when calling greet
greet("World")
```

**Expected Output:**
```text
Hello World
Hello World
Hello World
Hello World
```

This works as expected: the `greet` function is called four times because `num_times=4` was passed to the `@repeat` decorator.

### Creating Decorators with Optional Arguments

Sometimes, you want to make a decorator that can be used both with and without arguments. This can be accomplished by checking if the decorator was called with arguments or not. If no arguments are provided, the decorator should still work as usual.

We will modify the `@repeat` decorator to handle this case. Here's how to do it:

### Code Example with Optional Arguments:

```python
import functools

# Decorator with optional arguments
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
```

**Explanation:**
- The decorator now checks if it was called with or without arguments by inspecting `_func`.
- If `_func` is `None`, the decorator is called with arguments (like `@repeat(num_times=3)`).
- If `_func` is provided (like `@repeat` with no arguments), it immediately applies the decorator to the function.

### Example Usage:

#### 1. Using `@repeat` with Arguments

```python
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```

**Expected Output:**
```text
Hello Alice
Hello Alice
Hello Alice
```

#### 2. Using `@repeat` without Arguments

```python
@repeat
def say_whee():
    print("Whee!")

say_whee()
```

**Expected Output:**
```text
Whee!
Whee!
```

In this case, the `say_whee` function is called twice because the default value of `num_times` is 2.

### Conclusion

1. **Decorators with Arguments:**
   - We defined a `@repeat` decorator that repeats the execution of a function a specified number of times. The outer function takes the argument (`num_times`), and the inner function wraps the target function.

2. **Decorators with Optional Arguments:**
   - We modified the `@repeat` decorator to allow both cases: using the decorator with or without arguments. If no argument is provided, the default value (`num_times=2`) is used.


---



Let's explore how to track state in decorators by both using function attributes and implementing decorators with classes. These approaches allow us to keep track of the number of times a function is called, or any other stateful behavior.

### 1. **Tracking State in Decorators with Function Attributes**

To track the state (like counting the number of times a function is called), one simple approach is to use function attributes. Here, we’ll create a `@count_calls` decorator that counts how many times a function has been invoked.

### Code Example:

```python
import functools

# Decorator that tracks function calls
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1  # Increment call count
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}()")
        return func(*args, **kwargs)
    
    # Initialize the call count to 0
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
```

**Explanation:**
- `count_calls(func)` is the decorator that takes the function `func` as an argument.
- Inside the wrapper function `wrapper_count_calls`, we increase the `num_calls` attribute each time the function is called. This state is stored directly on the wrapper function.
- The `@functools.wraps(func)` ensures that the decorated function retains its original name and docstring.

### Usage Example:

```python
from decorators import count_calls

@count_calls
def say_whee():
    print("Whee!")

# Call the function multiple times
say_whee()
say_whee()

# Check the number of calls
print(say_whee.num_calls)
```

**Expected Output:**
```text
Call 1 of say_whee()
Whee!
Call 2 of say_whee()
Whee!
2
```

Each time `say_whee` is called, the decorator increments the `num_calls` attribute and prints the current call count. You can also manually access the `num_calls` attribute to see how many times the function has been called.

### 2. **Tracking State with a Class-Based Decorator**

A more flexible way to track state is by using a class. A class can be used as a decorator by implementing the `__call__` method, which allows an instance of the class to be called like a function.

### Code Example with Class:

```python
import functools

# Class-based decorator to count calls
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func  # Store the function
        self.num_calls = 0  # Initialize call count
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1  # Increment call count
        print(f"Call {self.num_calls} of {self.func.__name__}()")
        return self.func(*args, **kwargs)
```

**Explanation:**
- The `CountCalls` class is initialized with the function to be decorated.
- The `__call__` method is called every time the decorated function is invoked, and it increments the call count.
- `functools.update_wrapper(self, func)` is used to ensure that the decorated function retains its original properties (such as name and docstring).

### Usage Example:

```python
from decorators import CountCalls

@CountCalls
def say_whee():
    print("Whee!")

# Call the function multiple times
say_whee()
say_whee()

# Check the number of calls
print(say_whee.num_calls)
```

**Expected Output:**
```text
Call 1 of say_whee()
Whee!
Call 2 of say_whee()
Whee!
2
```

The output is similar to the function-based approach, but now the state (call count) is stored inside the class instance.

### 3. **Comparison and Conclusion**

- **Function Attributes:** This method uses function attributes to store state (such as the number of times a function has been called). It’s simple and works well for small, lightweight decorators.
  
- **Class-Based Decorators:** For more complex decorators that need to manage state or have additional functionality, using a class can be more flexible. The `__call__` method allows a class instance to behave like a function, and you can store state within the class instance itself.

Both methods are useful, and the choice between function attributes and classes depends on the complexity of the decorator and the requirements of your application. For simpler use cases, function attributes are usually sufficient, but for more complex scenarios, class-based decorators offer greater flexibility.



----


In this section, we look at some real-world examples of decorators that are practical for use in different scenarios. These examples cover slowing down code, creating singletons, and caching return values.

### 1. **Slowing Down Code with a Decorator**
A common use case is slowing down code, often for testing purposes (e.g., simulating delays). Previously, a decorator could make a function pause for a fixed duration. Now, we can make it more flexible by adding an optional `rate` parameter that controls the sleep duration.

### Code Example:

```python
import functools
import time

def slow_down(_func=None, *, rate=1):
    """Sleep the given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)
```

**Explanation:**
- The `slow_down` decorator is now configurable via the `rate` parameter, which determines how long to sleep before calling the function.
- The `decorator_slow_down` is nested to handle the optional argument for the decorator.
  
### Usage Example:

```python
from decorators import slow_down

@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)
```

**Output:**
```text
3
(2-second pause)
2
(2-second pause)
1
(2-second pause)
Liftoff!
```

This example adds a two-second pause between each number in the countdown.

---

### 2. **Creating Singletons with a Decorator**
A singleton ensures that only one instance of a class exists. The `@singleton` decorator enforces this by storing the first instance of the class and returning it for all subsequent instantiations.

### Code Example:

```python
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance is None:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton
```

**Explanation:**
- The decorator stores the first instance of the class in `wrapper_singleton.instance` and ensures that any subsequent attempts to create an instance will return the first one.
  
### Usage Example:

```python
from decorators import singleton

@singleton
class TheOne:
    pass

first_one = TheOne()
another_one = TheOne()

print(id(first_one))  # Same memory location
print(id(another_one))  # Same memory location
print(first_one is another_one)  # True
```

**Output:**
```text
140094218762310
140094218762310
True
```

Both `first_one` and `another_one` refer to the same instance, confirming that the class is indeed a singleton.

---

### 3. **Caching Return Values with a Decorator**
Decorators can be used to cache function results, particularly for expensive or recursive computations like calculating Fibonacci numbers. Caching avoids redundant calculations and improves performance.

### Code Example (Basic Cache Decorator):

```python
import functools

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = {}
    return wrapper_cache
```

**Explanation:**
- The `cache` decorator stores previous function results in a dictionary. If the function is called with the same arguments, it retrieves the result from the cache instead of recomputing it.
  
### Usage Example:

```python
from decorators import cache, count_calls

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))
print(fibonacci.num_calls)
```

**Output:**
```text
Call 1 of fibonacci()
...
Call 11 of fibonacci()
55
177
```

The Fibonacci sequence is now computed faster due to caching. The number of calls (`fibonacci.num_calls`) is much lower than it would have been without caching.

### Code Example (Using `functools.lru_cache` for Optimized Caching):

Python's `functools` module provides built-in decorators like `lru_cache` for optimized caching.

```python
import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    if num < 2:
        value = num
    else:
        value = fibonacci(num - 1) + fibonacci(num - 2)
    print(f"Calculated fibonacci({num}) = {value}")
    return value

# Usage
fibonacci(10)
fibonacci(8)
fibonacci(5)
print(fibonacci.cache_info())  # Check cache statistics
```

**Output:**
```text
Calculated fibonacci(10) = 55
Calculated fibonacci(9) = 34
Calculated fibonacci(8) = 21
...
CacheInfo(hits=17, misses=20, maxsize=4, currsize=4)
```

The `lru_cache` with `maxsize=4` stores only the most recent 4 function results, evicting older ones. The cache statistics show how many cache hits and misses occurred during the computation.

---

### Conclusion
- **Slowing Down Code:** The `slow_down` decorator with an optional `rate` argument provides a way to simulate delays in a flexible manner.
- **Singletons:** The `singleton` decorator ensures that a class has only one instance throughout its lifetime, useful for cases like configuration settings or connection pools.
- **Caching:** The `cache` decorator, along with Python's built-in `functools.lru_cache`, helps avoid redundant calculations by storing previously computed results.

These real-world examples show how decorators can be applied in various contexts to improve performance, enforce design patterns like singletons, and manage state.



---



This section presents real-world examples of using decorators to improve code organization and functionality, particularly in Python.

### 1. **Adding Information About Units**
In this example, the decorator `@set_unit` adds a unit attribute to a function. This can be useful when you're performing calculations that should have specific units attached. For example:

```python
def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit
```

In practice, this can be applied to a function like `volume`, which calculates the volume of a cylinder:

```python
@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height
```

After calling `volume(3, 5)`, you can check the `unit` attribute:

```python
print(volume.unit)  # Output: cm^3
```

Using this pattern can be enhanced with libraries like [Pint](https://pint.readthedocs.io/), which allow conversions between different units:

```python
import pint
ureg = pint.UnitRegistry()
vol = volume(3, 5) * ureg(volume.unit)

print(vol.to("cubic inches"))
```

### 2. **Unit Conversion with Pint**
By modifying the decorator to return a `Quantity` object from Pint, you make it easier to handle unit conversions. For example, with a function to calculate speed:

```python
def use_unit(unit):
    """Have a function return a Quantity with the given unit"""
    use_unit.ureg = pint.UnitRegistry()
    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)
        return wrapper_use_unit
    return decorator_use_unit
```

This decorator makes the speed calculation function return values in a specific unit. For example:

```python
@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration
```

With this setup, you can easily convert between units like meters per second, kilometers per hour, or miles per hour.

### 3. **Validating JSON in Flask**
Decorators can also be used to simplify validation in web frameworks like Flask. In this example, the `@validate_json` decorator checks if specific keys are present in a JSON payload:

```python
def validate_json(*expected_args):
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json
```

This allows you to validate JSON data before executing the actual logic of your route handler. For example:

```python
@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database
    return "success!"
```

Here, the `@validate_json` decorator checks that the key `student_id` is present in the request JSON before proceeding with the grade update logic.

---

## All in one 




### Conclusion

In this tutorial, you've explored the concept of decorators and how they can be leveraged in Python to enhance code reusability, readability, and functionality. Let's summarize the key takeaways, with examples for each concept:

### 1. **Understanding Functions as First-Class Citizens**

You started by understanding that functions in Python are first-class objects. This means you can define functions inside other functions, assign them to variables, and pass them around just like any other object. Here’s an example:

```python
def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function

# Calling the outer function and getting the inner function
inner = outer_function()
print(inner())  # Output: Hello from the inner function!
```

### 2. **Introduction to Decorators**

The next step was learning about decorators, which are functions that modify the behavior of other functions or methods. They allow you to add functionality to an existing function without changing its code. For instance, a simple decorator:

```python
def simple_decorator(func):
    def wrapper():
        print("Something before the function call")
        func()
        print("Something after the function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello!")

greet()  
# Output:
# Something before the function call
# Hello!
# Something after the function call
```

### 3. **Reusable Decorators**

You learned that decorators can be reused across different functions. This is particularly useful when you want to apply the same logic to many functions, such as logging or validation.

```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_execution
def add(a, b):
    return a + b

print(add(3, 5))  # Output: Executing add with arguments (3, 5) and {}
# Output: 8
```

### 4. **Using `functools.wraps`**

You saw how `functools.wraps` can be used to ensure that the decorated function maintains its original signature and metadata (like the name and docstring).

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is an example function."""
    pass

print(example.__name__)  # Output: example
print(example.__doc__)  # Output: This is an example function.
```

### 5. **Advanced Decorators**

#### a. **Decorating Classes**

You also learned that decorators can be applied to classes. This is useful when you want to modify the behavior of class methods or instance creation.

```python
def add_method(cls):
    def new_method(self):
        return "This is a new method!"
    
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())  # Output: This is a new method!
```

#### b. **Nesting Decorators**

You saw that decorators can be nested to apply multiple behaviors to a function or class.

```python
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        return func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        return func()
    return wrapper

@decorator_one
@decorator_two
def greet():
    return "Hello!"

greet()
# Output:
# Decorator One
# Decorator Two
# Hello!
```

#### c. **Adding Arguments to Decorators**

You also learned how to pass arguments to decorators. This is useful when you want to customize the behavior of the decorator based on the arguments you provide.

```python
def repeat(n):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!
```

#### d. **Keeping State within Decorators**

You learned that decorators can keep state between calls, which is useful when you want to maintain some kind of internal data or perform tracking.

```python
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} has been called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@counter
def greet():
    print("Hello!")

greet()
greet()
# Output:
# Function greet has been called 1 times.
# Hello!
# Function greet has been called 2 times.
# Hello!
```

#### e. **Using Classes as Decorators**

Finally, you saw that you can also use classes as decorators. A class-based decorator can maintain state across calls and provide more flexibility.

```python
class Decorator:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Function {self.func.__name__} has been called {self.calls} times.")
        return self.func(*args, **kwargs)

@Decorator
def greet():
    print("Hello!")

greet()
greet()
# Output:
# Function greet has been called 1 times.
# Hello!
# Function greet has been called 2 times.
# Hello!
```

### 6. **Summary**
- Decorators are a powerful feature in Python that allow you to modify the behavior of functions and classes in a reusable and elegant way.
- You can use decorators to add pre- and post-processing logic, manage state, and even modify class behavior.
- Decorators can be extended with arguments, nested, or even implemented using classes, making them highly flexible for a variety of use cases.

By mastering decorators, you can write more modular, reusable, and clean code that adheres to the DRY (Don’t Repeat Yourself) principle. You now have the tools to leverage decorators to solve many real-world problems efficiently.