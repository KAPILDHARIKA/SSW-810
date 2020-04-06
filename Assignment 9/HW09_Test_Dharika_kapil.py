"""
Homework 9 
Author: Dharika kapil
"""

import os
import unittest
from collections import defaultdict
from prettytable import PrettyTable
from typing import io,DefaultDict,Dict
"""import the file _ reader from another homework"""

class Repository:
    """
    class for Repository data
    """
    """PT_FIELD_NAMES = ['CWID','Name','']"""
    def __init__(self,path:str):

       
        self._directory:str = path
        os.chdir(self._directory)
        self._student_dict:Dict[str,Students]= dict()
        self._instructor_dict:Dict[str,Instructors]= dict()

        s_path:str="students.txt"
        i_path:str="instructors.txt"
        g_path:str="grades.txt"
        try:
            for cwid, name, major in file_reading_gen(os.path.join(self._directory,s_path),3,'\t',header=False):
                self.new_student(cwid,name,major)
        except(FileNotFoundError,ValueError) as e:
            print(e)
        try:
            for cwid, name, dept in file_reading_gen(os.path.join(self._directory,i_path),3,'\t',header=False):
                self.new_instructor(cwid,name,dept) 
        except(FileNotFoundError,ValueError) as e:
            print(e)        

        try:
            for student_cwid, course, Lettergrade, instructor_cwid in file_reading_gen(os.path.join(self._directory,g_path),4,'\t'):
                for key, value in self._student_dict.items():
                    if student_cwid == key:
                        value.courses.append(course)

                for key, value in self._instructor_dict.items():
                    if instructor_cwid == key:
                        value.courses[course] +=1 
        except(FileNotFoundError,ValueError) as e:
            print(e)                           

        """
         s:Student =self._student[student_cwid]
         s.store_course_grade(course,grade)
         inst:Instructor =self._instructor
         inst:store_course_student(course)
        """           

    def new_student(self,cwid:str,name:str,major:str)->None:
        """
        adding new student
        """ 
        self._student_dict[cwid]:dict= Students(cwid,name,major)

    def new_instructor(self,cwid:str,name:str,dept:str)->None:
        """
        adding new instructor
        """     
        self._instructor_dict[cwid]:dict= Instructors(cwid,name,dept)     

    def prettytable_student(self)->None:
        """
        function to print student table
        """
        stable:PrettyTable = PrettyTable()
        stable.field_names:list = ['CWID','Name','Completed courses']

        for rows in self._student_dict.values():
            stable.add_row([rows._cwid, rows._name, sorted(rows.courses)])      
    
        print(stable)

    def prettytable_instructor(self)->None:   
        """
        function to print instructor table
        """  
        itable:PrettyTable = PrettyTable()
        itable.field_names:list= ['CWID','Name', 'Dept', 'Course', 'Students']

        for item in self._instructor_dict.values():
            for course, student in item.courses.items():
               itable.add_row([item._cwid, item._name, item._dept, course, student])               

        print(itable)

class Students:
    """
    class for Student data
    """   
    def __init__(self, cwid:str, name:str, major:str)->None:
        """
        init methord 
        """
        self._cwid:str = cwid
        self._name:str = name
        self._major:str = major
        self.courses:list = list()

class Instructors:     
    """
    class for Instructors data      
    """
    def __init__(self, cwid:str, name:str, dept:str)->None:
        """
        init methord 
        """
        self._cwid:str = cwid
        self._name:str = name
        self._dept:str = dept
        self.courses:defaultdict(int) = defaultdict(int)

        """ 
        def store_course_student(self,course:str):
            self._courses[course] =+ 1
        """

def file_reading_gen(path:str, fields:int, sep:str, header:bool=False)->None:
    """
        File Reader Function to clean a field separated file
    """
    
    if not os.path.exists(path):
        raise FileNotFoundError

    fp:io = open(path, 'r')

    with fp:
        if header:
            next(fp)

        for n, line in enumerate(fp, 1):
            line:str = line.strip()

            if line.count(sep) == fields - 1:
                yield list(line.split(sep))

            else:
                raise ValueError(f"{fp.name} has {line.count(sep) + 1} fields on line {n} "+f"but expected {fields}")


