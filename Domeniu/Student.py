from Domeniu.Entitate import Entitate

class Student(Entitate):
    def __init__(self, idEntitate, nume, grupa):
        super().__init__(idEntitate)
        self.__nume = nume
        self.__grupa = grupa

    def getNume(self):
        return self.__nume

    def setNume(self, nume):
        self.__nume = nume

    def getGrup(self):
        return self.__grupa

    def setGrup(self, grupa):
        self.__grupa = grupa

    def __str__(self):
        return f"Id Student: {self.getIdEntitate()}, Nume: {self.__nume}, Grupa {self.__grupa}"
