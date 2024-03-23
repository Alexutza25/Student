import unittest

from Domeniu.Probleme import Probleme
from Repository.Repository import Repository

class TestProbRepository(unittest.TestCase):
    def setUp(self):
        self.probRepository = Repository()
        self.prob1 = Probleme("1", "usoara", "120")
        self.prob2 = Probleme("2", "grea", "360")
        self.probRepository.adauga(self.prob1)
        self.probRepository.adauga(self.prob2)


    def test_getAll(self):
        probleme = self.probRepository.getAll()
        self.assertEqual(len(probleme), 2)


    def test_getById(self):
        problema1 = self.probRepository.getById("1")
        problema2 = self.probRepository.getById("2")

        self.assertEqual(problema1.getIdEntitate(), "1")
        self.assertEqual(problema2.getDescriere(), "grea")


    def test_adauga_problema(self):
        probleme = self.probRepository.getAll()
        self.assertEqual(probleme[0].getIdEntitate(), "1")


    def test_modifica_problema(self):
        self.prob_mod = Probleme("1", "medie", "240")
        self.probRepository.modifica(self.prob_mod)
        probleme = self.probRepository.getAll()

        self.assertEqual(probleme[0].getDescriere(), "medie")


    def test_sterge_problema(self):

        self.probRepository.sterge(self.prob1.getIdEntitate())

        probleme = self.probRepository.getAll()
        self.assertEqual(len(probleme), 1)


if __name__ == '__main__':
    unittest.main()
