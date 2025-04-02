function updateStudentGradeByCity(students, city, newGrades) {
    return students.map((student) => {
        if (student.location === city) {
            newGrades.forEach((grade) => {
                if (grade.studentId === student.id) {
                    student.grade = grade.grade;
                }
            });
        }
        return student;
    });
}
export default updateStudentGradeByCity;