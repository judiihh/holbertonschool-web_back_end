import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(request, response) {
    const databasePath = process.argv[2];

    try {
      const students = await readDatabase(databasePath);
      
      let result = 'This is the list of our students\n';
      
      // Sort fields alphabetically (case insensitive)
      const sortedFields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      
      sortedFields.forEach((field) => {
        const studentsList = students[field];
        result += `Number of students in ${field}: ${studentsList.length}. List: ${studentsList.join(', ')}\n`;
      });
      
      response.status(200).send(result.trim());
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    const databasePath = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(databasePath);
      
      if (students[major]) {
        response.status(200).send(`List: ${students[major].join(', ')}`);
      } else {
        response.status(200).send('List: ');
      }
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController; 