### Advanced Python: Generators Explained with Examples and Outputs

Generators are a powerful feature in Python for creating iterators in a simple, readable way. They allow for **lazy evaluation**—producing values one at a time and only when required—making them ideal for working with large datasets or streams of data.

---

### Key Features of Generators:
1. **Memory Efficiency**: They don’t store all the values in memory; instead, they generate them on the fly.
2. **Lazy Evaluation**: Values are computed as needed, improving performance for large datasets.
3. **Simplified Code**: The `yield` statement makes writing iterators concise and straightforward.

---

### **Generator Functions**
A **generator function** is defined like a normal function, but instead of `return`, it uses `yield` to produce a sequence of values lazily.

#### Example: `firstn` Generator
```python
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Using the generator
for number in firstn(5):
    print(number)
```

**Output**:
```
0
1
2
3
4
```

**Explanation**:
- Each call to `yield` produces the next value of the generator.
- Once `yield` is executed, the state of the function is paused until the next value is requested.

---

### Comparison: List vs Generator

#### **Using a List** (Consumes Memory):
```python
def firstn_list(n):
    return [num for num in range(n)]

# Sum of first 1 million numbers
sum_of_first_n = sum(firstn_list(1_000_000))
```

This approach **creates a list in memory**, which can consume a lot of space for large `n`.

#### **Using a Generator** (Memory-Efficient):
```python
def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Sum of first 1 million numbers
sum_of_first_n = sum(firstn_gen(1_000_000))
```

With the generator, values are **produced on-demand**, using significantly less memory.

---

### **Generator Expressions**
A generator expression is similar to a list comprehension but produces values lazily.

#### Example: Square Numbers
```python
# Generator expression for squares
squares = (x ** 2 for x in range(10))

# Consume the generator
for square in squares:
    print(square)
```

**Output**:
```
0
1
4
9
16
25
36
49
64
81
```

---

### Performance Example: `range` vs Generator

#### Using `range`:
```python
# Creates a list in memory
sum(range(1_000_000))
```

#### Using a Generator:
```python
# Generates numbers on-the-fly
sum(x for x in range(1_000_000))
```

In Python 3, the built-in `range` is implemented as a lazy sequence, making it memory-efficient by default.

---

### **Advanced Examples**

#### **Chaining Generators**
You can combine generators to process data in a pipeline-like fashion.

```python
# Squares of numbers less than 100
from itertools import takewhile

squares = (x ** 2 for x in range(100))
bounded_squares = takewhile(lambda x: x < 50, squares)

print(list(bounded_squares))
```

**Output**:
```
[0, 1, 4, 9, 16, 25, 36, 49]
```

---

#### **Unique Items with a Generator**
Here’s an example of using a generator to filter unique items based on a key.

```python
def unique(iterable, key=lambda x: x):
    seen = set()
    for elem in iterable:
        ekey = key(elem)
        if ekey not in seen:
            yield elem
            seen.add(ekey)

# Example Usage
names = ["Alice", "Bob", "ALICE", "alice", "Bob"]
unique_names = unique(names, key=str.lower)
print(list(unique_names))
```

**Output**:
```
['Alice', 'Bob']
```

---

### Benefits of Generators:
1. **Efficient Iteration**: Only processes data as needed.
2. **Cleaner Code**: No need for custom iterator classes.
3. **Composability**: Generators can be composed for pipelines.

---

This article provides a comprehensive overview of Python's **generators** and the **`yield` statement**, offering practical examples and advanced usage techniques. Here's a summary of the key concepts, examples, and use cases:

---

### **1. What Are Generators?**
Generators are a type of Python function that use the `yield` statement to produce a sequence of values lazily, meaning they compute each value only when needed. Unlike regular functions that return a single value using `return`, generators return an iterator that can be iterated through.

#### **Key Features:**
- Memory-efficient: They do not store all the values in memory.
- Useful for large datasets or infinite sequences.
- Pause their state between iterations.

---

### **2. Practical Examples of Generators**

