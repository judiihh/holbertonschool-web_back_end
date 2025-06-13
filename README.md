# 🚀 Web Backend Development Projects

This repository contains various projects focusing on different aspects of web backend development, including JavaScript (ES6), Node.js, and Python.

## 📚 Projects

### 1. ES6 Basic JavaScript Project
Focuses on learning and implementing ES6 (ECMAScript 2015) basic features in JavaScript.

#### 🎯 Learning Objectives
- Understanding ES6 and its new features
- Working with constants and variables
- Block-scoped variables
- Arrow functions and default parameters
- Rest and spread parameters
- String templating
- Object creation and properties
- Iterators and for-of loops

#### ✅ Tasks Completed
1. `0-constants.js` - Using const and let
2. `1-block-scoped.js` - Block scoping
3. `2-arrow.js` - Arrow functions
4. `3-default-parameter.js` - Default parameters
5. `4-rest-parameter.js` - Rest parameters
6. `5-spread-operator.js` - Spread syntax
7. `6-string-interpolation.js` - Template literals
8. `7-getBudgetObject.js` - Object property shorthand
9. `8-getBudgetCurrentYear.js` - Computed property names
10. `9-getFullBudget.js` - ES6 method properties
11. `10-loops.js` - For...of loops
12. `11-createEmployeesObject.js` - Employee object creation
13. `12-createReportObject.js` - Report object creation

### 2. JavaScript Classes Project
Focuses on Object-Oriented Programming in JavaScript using classes.

#### 🎯 Learning Objectives
- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

#### ✅ Tasks Completed
1. `0-classroom.js` - Basic class implementation
2. `1-make_classrooms.js` - Creating multiple classroom instances
3. `2-hbtn_course.js` - Course class with getters and setters
4. `3-currency.js` - Currency class with custom string representation
5. `4-pricing.js` - Pricing class with static methods
6. `5-building.js` - Abstract Building class
7. `6-sky_high.js` - SkyHighBuilding class extending Building
8. `7-airport.js` - Airport class with custom string representation
9. `8-hbtn_class.js` - HolbertonClass with custom type casting
10. `9-hoisting.js` - Class hoisting example
11. `10-car.js` - Car class with Symbol-based cloning

### 3. ES6 Promises Project
Focuses on asynchronous programming in JavaScript using Promises.

#### 🎯 Learning Objectives
- Understanding Promises and their usage
- How to use the `then`, `resolve`, `catch` methods
- How to use the `async` and `await` operators
- How to use the `Promise.prototype.finally`
- Handling multiple promises with `Promise.all`
- Error handling in promises

### 4. ES6 Data Manipulation Project
Focuses on array and data manipulation using modern JavaScript features.

#### 🎯 Learning Objectives
- How to use map, filter, and reduce on arrays
- Typed arrays
- The Set, Map, and WeakMap data structures
- Working with modern JavaScript data structures
- Advanced array methods and transformations

### 5. Python Variable Annotations Project
Focuses on type annotations in Python programming.

#### 🎯 Learning Objectives
- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

### 6. Node.js Basics Project
Comprehensive Node.js project covering fundamental concepts from basic I/O operations to building full-featured web servers with Express.js and MVC architecture.

#### 🎯 Learning Objectives
- Understanding Node.js runtime environment
- Working with process stdin/stdout
- Creating HTTP servers using Node.js built-in modules
- Building web applications with Express.js framework
- Implementing MVC architecture patterns
- File system operations and CSV parsing
- ES6 modules and Babel transpilation
- RESTful API design and routing

#### ✅ Tasks Completed
1. `0-console.js` - Basic console output function
2. `1-stdin.js` - Interactive command-line program with stdin handling
3. `4-http.js` - Basic HTTP server using Node.js http module
4. `5-http.js` - Complex HTTP server with CSV parsing and student endpoints
5. `6-http_express.js` - Simple Express.js server implementation
6. `7-http_express.js` - Complex Express server with student data routes
7. `full_server/` - Complete MVC Express application with:
   - Controllers for handling business logic
   - Routes for endpoint definitions
   - Utilities for database operations
   - ES6 modules with Babel support

#### 🌐 Server Features
- **Basic HTTP Server**: Simple greeting endpoint
- **Student Data API**: CSV-based student management system
- **Express Integration**: Modern web framework implementation
- **MVC Architecture**: Organized code structure with separation of concerns
- **RESTful Endpoints**: 
  - `GET /` - Home page
  - `GET /students` - All students grouped by major
  - `GET /students/:major` - Students filtered by major (CS/SWE)

## 🛠️ Setup

1. For JavaScript Projects - Install NodeJS 20.x.x:
```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

2. For Python Projects - Ensure Python 3.7 or later is installed:
```bash
python3 --version
```

3. Install project dependencies:
For JavaScript:
```bash
npm install
```
For Python:
```bash
pip3 install -r requirements.txt
```

## 🧪 Running Tests

For JavaScript Projects:
```bash
npm test
```

For Python Projects:
```bash
python3 -m unittest discover -v
```

## 🔍 Linting

For JavaScript:
```bash
npm run lint
```

For Python:
```bash
mypy .
```

## 📋 Requirements

JavaScript Projects:
- Node.js 20.x.x
- npm 9.x.x
- Jest Testing Framework
- ESLint
- Babel

Python Projects:
- Python 3.7+
- mypy
- unittest

## **👤 Author**
- **Judith Espinal** - Holberton School Student