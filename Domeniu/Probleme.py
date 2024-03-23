from Domeniu.Entitate import Entitate

class Probleme(Entitate):
    def __init__(self, idEntitate, descriere, deadline):
        super().__init__(idEntitate)
        self.__descriere = descriere
        self.__deadline = deadline

    def getDescriere(self):
        return self.__descriere

    def setDescriere(self, descriere):
        self.__descriere = descriere

    def getDeadline(self):
        return self.__deadline

    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return f"Id Problema: {self.getIdEntitate()}, Descriere: {self.__descriere}, Deadline: {self.__deadline}"
