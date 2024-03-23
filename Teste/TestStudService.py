import unittest

from Repository.Repository import Repository

from Service.problemeService import ProblemeService
from Service.AsignareService import AsignareService
from Service.studentService import StudentService

class TestStudService(unittest.TestCase):
    def setUp(self):
        self.studentRepository = Repository()
        self.problemaRepository = Repository()
        self.studentService = StudentService(self.studentRepository, self.problemaRepository)
        self.studentService.addStudent("1", "Ana", "1")
        self.studentService.addStudent("2", "Maria", "3")


    def test_getAll(self):
        studenti = self.studentService.getAllStudenti()

        self.assertEqual(len(studenti), 2)


    def test_adauga_student(self):
        self.studenti = self.studentService.getAllStudenti()

        self.assertEqual(self.studenti[0].getIdEntitate(), "1")


    def test_modifica_student(self):
        self.studentService.modifyStudent("1", "Andreea", "2")

        self.studenti = self.studentService.getAllStudenti()

        self.assertEqual(self.studenti[0].getNume(), "Andreea")


    def test_sterge_student(self):
        self.studentService.stergeStudent("1")

        self.studenti = self.studentService.getAllStudenti()

        self.assertEqual(len(self.studenti), 1)


    def test_gaseste_id(self):
        self.student1 = self.studentService.cautareStudent("1")

        self.assertEqual(self.student1.getNume(), "Ana")


    def test_statistica1(self):
        self.studentService.addStudent("3", "Dariana", "2")
        problemaRepository = Repository()
        asignareRepository = Repository()
        problemaService = ProblemeService(problemaRepository, asignareRepository)
        problemaService.adaugaProblema("1", "usoara", "120")
        problemaService.adaugaProblema("2", "grea", "360")
        asignareService = AsignareService(asignareRepository, self.studentRepository ,problemaRepository)
        asignareService.adaugaAsignare("1", "1", "2", "7")
        asignareService.adaugaAsignare("2", "2", "1", "4")
        asignareService.adaugaAsignare("3", "3", "1", "3")
        lista_sortata = asignareService.sortareStatistica1("1", "nume")

        self.assertEqual(len(lista_sortata), 2)
        v = lista_sortata[0].split()
        self.assertEqual(v[0], "Dariana")
        self.assertEqual(v[1], "3")


    def test_statistica2(self):
        self.studentService.addStudent("3", "Dariana", "2")
        problemaRepository = Repository()
        asignareRepository = Repository()
        problemaService = ProblemeService(problemaRepository, asignareRepository)
        problemaService.adaugaProblema("1", "usoara", "120")
        problemaService.adaugaProblema("2", "grea", "360")
        asignareService = AsignareService(asignareRepository, self.studentRepository, problemaRepository)
        asignareService.adaugaAsignare("1", "1", "2", "7")
        asignareService.adaugaAsignare("2", "2", "1", "4")
        asignareService.adaugaAsignare("3", "3", "1", "3")
        lista = asignareService.medieSub5()

        v = lista[0].split()

        self.assertEqual(v[0], "Maria")
        self.assertEqual(v[1], "4")


if __name__ == '__main__':
    unittest.main()



