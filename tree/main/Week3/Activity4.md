
Student

Descriptions: students enrolled at YB College.

Attributes: StudentID(PK), FirstName(Char), LastName(Char), DOB(Number), Email(Char), Phone(Number), Major(Char).

Lecturer

Descriptions: faculty members who teach courses.

Attributes: LecturerID (PK), FirstName(Char), LastName(Char), Email(Char), Phone(number), Department(char).

Course

Descriptions: academic subjects offered.

Attributes: CourseID (PK), CourseName(Char), Credits(Number), Department(Char).

Class

Descriptions: a specific offering of a course in a semester.

Attributes: ClassID (PK), CourseID (Number), LecturerID (Number), Semester(Char), Year(Number), Room(Number).