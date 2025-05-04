# Pagination Project 📚

## Description 📝
This project focuses on implementing pagination techniques in a REST API context. It covers simple pagination, hypermedia metadata pagination, and deletion-resilient pagination methods.

## Learning Objectives 🎯
By the end of this project, you should be able to explain:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements ⚙️
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/env python3`
- Code should use pycodestyle style (version 2.5.*)
- All modules should have documentation
- All functions should have documentation
- All functions and coroutines must be type-annotated
- Documentation should be meaningful sentences explaining the purpose of the module, class, or method

## Setup 🛠️
- The project uses the `Popular_Baby_Names.csv` dataset
- Python 3.9
- pycodestyle 2.5.*

## Files 📁
- `Popular_Baby_Names.csv`: Dataset file containing baby names data.
- `0-simple_helper_function.py`: Contains the `index_range` helper function to calculate start and end indices for pagination.
- `1-simple_pagination.py`: Implements a `Server` class with a `get_page` method for simple pagination based on page number and page size.
- `2-hypermedia_pagination.py`: Extends the `Server` class with a `get_hyper` method that provides hypermedia metadata (like `next_page`, `prev_page`, `total_pages`) along with the page data.
- `3-hypermedia_del_pagination.py`: Implements a `Server` class with `indexed_dataset` and `get_hyper_index` methods for deletion-resilient hypermedia pagination using indices.

## **👤 Author**
- **Judith Espinal** - Holberton School Student