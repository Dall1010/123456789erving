from classes import Student

Student1 = Student(1, "jose", "ISI")
Student2 = Student(2, "maria", "ISI")
Student3 = Student(3, "marco", "ISI")

Students = []
Students.append(Student1)
Students.append(Student2)
Students.append(Student3)

#mostrar lista
for stu in Students:
    print(stu)