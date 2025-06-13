const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split into lines and filter out empty lines
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      // Remove header line
      const students = lines.slice(1);

      let result = `Number of students: ${students.length}\n`;

      // Group students by field
      const fields = {};
      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');
        const trimmedField = field.trim();
        if (!fields[trimmedField]) {
          fields[trimmedField] = [];
        }
        fields[trimmedField].push(firstname);
      });

      // Add results for each field
      for (const [field, studentsList] of Object.entries(fields)) {
        result += `Number of students in ${field}: ${studentsList.length}. List: ${studentsList.join(', ')}\n`;
      }

      resolve(result.trim());
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');

  const databasePath = process.argv[2];

  if (!databasePath) {
    res.send('This is the list of our students\nCannot load the database');
    return;
  }

  try {
    const studentData = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentData}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(1245);

module.exports = app;
