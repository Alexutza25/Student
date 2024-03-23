

class StudentRepository:
    def __init__(self):
        self.__studenti = {}

    def getAll(self):
        '''
        da lista de studenti
        :return: un dictionar de obiecte de tipul student
        '''
        return list(self.__studenti.values())

    def getById(self, idStudent):
        '''
        cauta studentul dupa id
        :param idStudent: string
        :return: un student daca exista unul sau None in caz contrar
        '''
        if idStudent in self.__studenti:
            return self.__studenti[idStudent]
        return None

    def adauga(self, student):
        '''
        cauta un student
        :param student: obiect de tipul student
        :return:
        '''
        if self.getById(student.getIdStudent()) is not None:
            raise KeyError("Exista deja un student cu id-ul dat")
        self.__studenti[student.getIdStudent()] = student

    def modifica(self, studentNou):
        '''
        modifica un student dupa id
        :param studentNou: obiect de tipul student
        :return:
        '''
        if self.getById(studentNou.getIdStudent()) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat")
        self.__studenti[studentNou.getIdStudent()] = studentNou

    def sterge(self, idStudent):
        '''
        sterge un student dupa id
        :param idStudent: string
        :return:
        '''
        if self.getById(idStudent) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat")
        self.__studenti.pop(idStudent)

