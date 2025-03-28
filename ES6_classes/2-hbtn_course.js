class HolbertonCourse {
    constructor(name, length, students) {
      // Type checking in the constructor
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
      if (!Array.isArray(students)) {
        throw new TypeError('Students must be an Array');
      }
      if (!students.every(student => typeof student === 'string')) {
        throw new TypeError('Students must be an array of strings');
      }

      this._name = name;
      this._length = length;
      this._students = students;
    }
  
    /**
     * @param {String} name
     */
    set name(name) {
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
      this._name = name;
    }
  
    get name() {
      return this._name;
    }
  
    /**
     * @param {Number} length
     */
    set length(length) {
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
      this._length = length;
    }
  
    get length() {
      return this._length;
    }
  
    /**
     * @param {Array} students
     */
    set students(students) {
      if (!Array.isArray(students)) {
        throw new TypeError('Students must be an Array');
      }
      if (!students.every(student => typeof student === 'string')) {
        throw new TypeError('Students must be an array of strings');
      }
      this._students = students;
    }
  
    get students() {
      return this._students;
    }
  }
  
  export default HolbertonCourse;
