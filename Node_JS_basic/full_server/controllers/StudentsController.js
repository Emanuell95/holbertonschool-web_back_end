import readDatabase from '../utils.js';

/**
 * StudentsController class handles student-related routes
 */
class StudentsController {
  /**
   * Get all students grouped by field
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static async getAllStudents(request, response) {
    const databasePath = process.argv[2];
    
    try {
      const students = await readDatabase(databasePath);
      let result = 'This is the list of our students\n';
      
      // Sort fields alphabetically (case insensitive)
      const sortedFields = Object.keys(students).sort((a, b) => 
        a.toLowerCase().localeCompare(b.toLowerCase())
      );
      
      const lines = [];
      sortedFields.forEach(field => {
        const studentList = students[field];
        const count = studentList.length;
        const names = studentList.join(', ');
        lines.push(`Number of students in ${field}: ${count}. List: ${names}`);
      });
      
      result += lines.join('\n');
      response.status(200).send(result);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  /**
   * Get all students by major (CS or SWE)
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    const databasePath = process.argv[2];
    
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    
    try {
      const students = await readDatabase(databasePath);
      const studentList = students[major] || [];
      const names = studentList.join(', ');
      response.status(200).send(`List: ${names}`);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
