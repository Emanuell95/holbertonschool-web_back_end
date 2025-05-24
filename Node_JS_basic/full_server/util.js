import fs from 'fs';

/**
 * Reads the database file and returns an object of arrays of student firstnames per field
 * @param {string} filePath - Path to the database file
 * @returns {Promise} Promise that resolves to an object with student data organized by field
 */
const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      try {
        const lines = data.trim().split('\n');
        if (lines.length <= 1) {
          resolve({});
          return;
        }

        const students = {};
        
        // Skip the header row
        for (let i = 1; i < lines.length; i++) {
          const line = lines[i].trim();
          if (line) {
            const [firstname, , , field] = line.split(',');
            if (firstname && field) {
              if (!students[field]) {
                students[field] = [];
              }
              students[field].push(firstname);
            }
          }
        }

        resolve(students);
      } catch (parseError) {
        reject(parseError);
      }
    });
  });
};

export default readDatabase;
