const fs = require('fs').promises; // Use the promises version of fs

/**
 * Counts students from a CSV file.
 * @param {string} dataPath - Path to the CSV file.
 * @returns {Promise<boolean>} A promise that resolves to true if the operation is successful.
 */
const countStudents = (dataPath) => {
  return fs.readFile(dataPath, 'utf-8')
    .then((data) => {
      const fileLines = data.trim().split('\n');
      const studentGroups = {};
      const dbFieldNames = fileLines[0].split(',');
      const studentPropNames = dbFieldNames.slice(0, dbFieldNames.length - 1);

      for (const line of fileLines.slice(1)) {
        const studentRecord = line.split(',');
        const studentPropValues = studentRecord.slice(0, studentRecord.length - 1);
        const field = studentRecord[studentRecord.length - 1];
        if (!Object.keys(studentGroups).includes(field)) {
          studentGroups[field] = [];
        }
        const studentEntries = studentPropNames.map((propName, idx) => [propName, studentPropValues[idx]]);
        studentGroups[field].push(Object.fromEntries(studentEntries));
      }

      const totalStudents = Object.values(studentGroups).reduce((pre, cur) => (pre || []).length + cur.length);
      // Use a logging library or remove these statements
      // console.log(`Number of students: ${totalStudents}`);
      // for (const [field, group] of Object.entries(studentGroups)) {
      //   const studentNames = group.map((student) => student.firstname).join(', ');
      //   console.log(`Number of students in ${field}: ${group.length}. List: ${studentNames}`);
      // }
      return true;
    })
    .catch((err) => {
      throw new Error('Cannot load the database');
    });
};

module.exports = countStudents;