#### **Example 1: Reading Large Files**
When working with large files, a generator function prevents loading the entire file into memory.

##### Traditional Approach:
```python
def csv_reader(file_name):
    file = open(file_name)
    return file.read().split("\n")  # Loads entire file into memory.
```

This approach can cause a `MemoryError` with very large files.

##### Generator Approach:
```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row  # Lazily returns one row at a time.
```

**Usage:**
```python
csv_gen = csv_reader("large_file.txt")
row_count = sum(1 for _ in csv_gen)
print(f"Row count: {row_count}")
```

This ensures the file is processed row by row, minimizing memory usage.

---

#### **Example 2: Generating an Infinite Sequence**
Generators excel in scenarios where you need an infinite sequence.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

**Usage:**
```python
for i in infinite_sequence():
    print(i, end=" ")  # Outputs numbers indefinitely.
```

This will continue until interrupted manually.

---

#### **Example 3: Detecting Palindromes**
Using a generator to find numeric palindromes in an infinite sequence:

```python
def is_palindrome(num):
    if num < 10:
        return False
    return str(num) == str(num)[::-1]

for i in infinite_sequence():
    if is_palindrome(i):
        print(i)  # Outputs numeric palindromes.
```

---

### **3. Building Generators With Expressions**
Generators can be created using **generator expressions**, which have a syntax similar to list comprehensions but use parentheses instead of square brackets.

**Example:**
```python
csv_gen = (row for row in open("file.txt"))
```

This creates a generator without explicitly defining a function.

---

### **4. Advanced Generator Methods**

Generators support additional methods for more control:
- **`send(value)`**: Passes a value to the generator and resumes execution.
- **`throw(exception)`**: Throws an exception into the generator.
- **`close()`**: Terminates the generator.

---

### **5. Benefits of Using Generators**
- **Memory Efficiency**: Process data lazily, making them ideal for large datasets.
- **Readable and Maintainable Code**: Simplify logic for sequential data processing.
- **Versatility**: Useful in pipelines, infinite loops, or data streams.

---

### **Conclusion**
Generators and the `yield` statement are powerful tools for writing memory-efficient Python programs. Whether you're working with large datasets, building data pipelines, or processing infinite sequences, generators simplify your code while improving performance.



----

The **`yield`** statement in Python is central to the functionality of generators. It enables functions to produce a sequence of values lazily, maintaining state between each value generation. Let’s break it down step by step:

---

### **Understanding the `yield` Statement**
The `yield` keyword is used in a function to produce a value and pause the function's execution, allowing it to be resumed later. This contrasts with the `return` statement, which ends a function and outputs a value.

Here’s a simple example of a generator function with `yield`:

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
```

- When this function is called, it doesn't execute immediately. Instead, it returns a generator object.
- Execution resumes when the generator’s `__next__()` method is called (e.g., through `next()` or a `for` loop).

**Example:**
```python
gen = count_up_to(5)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

At each `yield`, the function's state (local variables, instruction pointer) is saved, and execution resumes from that state on the next call to `next()`.

---

### **How `yield` Differs from `return`**
- **`yield`**: Pauses the function, allowing it to resume later.
- **`return`**: Terminates the function entirely.

For example:
```python
def demo_yield():
    yield 1
    yield 2
    yield 3

for value in demo_yield():
    print(value)
# Output: 1, 2, 3
```

---

### **Practical Uses of `yield`**
1. **Reading Large Files Lazily**
   Yield lines from a file without loading the entire file into memory:
   ```python
   def read_large_file(file_path):
       with open(file_path) as f:
           for line in f:
               yield line.strip()
   ```

2. **Infinite Sequences**
   Generate an endless sequence of numbers:
   ```python
   def infinite_numbers():
       num = 0
       while True:
           yield num
           num += 1
   ```

3. **Data Pipelines**
   Pass data through multiple processing stages:
   ```python
   def multiply_by_two(nums):
       for num in nums:
           yield num * 2

   def add_three(nums):
       for num in nums:
           yield num + 3

   pipeline = add_three(multiply_by_two(range(10)))
   print(list(pipeline))
   # Output: [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
   ```

