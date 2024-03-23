from Domeniu.Asignare import Asignare
from Repository.Repository import Repository
from Domeniu.Exceptii.Eroare import Error

class AsignareService:
    def __init__(self, asignareRepository: Repository, studentiRepository: Repository, problemeLaboratorRepository: Repository):
        self.__asignareRepository = asignareRepository
        self.__studentiRepository = studentiRepository
        self.__problemeLaboratorRepository = problemeLaboratorRepository

    def getAllAsignari(self):
        '''
        returneaza lista de asignari
        :return: o lista de obiecte de tipul Asignare
        '''
        return self.__asignareRepository.getAll()

    def adaugaAsignare(self, idAsignare, idStudent, idProblemaLaborator, nota):
        '''
        adauga o asignare
        :param idAsignare: string
        :param idStudent:   string
        :param idProblemaLaborator:    string
        :param nota:    string
        :return:
        '''
        if self.__studentiRepository.getById(idStudent) is None:
            raise KeyError("Nu exista un student cu id-ul dat")
        if self.__problemeLaboratorRepository.getById(idProblemaLaborator) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")

        asignari = self.__asignareRepository.getAll()
        for asignare in asignari:
            if asignare.getIdStudent() == idStudent and asignare.getIdProblema() == idProblemaLaborator:
                raise Error("Studentul este deja inscris la problema data")

        asignare = Asignare(idAsignare, idStudent, idProblemaLaborator, nota)
        self.__asignareRepository.adauga(asignare)

    def stergeAsignare(self, idAsignare):
        '''
        sterge o asignare care are id-ul idStudent si id-ul idProblemaLaborator
        :return:
        '''
        self.__asignareRepository.sterge(idAsignare)

    def modificaAsignare(self, idAsignare, idStudentNou, idProblemaLaboratorNoua, notaNoua):
        '''
        functia modifica toate datele despre o asignare cu id-ul dat
        :param idStudentNou: string
        :param idStudentNou: string
        :param idProblemaLaboratorNoua: string
        :param notaNoua: string
        :return:
        '''
        if self.__studentiRepository.getById(idStudentNou) is None:
            raise KeyError("Nu exista un student cu id-ul dat")
        if self.__problemeLaboratorRepository.getById(idProblemaLaboratorNoua) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")

        asignareNoua = Asignare(idAsignare, idStudentNou, idProblemaLaboratorNoua, notaNoua)
        self.__asignareRepository.modifica(asignareNoua)

    def cautareAsignare(self, idAsignare):
        '''
        functia cauta si afiseaza asignarea cu id-ul dat
        :param idAsignare: string
        :return:
        '''
        return self.__asignareRepository.cauta(idAsignare)

    def sortareStatistica1(self, idProblemaLaborator ,criteriuSortare):
        if self.__problemeLaboratorRepository.getById(idProblemaLaborator) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")
        asignari = self.__asignareRepository.getAll()
        studenti = self.__studentiRepository.getAll()
        lista = []
        nr = 0
        for asignare in asignari:
            if asignare.getIdProblema() == idProblemaLaborator:
                for student in studenti:
                    if student.getIdEntitate() == asignare.getIdStudent():
                        lista.append(student.getNume())
                        lista[nr] = lista[nr] + " " + asignare.getNota()
                        nr += 1
        if criteriuSortare == "nume":
            lista.sort()
        elif criteriuSortare == "nota":
            lista.sort(key= lambda x: x.split()[-1])
            #lista.sort(key= lambda x: x.split()[-1])
        else:
            raise KeyError("Statistica nu poate fi sortata decat dupa nume sau nota")
        if lista == []:
            return "Problema cu id-ul introdus nu este asignata niciunui student"

        return lista

    def medieSub5(self ):
        asignari = self.__asignareRepository.getAll()
        studenti = self.__studentiRepository.getAll()
        lista = []
        index = 0
        nota = 0
        cnt = 0
        for student in studenti:
            for asignare in asignari:
                if student.getIdEntitate() == asignare.getIdStudent():
                    if nota == 0:
                        nota = int(asignare.getNota())
                    else:
                        nota = int(asignare.getNota())
                    if int(nota) < 5:
                        lista.append(student.getNume())
                        lista[index] = lista[index] + " " + str(nota)
                        index += 1

        return lista

