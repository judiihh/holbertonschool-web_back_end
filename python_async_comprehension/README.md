# Python - Async Comprehension 🔄 ⚡

This project covers asynchronous comprehensions and generators in Python. It explores advanced Python features including async generators, async comprehensions, and type annotations for generators.

## Learning Objectives 🎯

At the end of this project, you should be able to explain:

* 🔄 How to write an asynchronous generator
* ⚡ How to use async comprehensions
* 📝 How to type-annotate generators

## Requirements 📋

### General
* 📝 Allowed editors: vi, vim, emacs
* 💻 All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* ↩️ All files should end with a new line
* ⚡ The first line of all files should be exactly `#!/usr/bin/env python3`
* 🎨 Code should use pycodestyle style (version 2.5.x)
* 📚 All modules, functions, and coroutines must be documented
* ✍️ All functions and coroutines must be type-annotated
* 📖 Documentation should be real sentences explaining the purpose of the module, class, or method

## Tasks 📝

### 0. Async Generator ⚡
* Write a coroutine called `async_generator` that:
  * Takes no arguments
  * Loops 10 times ♾️
  * Asynchronously waits 1 second each iteration ⏱️
  * Yields a random number between 0 and 10 (specifically, `random.uniform(0, 10)`) 🎲
* File: `0-async_generator.py`

### 1. Async Comprehension ⚡
* Write a coroutine called `async_comprehension` that:
  * Takes no arguments
  * Collects 10 random numbers using an async comprehension over `async_generator`
  * Returns the list of 10 random numbers 📝
* File: `1-async_comprehension.py`

### 2. Measure Runtime ⏱️
* Write a coroutine called `measure_runtime` that:
  * Executes `async_comprehension` four times in parallel using `asyncio.gather`
  * Measures the total runtime and returns it 📈
* File: `2-measure_runtime.py`

## **👤 Author**
- **Judith Espinal** - Holberton School Student 