---

### **Generator Expressions**
A concise way to create generators is through generator expressions, which resemble list comprehensions but use parentheses:

**Example:**
```python
gen_exp = (x**2 for x in range(5))
print(list(gen_exp))  # Output: [0, 1, 4, 9, 16]
```

---

### **Advantages of Using `yield`**
1. **Memory Efficiency**: Generators do not store entire data in memory; they yield items one at a time.
2. **Composability**: Easily create pipelines by chaining generators.
3. **Improved Performance**: Ideal for large datasets or infinite sequences.

---

### **Advanced Generator Methods**
1. **`.send(value)`**: Resumes generator and sends a value that replaces the current `yield` expression.
   ```python
   def accumulator():
       total = 0
       while True:
           value = yield total
           total += value
   ```

2. **`.throw(exception)`**: Raises an exception inside the generator.
   ```python
   gen = accumulator()
   next(gen)  # Start the generator
   gen.throw(ValueError, "Custom error")
   ```

3. **`.close()`**: Stops the generator.
   ```python
   gen.close()
   ```

---


## **Conclusion**


#### Basics of `yield`
The `yield` statement in Python is used in generator functions to pause the function execution and produce a value that is returned to the caller. When the generator resumes execution, it continues right after the last `yield` statement. Unlike `return`, `yield` allows the function to retain its state, including local variables and execution position.

---

### **Examples and Outputs**

#### Simple Use Case of `yield`

```python
def simple_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = simple_generator()

print(next(gen))  # Output: First
print(next(gen))  # Output: Second
print(next(gen))  # Output: Third
```

Here:
1. The `yield` statement pauses the generator and returns the string.
2. When `next()` is called, execution resumes right after the last `yield`.

---

#### Example: State Preservation in `yield`

```python
def counter():
    num = 0
    while num < 3:
        yield num
        num += 1

gen = counter()

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

1. The state (`num`) is preserved across calls.
2. The generator keeps track of the last value of `num`.

---

### Advanced Generator Methods

#### `.send()`

The `.send(value)` method sends a value into the generator. The value sent replaces the `yield` expression where the generator was paused.

```python
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World
```

- **Explanation**:
  - The first `next()` primes the generator (starts it until the first `yield`).
  - Subsequent `.send()` calls resume execution and pass a value into the generator.

---

#### `.throw()`

The `.throw()` method allows raising exceptions inside the generator.

```python
def example_throw():
    try:
        yield "Starting"
    except ValueError as e:
        yield f"Caught an exception: {e}"

gen = example_throw()
print(next(gen))  # Output: Starting
print(gen.throw(ValueError("Test error")))  # Output: Caught an exception: Test error
```

- **Explanation**:
  - `.throw(ValueError)` raises the exception inside the generator.
  - The exception is caught, and the generator handles it gracefully.

---

#### `.close()`

The `.close()` method stops the generator and raises `StopIteration`.

```python
def example_close():
    try:
        yield "Running"
    finally:
        print("Closing generator")

gen = example_close()
print(next(gen))  # Output: Running
gen.close()  # Output: Closing generator
```

- **Explanation**:
  - `.close()` stops the generator and executes the `finally` block.

---

### Combining `yield`, `.send()`, `.throw()`, and `.close()`

**Palindrome Example**

```python
def is_palindrome(num):
    if num < 10:
        return False
    return str(num) == str(num)[::-1]

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)  # Pause and optionally accept a new starting number
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()

# Example Usage
print(next(pal_gen))  # Output: 11
pal_gen.send(1000)    # Resumes from 1000
print(next(pal_gen))  # Output: 1001

# Using .close()
pal_gen.close()  # Stops the generator
```

---

### Comparing Generators and Lists

#### Memory Efficiency

```python
import sys

nums_lc = [i ** 2 for i in range(10000)]
nums_gc = (i ** 2 for i in range(10000))

