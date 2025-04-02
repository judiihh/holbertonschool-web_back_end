# 📚 ES6 Promises Project

This project focuses on understanding and implementing Promises in JavaScript using ES6 features.

## 🎯 Learning Objectives

- Promises (how, why, and what)
- How to use the then, resolve, catch methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an async function

## ✅ Tasks Completed

1. `0-promise.js`
   - Return a Promise using getResponseFromAPI()
   - Basic Promise implementation

2. `1-promise.js`
   - Implement getFullResponseFromAPI(success)
   - Return resolved/rejected Promise based on boolean parameter

3. `2-then.js`
   - Handle Promise resolution with then/catch
   - Return specific response format
   - Log API response message

4. `3-all.js`
   - Handle multiple Promises with Promise.all
   - Import and use uploadPhoto and createUser functions
   - Handle Promise rejections

5. `4-user-promise.js`
   - Create signUpUser function returning a resolved Promise
   - Return user object with firstName and lastName

6. `5-photo-reject.js`
   - Implement uploadPhoto function returning a rejected Promise
   - Include error message with filename

7. `6-final-user.js`
   - Handle multiple Promise settlements
   - Use Promise.allSettled
   - Return array of Promise results

8. `7-load_balancer.js`
   - Implement loadBalancer function using Promise.race
   - Return value from first resolved Promise

9. `8-try.js`
   - Create divideFunction with error handling
   - Throw error for division by zero

10. `9-try.js`
    - Implement guardrail function with try/catch
    - Handle function execution and errors
    - Return queue array with results

## 📋 Requirements

- Node.js 20.x.x
- npm 9.x.x
- Jest Testing Framework
- ESLint
- Babel

## 🧪 Testing

To run the tests:
```bash
npm test
```

To run the linter:
```bash
npm run lint
```

To run both tests and linting:
```bash
npm run full-test
```

## **👤 Author**
- **Judith Espinal** - Holberton School Student
