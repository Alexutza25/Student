from dataclasses import dataclass

@dataclass
class StudentNoteNotaDTO:
    nume: str
    nota: int

class StudentiNoteNotaDTOAssembler:
    @staticmethod
    def createNoteNotaDTO(student, notaObt):
        nume = student.getNume()
        nota = notaObt
        return StudentNoteNotaDTO(nume, nota)