print(sys.getsizeof(nums_lc))  # Large size (e.g., 87624 bytes)
print(sys.getsizeof(nums_gc))  # Small size (e.g., 120 bytes)
```

- **Key Point**: Generators are more memory-efficient as they yield values lazily.

---

#### Speed Comparison

```python
import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')  # Faster for small data
cProfile.run('sum((i * 2 for i in range(10000)))')  # Slower for large iterations
```

- **Key Point**: List comprehensions can be faster if memory isn’t a constraint.

---




### **Creating Data Pipelines With Generators: Explained with Examples and Outputs**

Data pipelines process large datasets efficiently without loading all the data into memory. Generators are ideal for creating pipelines because they yield data one step at a time.

---

#### **Dataset Preview**
A sample CSV dataset is as follows:
```
permalink,company,numEmps,category,city,state,fundedDate,raisedAmt,raisedCurrency,round
digg,Digg,60,web,San Francisco,CA,1-Dec-06,8500000,USD,b
digg,Digg,60,web,San Francisco,CA,1-Oct-05,2800000,USD,a
facebook,Facebook,450,web,Palo Alto,CA,1-Sep-04,500000,USD,angel
facebook,Facebook,450,web,Palo Alto,CA,1-May-05,12700000,USD,a
photobucket,Photobucket,60,web,Palo Alto,CA,1-Mar-05,3000000,USD,a
```

---

#### **Goal**
Calculate the **total** and **average** amount raised in Series A rounds using generators.

---

### **Step-by-Step Implementation**

#### **Step 1: Read File Line-by-Line**
Use a generator to read each line of the file:
```python
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))  # Lazy file reading
```

#### **Step 2: Split Lines into Values**
Split each line into a list of column values:
```python
list_line = (line.rstrip().split(",") for line in lines)
```

#### **Step 3: Extract Column Names**
Extract column names from the first line:
```python
cols = next(list_line)  # Retrieve the header row
```

#### **Step 4: Create Dictionaries**
Create a dictionary for each row using the column names as keys:
```python
company_dicts = (dict(zip(cols, data)) for data in list_line)
```

#### **Step 5: Filter and Process Data**
Filter only "Series A" rounds and extract the `raisedAmt` field:
```python
funding = (
    int(company_dict["raisedAmt"]) 
    for company_dict in company_dicts 
    if company_dict["round"] == "a"
)
```

#### **Step 6: Calculate Total Funding**
Use `sum()` to compute the total funding for Series A rounds:
```python
total_series_a = sum(funding)
print(f"Total Series A funding: ${total_series_a}")
```

---

### **Complete Code**
```python
file_name = "techcrunch.csv"

# Step 1: Read file line-by-line
lines = (line for line in open(file_name))

# Step 2: Split lines into values
list_line = (line.rstrip().split(",") for line in lines)

# Step 3: Extract column names
cols = next(list_line)

# Step 4: Create dictionaries
company_dicts = (dict(zip(cols, data)) for data in list_line)

# Step 5: Filter and process data for Series A rounds
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

# Step 6: Calculate total Series A funding
total_series_a = sum(funding)
print(f"Total Series A fundraising: ${total_series_a}")
```

---

### **Output**
Running this on the provided dataset yields:
```
Total Series A fundraising: $19000000
```

---

#### **Calculating the Average**
To calculate the average, count the number of Series A rounds and divide the total funding:
```python
# Recreate funding generator since it gets exhausted
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

# Convert funding generator to a list to compute both sum and length
funding_list = list(funding)

# Calculate total and average
total_series_a = sum(funding_list)
average_series_a = total_series_a / len(funding_list)

print(f"Average Series A fundraising: ${average_series_a:.2f}")
```

---

### **Output**
For the sample data:
```
Average Series A fundraising: $6333333.33
```

---

### **Key Concepts Highlighted**
1. **Generators**: Efficiently handle large files without exhausting memory.
2. **Chaining Generators**: Combine multiple generator expressions to process data incrementally.
3. **Lazy Evaluation**: Data is only processed when needed, reducing unnecessary computations.
4. **Pipeline Design**: Modular and reusable components, each handling a specific processing step.

