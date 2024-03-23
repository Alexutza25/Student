import unittest
from unittest import runner

from Repository.ProblemeFileRepository import FileProblemeRepository
from Service.studentService import StudentService
from Repository.AsignareFileRepository import FileAsignareRepository
from Service.problemeService import ProblemeService
from UI.console import Consola
from Service.DTO import DtoService
from Teste.TestDomeniu import *
from Teste.TestProbRep import *
from Teste.TestStudRep import *
from Teste.TestProbService import *
from Teste.TestStudService import *
from Service.AsignareService import AsignareService
from Repository.StudentFileRepository import FileStudentRepository

def run_some_tests():
    test_classes_to_run = [TestProb, TestStud, TestStudService, TestProbService,
                           TestProbRepository, TestStudRepository]
    loader = unittest.TestLoader()

    suites_list = []
    for test in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test)
        suites_list.append(suite)

        #big_suite = unittest.TextTestRunner()
        #results = runner.run(big_suite)

def main():
    run_some_tests()
    #testAll()
    #studentRepository = Repository()
    #problemaLaboratorRepository = Repository()
    #asignareRepository = Repository()

    problemaLaboratorRepository = FileProblemeRepository("Probleme.txt")
    studentRepository = FileStudentRepository("Student.txt")
    asignareRepository = FileAsignareRepository("Asignari.txt")

    studentService = StudentService(studentRepository, asignareRepository)
    problemeService = ProblemeService(problemaLaboratorRepository, asignareRepository)
    asignareService = AsignareService(asignareRepository, studentRepository, problemaLaboratorRepository)
    dtoService = DtoService(studentService, problemeService, asignareService)

    consola = Consola(studentService, problemeService, asignareService, dtoService)
    consola.meniu()

main()