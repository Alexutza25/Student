from Domeniu.DTO1 import StudentiNumeNotaDTOAssembler
from Domeniu.DTO2 import StudentiNoteNotaDTOAssembler



class DtoService:
    def __init__(self, studentService, problemaService, asignariService):
        self.__studentService = studentService
        self.__problemaService = problemaService
        self.__asignariService = asignariService

    def __create_student_nume_dtos(self, id_problema):
        student_dtos = []
        asignari = self.__asignariService.getAllAsignari()
        studenti = self.__studentService.getAllStudenti()
        lista = []
        index = 0
        count = self.studenti_asignati()
        for asignare in asignari:
            if asignare.getIdProblema() == id_problema:
                for student in studenti:
                    if student.getIdEntitate() == asignare.getIdStudent():
                        lista.append(student.getNume())
                        lista[index] = lista[index] + " " + asignare.getNota()
                        index += 1
                        dto = StudentiNumeNotaDTOAssembler.createNumeNotaDTO(student, asignare.getNota())

                student_dtos.append(dto)
        return student_dtos

    def __create_student_nota_dtos(self, id_problema):
        student_dtos = []
        count = self.studenti_asignati()
        for student in self.__studentService.getAllStudenti():
            if student.getIdEntitate() in count:
                dto = StudentiNoteNotaDTOAssembler.createNoteNotaDTO(student,count[student.getIdEntitate()])
                student_dtos.append(dto)
        return student_dtos

    def studenti_asignati(self):
        count = {}
        elemente = self.__asignariService.getAllAsignari()
        for element in elemente:
            if element.getIdEntitate() in count:
                count[element.getIdEntitate()] += 1
            else:
                count[element.getIdEntitate()] = 1
        return count

    def ordonare_nume(self, id_problema):
        count = self.studenti_asignati()
        j = int((100 * len(count)) / 100)
        student_dtos = self.__create_student_nume_dtos(id_problema)
        student_dtos = sorted(student_dtos, key=lambda x: x.nume, reverse=False)
        return student_dtos[:j]

    def ordonare_nota(self, id_problema):
        count = self.studenti_asignati()
        j = int((100 * len(count)) / 100)
        student_dtos = self.__create_student_nume_dtos(id_problema)
        student_dtos = sorted(student_dtos, key=lambda x: x.nota, reverse=False)
        return student_dtos[:j]

    '''def medie_sub_5_DTO(self):
        student_dtos = []
        asignari = self.__asignariService.getAllAsignari()
        studenti = self.__studentService.getAllStudenti()
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
                        dto = StudentiNumeNotaDTOAssembler.createNumeNotaDTO(student, nota)
            student_dtos.append(dto)
        return student_dtos'''