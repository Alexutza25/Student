from Domeniu.Student import Student
from Repository.Repository import Repository


class FileStudentRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, student):
        super().adauga(student)
        self.__writeFile()

    def modifica(self, student):
        super().modifica(student)
        self.__writeFile()

    def sterge(self, student):
        super().sterge(student)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idStudent = line.split()[0]
                nume = line.split()[1]
                grupa = line.split()[2]
                student = Student(idStudent, nume, grupa)
                self._entitati[idStudent] = student

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for student in self.getAll():
                f.write(f'{student.getIdEntitate()} {student.getNume()} {student.getGrup()}\n')