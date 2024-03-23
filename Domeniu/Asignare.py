from Domeniu.Entitate import Entitate

class Asignare(Entitate):
    def __init__(self, idEntitate, idStudent, idProblema, nota):
        super().__init__(idEntitate)
        self.__idStudent = idStudent
        self.__idProblema = idProblema
        self.__nota = nota

    def getIdStudent(self):
        return self.__idStudent

    def setIdStudent(self, idStudent):
        self.__idStudent = idStudent

    def getIdProblema(self):
        return self.__idProblema

    def setIdProblema(self, idProblema):
        self.__idProblema = idProblema

    def getNota(self):
        return self.__nota

    def setNota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"Id Asignare: {self.getIdEntitate()}, Id Student: {self.__idStudent}, Id Problema: {self.__idProblema}, Nota: {self.__nota}"


