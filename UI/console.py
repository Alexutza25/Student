from Service.studentService import StudentService
from Service.problemeService import ProblemeService
from Service.AsignareService import AsignareService
from Domeniu.Exceptii.Eroare import Error

from Service.DTO import DtoService

class Consola:
    def __init__(self, studentService: StudentService, problemeService:ProblemeService, asignareService: AsignareService, dtoService: DtoService):
        self.__studentService = studentService
        self.__problemeService = problemeService
        self.__asignareService = asignareService
        self.__dtoService = dtoService


    def adaugaStudent(self):
        try:
            idStudent = input("Dati id-ul studentului: ")
            nume = input("Dati numele studentului: ")
            grup = input("Dati grupa studentului ")
            self.__studentService.addStudent(idStudent, nume, grup)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def modificaStudent(self):
        try:
            idStudent = input("Dati id-ul studentului: ")
            numeNou = input("Dati numele studentului: ")
            grupNou = input("Dati grupa studentului: ")
            self.__studentService.modifyStudent(idStudent, numeNou, grupNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def stergeStudent(self):
        try:
            idStudent = input("Dati id-ul studentului: ")
            self.__studentService.stergeStudent(idStudent)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def adaugaProblema(self):
        try:
            idProblema = input("Dati id-ul problemei: ")
            descriere = input("Dati descrierea problemei: ")
            deadline = input("Dati durata (in minute) a timpului acordat pentru rezolvarea problemei: ")
            self.__problemeService.adaugaProblema(idProblema, descriere, deadline)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def modificaProblema(self):
        try:
            idProblema = input("Dati id-ul problemei de modificat: ")
            descriereNoua = input("Dati noua descriere a problemei: ")
            deadlineNou = input("Dati noul deadline (in minute) pt rezolvarea problemei: ")
            self.__problemeService.modificaProblema(idProblema, descriereNoua, deadlineNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def stergeProblema(self):
        try:
            idProblema = input("Dati id-ul problemei de sters: ")
            self.__problemeService.stergeProblema(idProblema)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def adaugaAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari: ")
            idStudent = input("Dati id-ul studentului: ")
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator: ")
            nota = input("Dati nota primita de student pe acest laborator si problema: ")
            while float(nota) > 10 or float(nota) < 1:
                print("Nota trebuie sa fie in intervalul 1 - 10")
                nota = input("Dati nota primita de student pe acest laborator si problema: ")
            self.__asignareService.adaugaAsignare(idAsignare, idStudent, idProblemaLaborator, nota)
        except KeyError as e:
            print(e)
        except Error as e:
            print(e)


    def stergeAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari care sa se stearga: ")
            self.__asignareService.stergeAsignare(idAsignare)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def modificaAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari: ")
            idStudent = input("Dati id-ul studentului: ")
            idProblemaLaborator = input("Dati numarul laboratorului si numarul problemei de laborator: ")
            nota = input("Dati nota primita de student pe acest laborator si problema: ")
            while float(nota) > 10 or float(nota) < 1:
                print("Nota trebuie sa fie in intervalul 1 - 10")
                nota = input("Dati nota primita de student pe acest laborator si problema: ")
            self.__asignareService.modificaAsignare(idAsignare, idStudent, idProblemaLaborator, nota)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def cautareStudent(self):
        try:
            idStudent = input("Dati id-ul studentului cautat: ")
            print(self.__studentService.cautareStudent(idStudent))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def cautareProblema(self):
        try:
            idProblema = input("Dati id-ul problemei")
            print(self.__problemeService.cautareProblema(idProblema))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def cautareAsignare(self):
        try:
            idAsignare = input("Dati id-ul asignari cautate: ")
            print(self.__asignareService.cautareAsignare(idAsignare))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)


    def statistica_1(self):
        try:
            idProblema = input("Dati id-ul problemei pe baza careia se va creea statistica: ")
            criteriu = input("Dati criteriul dupa care sa se sorteze lista afisata (nume sau nota): ")
            print(self.__asignareService.sortareStatistica1(idProblema, criteriu))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def statistica_2(self):
        try:
            print(self.__asignareService.medieSub5())
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def statistica_1DTO(self):
        try:
            idProblema = input("Dati id-ul problemei pe baza careia se va creea statistica: ")
            criteriu = input("Dati criteriul dupa care sa se sorteze lista afisata (nume sau nota): ")
            if criteriu == "nume":
                print(self.__dtoService.ordonare_nume(idProblema))
            else:
                print(self.__dtoService.ordonare_nota(idProblema))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def statistica_2DTO(self):
        try:
            print(self.__dtoService.medie_sub_5_DTO())
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def printMenu(self):
        print("1. Adauga student")
        print("2. Modifica student")
        print("3. Sterge student")
        print("4. Adauga problema")
        print("5. Modifica problema")
        print("6. Sterge problema")
        print("7. Asigneaza un laborator")
        print("8. Modifica asignare")
        print("9. Sterge asignare")
        print("10. Cauta un student")
        print("11. Cauta o problema")
        print("12. Cauta o asignare")
        print("13. Statistica 1")
        print("14. Statistica 2")
        print("15. Statistica 1 DTO")
        print("16. Statistica 2 DTO")
        print("s. Afiseaza toti studentii")
        print("p. Afiseaza toate problemele")
        print("a. Afiseaza toate asignarile")
        print("x. Iesire")


    def meniu(self):
        while True:
            self.printMenu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaStudent()
            elif optiune == "2":
                self.modificaStudent()
            elif optiune == "3":
                self.stergeStudent()
            elif optiune == "4":
                self.adaugaProblema()
            elif optiune == "5":
                self.modificaProblema()
            elif optiune == "6":
                self.stergeProblema()
            elif optiune == "7":
                self.adaugaAsignare()
            elif optiune == "8":
                self.modificaAsignare()
            elif optiune == "9":
                self.stergeAsignare()
            elif optiune == "10":
                self.cautareStudent()
            elif optiune == "11":
                self.cautareProblema()
            elif optiune == "12":
                self.cautareAsignare()
            elif optiune == "13":
                self.statistica_1()
            elif optiune == "14":
                self.statistica_2()
            elif optiune == "15":
                self.statistica_1DTO()
            elif optiune == "16":
                self.statistica_2DTO()
            elif optiune == "s":
                self.afiseaza(self.__studentService.getAllStudenti())
            elif optiune == "p":
                self.afiseaza(self.__problemeService.getAllProblema())
            elif optiune == "a":
                self.afiseaza(self.__asignareService.getAllAsignari())
            elif optiune == "x":
                break
            else: print("Optiune gresita, reincercati")

















































































    