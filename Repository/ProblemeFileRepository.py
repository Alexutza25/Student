from Domeniu.Probleme import Probleme
from Repository.Repository import Repository


class FileProblemeRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, problema):
        super().adauga(problema)
        self.__writeFile()

    def modifica(self, problema):
        super().modifica(problema)
        self.__writeFile()

    def sterge(self, problema):
        super().sterge(problema)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idProblema = line.split()[0]
                descriere = line.split()[1]
                deadline = line.split()[2]
                problema = Probleme(idProblema, descriere, deadline)
                self._entitati[idProblema] = problema

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for problema in self.getAll():
                f.write(f'{problema.getIdEntitate()} {problema.getDescriere()} {problema.getDeadline()}\n')