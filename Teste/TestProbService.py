import unittest

from Repository.Repository import Repository

from Service.problemeService import ProblemeService

class TestProbService(unittest.TestCase):
    def setUp(self):
        self.problemaRepository = Repository()
        self.asignareRepository = Repository()
        self.problemaService = ProblemeService(self.problemaRepository, self.asignareRepository)
        self.problemaService.adaugaProblema("1", "usoara", "120")
        self.problemaService.adaugaProblema("2", "grea", "360")


    def test_getAll(self):
        self.probleme = self.problemaService.getAllProblema()

        self.assertEqual(len(self.probleme), 2)


    def test_adauga_problema(self):
        self.probleme = self.problemaService.getAllProblema()

        self.assertEqual(self.probleme[1].getDescriere(), "grea")


    def test_modifica_problema(self):
        self.problemaService.modificaProblema("1", "foarte usoara", "60")

        self.probleme = self.problemaService.getAllProblema()

        self.assertEqual(self.probleme[0].getDescriere(), "foarte usoara")


    def test_sterge_problema(self):
        self.problemaService.stergeProblema("1")

        self.probleme = self.problemaService.getAllProblema()

        self.assertEqual(len(self.probleme), 1)


    def test_gaseste_problema(self):
        self.probleme = self.problemaService.cautareProblema("1")

        self.assertEqual(self.probleme.getDescriere(), "usoara")


if __name__ == '__main__':
    unittest.main()

