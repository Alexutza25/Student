class Repository:
    def __init__(self):
        self._entitati = {}

    def getAll(self):
        '''
        returneaza lista de entitati
        :return:  o lista de obiecte de tipul Entitate
        '''
        return list(self._entitati.values())

    def getById(self, idEntitate):
        '''
        returneaza entitatea cu id-ul dat
        :param idEntitate:  string
        :return:  un obiect de tipul Entitate daca exista unul cu id-ul dat, altfel None
        '''

        return self._entitati.get(idEntitate, None)

    def adauga(self, entitate):
        '''
        adauga o entitate in dictionar
        :param entitate:  obiect de tipul Entitate
        :return:
        '''
        if self.getById(entitate.getIdEntitate()) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat")
        self._entitati[entitate.getIdEntitate()] = entitate

    def sterge(self, idEntitate):
        '''
        sterge o entitate din dictionar
        :param idEntitate: string
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat")
        self._entitati.pop(idEntitate)

    def modifica(self, entitateNoua):
        '''
        functia modifica toate datele despre o entitate cu id-ul dat
        :param entitateNoua: noua entitate de tipul Entitate
        :return:
        '''
        if self.getById(entitateNoua.getIdEntitate()) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat")
        self._entitati[entitateNoua.getIdEntitate()] = entitateNoua

    def cauta(self, idEntitate):
        '''
        functia cauta si afiseaza entitatea cu id-ul dat
        :param idEntitate: string
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat")
        return self._entitati[idEntitate]