import unittest


from Domeniu.Probleme import Probleme
from Domeniu.Student import Student


class TestProb(unittest.TestCase):
    def setUp(self):
        self.prob1 = Probleme("1", "usoara", "120")


    def test_getId(self):
        self.assertEqual(self.prob1.getIdEntitate(), "1")


    def test_getDescriere(self):
        self.assertEqual(self.prob1.getDescriere(), "usoara")


    def test_getDeadline(self):
        self.assertEqual(self.prob1.getDeadline(), "120")


    def test_setId(self):
        self.prob1.setIdEntitate("11")
        self.assertEqual(self.prob1.getIdEntitate(),"11")


    def test_setDescriere(self):
        self.prob1.setDescriere("grea")
        self.assertEqual(self.prob1.getDescriere(), "grea")


    '''def test_setDeadline(self):
        self.prob1.setDurata("360")
        self.assertEqual(self.prob1.getDeadline(), "360")'''


class TestStud(unittest.TestCase):
    def setUp(self):
        self.student = Student("1", "Andreea", "1")


    def test_getId(self):
        self.assertEqual(self.student.getIdEntitate(), "1")


    def test_getNume(self):
        self.assertEqual(self.student.getNume(), "Andreea")


    def test_getGrupa(self):
        self.assertEqual(self.student.getGrup(), "1")


    def test_setId(self):
        self.student.setIdEntitate("1")
        self.assertEqual(self.student.getIdEntitate(), "1")


    def test_setNume(self):
        self.student.setNume("Andrei")
        self.assertEqual(self.student.getNume(), "Andrei")


    def test_setGrupa(self):
        self.student.setGrup("2")
        self.assertEqual(self.student.getGrup(), "2")

if __name__ == '__main__':
    unittest.main()


