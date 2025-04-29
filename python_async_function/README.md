# Python Async Function 🔄

This project covers asynchronous programming in Python using `async`/`await` syntax and the `asyncio` library. The project focuses on understanding and implementing asynchronous coroutines, tasks, and concurrent programming concepts.

## Learning Objectives 🎯

By the end of this project, you should be able to explain:

* `async` and `await` syntax in Python
* How to execute an async program with `asyncio`
* How to run concurrent coroutines
* How to create `asyncio` tasks
* How to use the `random` module

## Requirements ⚙️

### General
* All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
* All files should end with a new line
* The first line of all files should be `#!/usr/bin/env python3`
* Code should use `pycodestyle` style (version 2.5.x)
* All modules, functions, and coroutines must be type-annotated
* All modules should have documentation
* All functions/coroutines should have documentation
* All files must be executable

## Tasks 📝

### 0. The basics of async ⏰
* File: `0-basic_async_syntax.py`
* Write an asynchronous coroutine `wait_random` that:
  * Takes an integer argument `max_delay` (default value of 10)
  * Waits for a random delay between 0 and `max_delay` seconds (float value)
  * Returns the random delay

### 1. Let's execute multiple coroutines at the same time with async 🔄
* File: `1-concurrent_coroutines.py`
* Write an async routine `wait_n` that:
  * Takes in 2 int arguments: `n` and `max_delay`
  * Spawns `wait_random` n times with the specified `max_delay`
  * Returns the list of all delays (float values) in ascending order

### 2. Measure the runtime ⚡
* File: `2-measure_runtime.py`
* Create a `measure_time` function that:
  * Takes integers `n` and `max_delay` as arguments
  * Measures the total execution time for `wait_n(n, max_delay)`
  * Returns `total_time / n` as a float

### 3. Tasks 📋
* File: `3-tasks.py`
* Write a regular function `task_wait_random` that:
  * Takes an integer `max_delay`
  * Returns an `asyncio.Task` object
  * Uses `wait_random` from the first task

### 4. Tasks 🔄
* File: `4-tasks.py`
* Write a function `task_wait_n` that:
  * Is nearly identical to `wait_n` from task 1
  * Uses `task_wait_random` instead of `wait_random`
  * Returns list of delays in ascending order

## Author 👨‍💻
* Holberton School Students 