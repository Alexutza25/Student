from Domeniu.Asignare import Asignare
from Repository.Repository import Repository


class FileAsignareRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, asignare):
        super().adauga(asignare)
        self.__writeFile()

    def modifica(self, asignare):
        super().modifica(asignare)
        self.__writeFile()

    def sterge(self, asignare):
        super().sterge(asignare)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idAsignare = line.split()[0]
                idStudent = line.split()[1]
                idProblema = line.split()[2]
                nota = line.split()[3]
                asignare = Asignare(idAsignare, idStudent, idProblema, nota)
                self._entitati[idAsignare] = asignare

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for asignare in self.getAll():
                f.write(f'{asignare.getIdEntitate()} {asignare.getIdStudent()} {asignare.getIdProblema()} {asignare.getNota()}\n')