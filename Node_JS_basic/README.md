# 🚀 Node.js Basics

This project contains comprehensive Node.js exercises covering fundamental concepts from basic I/O operations to building full-featured web servers with Express.js and MVC architecture.

## 📋 Project Structure

### Core Tasks
- `0-console.js` - A simple module that exports a function to display messages in the console
- `1-stdin.js` - Interactive command-line program that reads user input from stdin
- `4-http.js` - Basic HTTP server using Node.js built-in `http` module
- `5-http.js` - Complex HTTP server with CSV file parsing and student data endpoints
- `6-http_express.js` - Simple Express.js server with basic routing
- `7-http_express.js` - Complex Express.js server with student data endpoints

### Full Server Application (Task 8)
- `full_server/` - Complete MVC structured Express application
  - `controllers/AppController.js` - Home page controller
  - `controllers/StudentsController.js` - Student data management controller
  - `routes/index.js` - Application route definitions
  - `utils.js` - Utility functions for database operations
  - `server.js` - Main Express server application

### Configuration Files
- `babel.config.js` - Babel configuration for ES6+ features
- `.babelrc` - Babel runtime configuration
- `.eslintrc.js` - ESLint configuration for code quality
- `package.json` - Project dependencies and scripts

### Data Files
- `database.csv` - Sample student data for testing server endpoints

## 🛠️ Setup

1. Install dependencies:
```bash
npm install
```

2. For the full server application, ensure you have the database file:
```bash
# The database.csv file should be in the project root
```

## 🧪 Available Scripts

- `npm run lint` - Run ESLint on all JavaScript files
- `npm run check-lint` - Check linting on all JavaScript files
- `npm run test` - Run tests using Mocha
- `npm run dev` - Start the full server application with Babel and Nodemon
- `npm run full-server` - Alternative command to start the full server

## 🎯 Task Descriptions

### Task 0: Executing basic JavaScript with Node.js
**File:** `0-console.js`
- Exports a function `displayMessage` that prints a string to STDOUT

### Task 1: Using Process stdin
**File:** `1-stdin.js`
- Interactive CLI program that prompts for and displays user name
- Handles both interactive and non-interactive input modes

### Task 4: Create a small HTTP server using Node's HTTP module
**File:** `4-http.js`
- Basic HTTP server listening on port 1245
- Returns "Hello Holberton School!" for any endpoint

### Task 5: Create a more complex HTTP server using Node's HTTP module
**File:** `5-http.js`
- HTTP server with two endpoints: `/` and `/students`
- Reads and parses CSV database file
- Displays student statistics grouped by field of study

### Task 6: Create a small HTTP server using Express
**File:** `6-http_express.js`
- Simple Express server with root endpoint
- Demonstrates Express.js basic setup and routing

### Task 7: Create a more complex HTTP server using Express
**File:** `7-http_express.js`
- Express server with student data endpoints
- Cleaner implementation of Task 5 using Express routing

### Task 8: Organize a complex HTTP server using Express
**Directory:** `full_server/`
- Complete MVC architecture with Express
- Separate controllers, routes, and utilities
- ES6 modules with Babel transpilation
- RESTful API endpoints for student data

## 🌐 Server Endpoints

### Basic Servers (Tasks 4-7)
- `GET /` - Returns greeting message
- `GET /students` - Returns student statistics from CSV database

### Full Server (Task 8)
- `GET /` - Home page endpoint
- `GET /students` - All students grouped by major
- `GET /students/:major` - Students filtered by specific major (CS or SWE)

## 🗃️ Database Format

The `database.csv` file should contain student data in the following format:
```csv
firstname,lastname,age,field
John,Doe,20,CS
Jane,Smith,22,SWE
...
```

## 📚 Technologies Used

### Main Dependencies
- **Express.js** - Web application framework
- **Chai HTTP** - HTTP testing utilities

### Development Dependencies
- **Babel** - JavaScript transpiler for ES6+ features
- **ESLint** - Code linting and style enforcement
- **Mocha** - Testing framework
- **Chai** - Assertion library
- **Nodemon** - Development server with auto-reload
- **Sinon** - Test spies, stubs, and mocks

## 🚀 Running the Applications

### Individual Task Files
```bash
# Task 0
node 0-console.js

# Task 1
node 1-stdin.js

# Task 4
node 4-http.js

# Task 5
node 5-http.js database.csv

# Task 6
node 6-http_express.js

# Task 7
node 7-http_express.js database.csv
```

### Full Server Application
```bash
# Start the full server (Task 8)
npm run dev

# Or alternatively
DB_HOST=database.csv npm run dev
```

The full server will be available at `http://localhost:1245`

## 🧪 Testing

All servers can be tested using curl or any HTTP client:

```bash
# Test basic endpoints
curl localhost:1245/
curl localhost:1245/students

# Test full server major-specific endpoint
curl localhost:1245/students/CS
curl localhost:1245/students/SWE
```

---

👤 **Author**  
Judith Espinal - Holberton School Student