class TestCases(unittest.TestCase):
    """
    Class to implement unit test cases
    """

    def test_file_reading_gen_student(self)->None:
        """
        funcion to test the file_reading_gen function for student
        """
        test1 :list= file_reading_gen('students.txt', 3, sep="\t")
        self.assertEqual(next(test1), ["10103", "Baldwin, C", "SFEN"])
        self.assertEqual(next(test1), ["10115",	"Wyatt, X",	"SFEN"])
        self.assertEqual(next(test1), ["10172",	"Forbes, I", "SFEN"])
        self.assertEqual(next(test1), ["10175",	"Erickson, D", "SFEN"])
        self.assertEqual(next(test1), ["10183",	"Chapman, O", "SFEN"])
        self.assertEqual(next(test1), ["11399", "Cordova, I", "SYEN"])
        self.assertEqual(next(test1), ["11461",	"Wright, U", "SYEN"])
        self.assertEqual(next(test1), ["11658", "Kelly, P", "SYEN"])
        self.assertEqual(next(test1), ["11714", "Morton, A", "SYEN"])
        self.assertEqual(next(test1), ["11788", "Fuller, E", "SYEN"])

        """with self.assertRaises(FileNotFoundError):
            for i in file_reading_gen(r"/Users/homework 9/notstudents.txt", "3", "\t"):
                return i"""


    def test_file_reading_gen_instructor(self)->None:
        
        """function to test the file_reading_gen function for instructor """
         
        test1:list = file_reading_gen("instructors.txt", 3, sep='\t')
        self.assertEqual(next(test1), ["98765", "Einstein, A", "SFEN"])
        self.assertEqual(next(test1), ["98764", "Feynman, R", "SFEN"])
        self.assertEqual(next(test1), ["98763", "Newton, I", "SFEN"])
        self.assertEqual(next(test1), ["98762", "Hawking, S", "SYEN"])
        self.assertEqual(next(test1), ["98761", "Edison, A", "SYEN"])
        self.assertEqual(next(test1), ["98760", "Darwin, C", "SYEN"])
        """self.assertNotEqual(next(test1), ["435765", "foo, b", "commerce"])"""  

    def test_file_reading_gen_grades(self)->None:
        
        """function to test the file_reading_gen function for grades"""
         
        test1:list = file_reading_gen("grades.txt", 4, '\t')
        self.assertEqual(next(test1), ["10103", "SSW 567", "A", "98765"])
        self.assertEqual(next(test1), ["10103", "SSW 564", "A-", "98764"])
        self.assertEqual(next(test1), ["10103", "SSW 687", "B", "98764"])
        self.assertEqual(next(test1), ["10103", "CS 501", "B", "98764"])
        self.assertEqual(next(test1), ["10115", "SSW 567", "A", "98765"])
        self.assertEqual(next(test1), ["10115", "SSW 564", "B+", "98764"])
        self.assertEqual(next(test1), ["10115", "SSW 687", "A", "98764"])
        self.assertEqual(next(test1), ["10115", "CS 545", "A", "98764"])
        self.assertEqual(next(test1), ["10172", "SSW 555", "A", "98763"])
        self.assertEqual(next(test1), ["10172", "SSW 567", "A-", "98765"])
        self.assertNotEqual(next(test1), ["1829126832", "MIS 810", "F", "862987263"]) 

def main():   
    """ Main Function to interact with the user """

    Stevens:Repository = Repository(r'/Users/dharikapil/Documents/810/Assignment 9')

    Stevens.prettytable_student()

    print("\n\n")

    Stevens.prettytable_instructor()

    print(Stevens._instructor_dict)


    """Nyu:Repository = Repository()"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()       
