# 📚 ES6 Data Manipulation Project

This project focuses on advanced JavaScript data manipulation techniques using ES6 features.

## 🎯 Learning Objectives

- How to use map, filter and reduce on arrays
- Typed arrays
- The Set, Map, and Weak link data structures

## ✅ Tasks Completed

1. `0-get_list_students.js`
   - Basic class implementation
   - Returns array of student objects with id, firstName, and location

2. `1-get_list_student_ids.js`
   - Returns array of student IDs using map
   - Handles non-array input by returning empty array

3. `2-get_students_by_loc.js`
   - Filters students by location using filter
   - Returns array of students in specified city

4. `3-get_ids_sum.js`
   - Calculates sum of student IDs using reduce
   - Returns total sum of all student IDs

5. `4-update_grade_by_city.js`
   - Updates student grades by city
   - Combines filter and map methods
   - Sets 'N/A' for students without grades

6. `5-typed_arrays.js`
   - Creates ArrayBuffer with Int8 value
   - Handles position validation
   - Returns DataView object

7. `6-set.js`
   - Converts array to Set
   - Removes duplicate values
   - Returns Set object

8. `7-has_array_values.js`
   - Checks if all array elements exist in Set
   - Returns boolean result
   - Uses Set.has() method

9. `8-clean_set.js`
   - Filters Set values by prefix
   - Joins filtered values with hyphens
   - Returns formatted string

10. `9-groceries_list.js`
    - Creates Map of grocery items
    - Stores item names and quantities
    - Returns Map object

11. `10-update_uniq_items.js`
    - Updates Map quantities
    - Changes value of 1 to 100
    - Validates Map input

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
