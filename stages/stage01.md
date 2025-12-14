
## 🛠 Tools & Skills 


Getting started with AI might seem challenging, but our path here begins with two foundational skills: Python and GitHub. Python is the most common programming language in AI world: simple syntax and powerful libraries (like TensorFlow and PyTorch) necessary to build intelligent systems.  

GitHub is your collaborative workspace and professional portfolio. It allows you to save, version-control, and share your code, enabling you to work on complex projects, and showcase your machine learning models to potential employers. 

### IDE Tools 

The first thing you need when starting to code in Python is an IDE (Integrated Development Environment). An IDE is a tool that helps you write, run, debug, and organize your code more efficiently than a simple text editor. There are many IDEs available for Python development. Below are three of the most common and beginner-friendly options, along with why you might choose each one and how to get started.

#### 1. Visual Studio Code (VS Code) 

Visual Studio Code is a lightweight, free, and extremely popular code editor that becomes a powerful Python IDE through extensions. Download from the official website: https://code.visualstudio.com

##### 🎥 Quick Intro to Visual Studio Code
[![Learn Visual Studio Code in 7min](https://img.youtube.com/vi/B-s71n0dHUk/0.jpg)](https://youtu.be/B-s71n0dHUk)

**Focus:** Get familiar with VS Code basics — interface, workspace, and core features.  
**Duration:** ~7 minutes


#### 2. Jupyter Notebook

Best for Learning & Experimentation. Jupyter Notebook is an interactive environment where you write and run Python code in small blocks (cells), alongside explanations, equations, and visualizations. Install via Anaconda, which includes Python, Jupyter, and many useful libraries https://www.anaconda.com  Or install directly using pip: `pip install notebook`

#### 3. Google Colab

One of the most common IDE for beginners: 

✅ No setup or installation needed

✅ Runs entirely in the browser

✅ Free access to GPUs and TPUs (with limits)

✅ Ideal for Python, data science, and AI

✅ Easy to share notebooks with instructors or classmates

For beginners, this removes one of the biggest barriers to learning: environment setup.

**How to Get Started**

-   Go to: https://colab.research.google.com

-   Sign in with a Google account

-   Click New Notebook

-   Start writing Python code immediately

##### 🎥 Google Colab - Quick Video
[![Introduction to Artificial Intelligence](https://img.youtube.com/vi/inN8seMm7UI/0.jpg)](https://youtu.be/inN8seMm7UI)

### Python Foundations

-   Python basics (comments, data types, etc...)


#### 1. Comments: Comments are notes in your code that Python ignores. They help explain what your code does.

```python
# This is a single-line comment

"""
This is a 
multi-line comment
or docstring.
"""
```

#### 2. Variables and Data Types 
| Data Type | Example                        | Description        |
| --------- | ------------------------------ | ------------------ |
| int       | `age = 25`                     | Integer numbers    |
| float     | `height = 1.75`                | Decimal numbers    |
| str       | `name = "Alice"`               | Text               |
| bool      | `is_student = True`            | True or False      |
| list      | `fruits = ["apple", "banana"]` | Ordered collection |
| dict      | `person = {"name": "Alice"}`   | Key-value pairs    |


#### 3. Basic Operations 

| Operation      | Symbol | Example   | Output |
| -------------- | ------ | --------- | ------ |
| Addition       | `+`    | `2 + 3`   | 5      |
| Subtraction    | `-`    | `5 - 2`   | 3      |
| Multiplication | `*`    | `4 * 3`   | 12     |
| Division       | `/`    | `10 / 3`  | 3.333… |
| Floor division | `//`   | `10 // 3` | 3      |
| Modulus        | `%`    | `10 % 3`  | 1      |
| Exponent       | `**`   | `2 ** 3`  | 8      |

#### 4. Strings 
```python 
greeting = "Hello"
name = 'Alice'
message = greeting + " " + name
print(message)  # Output: Hello Alice

# String formatting
age = 25
print(f"{name} is {age} years old.")  # Using f-strings
```

#### 5. Lists 
```python 
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # Access first element -> apple
fruits.append("orange")  # Add an element
fruits.remove("banana")  # Remove an element

```
#### 6. Dictionaries 
```python 
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
person["age"] = 26     # Update value

```
#### 7. Conditional Statements 
```python 
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```
#### 8. Loops 
```python 

# For loop
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```



-   Functions, modules
-   File handling


### Git & GitHub Basics

-   Repositories, commits, push/pull
-   GitHub workflow
-   Good Starting Point is https://docs.github.com/en/get-started/start-your-journey/hello-world


[Back to AI Journey](../README.md)