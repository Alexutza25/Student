from Domeniu.Student import Student


def testStudent():
    student = Student("1", "ana", "311")

    assert student.getNume() == "ana"
    assert student.getGrup() == "311"

def testStudentSetteri():
    student = Student("1", "ana", "311")


    student.setNume("paul")
    assert student.getNume() == "paul"

    student.setGrup("999")
    assert student.getGrup() == "999"






