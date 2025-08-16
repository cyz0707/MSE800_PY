
Student

Role: Represents students enrolled at YB College.

Attributes: StudentID(Number), FirstName(Char), LastName(Char), DOB(Number), Email(Char), Phone(Number), Major(Char).

Lecturer

Role: Represents faculty members who teach courses.

Attributes: LecturerID (Number), FirstName(Char), LastName(Char), Email(Char), Phone(number), Department(char).

Course

Role: Represents academic subjects offered.

Attributes: CourseID (Number), CourseName(Char), Credits(Number), Department(Char).

Class

Role: Represents a specific offering of a course in a semester.

Attributes: ClassID (Number), CourseID (Number), LecturerID (Number), Semester(Char), Year(Number), Room(Number).