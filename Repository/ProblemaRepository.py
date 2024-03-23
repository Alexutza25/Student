class ProblemaRepository:
    def __init__(self):
        self.__probleme = {}

    def getAll(self):
        return list(self.__probleme.values())

    def getById(self, idProbleme):
        if idProbleme in self.__probleme:
            return self.__probleme[idProbleme]
        return None

    def adauga(self, probleme):
        self.__probleme[probleme.getIdProblema()] = probleme

    def modifica(self, problemaNoua):
        if self.getById(problemaNoua.getIdProblema()) is None:
            raise KeyError("Nu exista nicio problema cu id-ul dat!")
        self.__probleme[problemaNoua.getIdProblema()] = problemaNoua

    def sterge(self, idProblema):
        if self.getById(idProblema) is None:
            raise KeyError("Nu exista nicio problema cu id-ul dat!")
        self.__probleme.pop(idProblema)