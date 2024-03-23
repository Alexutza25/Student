from Domeniu.Probleme import Probleme
from Repository.Repository import Repository


class ProblemeService:
    def __init__(self, problemaRepository: Repository, asignareRepository: Repository):
        self.__problemaRepository = problemaRepository
        self.__asignareRepository = asignareRepository

    def getAllProblema(self):
        '''

        :return: o lista de obiecte de tipul probleme
        '''
        return self.__problemaRepository.getAll()

    def adaugaProblema(self, idProblema, descriere, deadline):
        '''
        adauga o problemam
        :param idProblema: int
        :param descriere: string
        :param deadline: int
        :return:
        '''
        probleme = Probleme(idProblema, descriere, deadline)
        self.__problemaRepository.adauga(probleme)

    def modificaProblema(self, idProblema, descriereNoua, deadlineNou):
        '''
        modicia o problema cu id-ul dat
        :param idProblema: int
        :param descriereNoua: string
        :param deadlineNou: int
        :return:
        '''
        if idProblema.strip() != "" and self.__problemaRepository.getById(idProblema) is None:
            raise ValueError("Nu exista nicio problema cu acest id!")
        probleme = Probleme(idProblema, descriereNoua, deadlineNou)
        self.__problemaRepository.modifica(probleme)

    def stergeProblema(self, idProblema):
        '''
        sterge problema specifica id-ului dat
        :param idProblema: int
        :return:
        '''
        studenti = self.__asignareRepository.getAll()
        for student in studenti:
            if student.getIdProblema() == idProblema:
                self.__asignareRepository.sterge(student.getIdStudent())
        self.__problemaRepository.sterge(idProblema)


    def cautareProblema(self, idProblema):
        '''
        cauta si afiseaza laboratorul si numarul problemei cu id-ul dat
        :param idProblema: string
        :return:
        '''
        return self.__problemaRepository.cauta(idProblema)