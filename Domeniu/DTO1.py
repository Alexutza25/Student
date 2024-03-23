from dataclasses import dataclass

@dataclass
class StudentNumeNotaDTO:
    nume: str
    nota: int

class StudentiNumeNotaDTOAssembler:
    @staticmethod
    def createNumeNotaDTO(student, notaObt):
        nume = student.getNume()
        nota = notaObt
        return StudentNumeNotaDTO(nume, nota)