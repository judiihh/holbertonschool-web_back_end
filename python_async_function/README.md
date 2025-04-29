# Python Async Function

This project covers asynchronous programming in Python using `async`/`await` syntax and the `asyncio` library. The project focuses on understanding and implementing asynchronous coroutines, tasks, and concurrent programming concepts.

## Learning Objectives

By the end of this project, you should be able to explain:

* `async` and `await` syntax in Python
* How to execute an async program with `asyncio`
* How to run concurrent coroutines
* How to create `asyncio` tasks
* How to use the `random` module

## Requirements

### General
* All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
* All files should end with a new line
* The first line of all files should be `#!/usr/bin/env python3`
* Code should use `pycodestyle` style (version 2.5.x)
* All modules, functions, and coroutines must be type-annotated
* All modules should have documentation
* All functions/coroutines should have documentation
* All files must be executable

## Tasks

### 0. The basics of async
* File: `0-basic_async_syntax.py`
* Write an asynchronous coroutine `wait_random` that:
  * Takes an integer argument `max_delay` (default value of 10)
  * Waits for a random delay between 0 and `max_delay` seconds (float value)
  * Returns the random delay

## Author
* Holberton School Students 