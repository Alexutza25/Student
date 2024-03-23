import unittest

from Domeniu.Student import Student
from Repository.Repository import Repository

class TestStudRepository(unittest.TestCase):
    def setUp(self):
        self.studentRepository = Repository()
        self.student = Student("1", "Ana", 1)
        self.studentRepository.adauga(self.student)


    def test_getAll(self):
        self.studenti = self.studentRepository.getAll()
        self.assertEqual(len(self.studenti), 1)


    def test_getBy(self):
        self.student1 = self.studentRepository.getById(self.student.getIdEntitate())

        self.assertEqual(self.student1.getIdEntitate(), "1")
        self.assertEqual(self.student1.getNume(), "Ana")


    def test_adauga_student(self):
        self.studenti = self.studentRepository.getAll()

        self.assertEqual(len(self.studenti), 1)
        self.assertEqual(self.studenti[0].getNume(), "Ana")


    def test_modifica_student(self):
        self.studentRepository. modifica(self.student)
        self.studenti = self.studentRepository.getAll()
        self.assertEqual(self.studenti[0].getNume(), "Ana")


    def test_sterge_student(self):
        self.studentRepository.sterge(self.student.getIdEntitate())

        self.studenti = self.studentRepository.getAll()
        self.assertEqual(len(self.studenti), 0)


if __name__=='__main__':
    unittest.main()



