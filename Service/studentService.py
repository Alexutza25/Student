from Domeniu.Student import Student
from Repository.Repository import Repository

class StudentService:
    def __init__(self, studentRepository: Repository, asignareRepository: Repository):
        self.__studentRepository = studentRepository
        self.__asignareRepository = asignareRepository

    def getAllStudenti(self):
        """
        da toata lista de studenti
        :return: o lista de obiecte de tip student
        """
        return self.__studentRepository.getAll()

    def addStudent(self, idStudent, nume, grup):
        '''
        aduga un student
        :param idStudent: string
        :param nume: string
        :param grup: string
        :return:
        '''

        student = Student(idStudent, nume, grup)
        self.__studentRepository.adauga(student)

    def modifyStudent(self, idStudent, numeNou, grupNou):
        '''
        modifica un student dupa id
        :param idStudent: string
        :param numeNou: string
        :param grupNou: string
        :return:
        '''

        student = Student(idStudent, numeNou, grupNou)
        self.__studentRepository.modifica(student)

    def stergeStudent(self, idStudent):
        '''
        sterge un student dupa id
        :param idStudent: string
        :return:
        '''
        asignari = self.__asignareRepository.getAll()
        for asignare in asignari:
            if asignare.getIdStudent() == idStudent:
                self.__asignareRepository.sterge(asignare.getIdAsignare)
        self.__studentRepository.sterge(idStudent)


    def cautareStudent(self, idStudent):
        '''
        functia cauta si afiseaza studentul cu id-ul dat
        :param idStudent: string
        :return:
        '''
        return self.__studentRepository.cauta(idStudent)




