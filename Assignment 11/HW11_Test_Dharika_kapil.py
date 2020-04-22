"""
File to unitest
"""

import os
from HW11_Dharika_kapil import filegenerator,sql,Repository,Students,Instructors,Major,prettytablesql
import unittest
from collections import defaultdict
from prettytable import PrettyTable
from typing import io,DefaultDict,Dict


class TestCases(unittest.TestCase):
    """
    Class to implement unit test cases
    """
    
    def test_filegenerator_student(self)->None:
        """
        funcion to test the file_reading_gen function for student
        """
        test1 :list= filegenerator(os.path.join(r'/Users/dharikapil/Documents/810/Assignment 11','students.txt'), 3, sep="\t",header=True)
        self.assertEqual(next(test1), ["10103", "Jobs, S", "SFEN"])
        self.assertEqual(next(test1), ["10115",	"Bezos, J",	"SFEN"])
        self.assertEqual(next(test1), ["10183",	"Musk, E", "SFEN"])
        self.assertEqual(next(test1), ["11714",	"Gates, B", "CS"])
        

        


    def test_filegenerator_instructor(self)->None:
        
        """function to test the file_reading_gen function for instructor """
         
        test1:list = filegenerator(os.path.join(r'/Users/dharikapil/Documents/810/Assignment 11',"instructors.txt"), 3, sep='\t',header=True)
        self.assertEqual(next(test1), ["98764", "Cohen, R", "SFEN"])
        self.assertEqual(next(test1), ["98763", "Rowland, J", "SFEN"])
        self.assertEqual(next(test1), ["98762", "Hawking, S", "CS"])
        
        

    def test_filegenerator_grades(self)->None:
        
        """function to test the file_reading_gen function for grades"""
         
        test1:list = filegenerator(os.path.join(r'/Users/dharikapil/Documents/810/Assignment 11',"grades.txt"), 4, '\t',header=True)
        self.assertEqual(next(test1), ["10103", "SSW 810", "A-", "98763"])
        self.assertEqual(next(test1), ["10103", "CS 501", "B", "98762"])
        self.assertEqual(next(test1), ["10115", "SSW 810", "A", "98763"])
        self.assertEqual(next(test1), ["10115", "CS 546", "F", "98762"])
        self.assertEqual(next(test1), ["10183", "SSW 555", "A", "98763"])
        self.assertEqual(next(test1), ["10183", "SSW 810", "A", "98763"])
        self.assertEqual(next(test1), ["11714", "SSW 810", "B-", "98763"])
        self.assertEqual(next(test1), ["11714", "CS 546", "A", "98764"])
        self.assertEqual(next(test1), ["11714", "CS 570", "A-", "98762"])
 
       

    def test_sql(self)->None:
        """Function to test the database connection """
        i=sql()
        self.assertEqual(list(next(i)),['Bezos, J','10115','SSW 810','A','Rowland, J'])
        self.assertEqual(list(next(i)),['Bezos, J','10115','CS 546','F', 'Hawking, S'])
        self.assertEqual(list(next(i)),['Gates, B','11714','SSW 810','B-','Rowland, J'])
        self.assertEqual(list(next(i)),['Gates, B','11714','CS 546','A','Cohen, R'])
        self.assertEqual(list(next(i)),['Gates, B','11714','CS 570','A-','Hawking, S'])
        self.assertEqual(list(next(i)),['Jobs, S','10103','SSW 810','A-','Rowland, J'])
        self.assertEqual(list(next(i)),['Jobs, S','10103','CS 501','B','Hawking, S'])
        self.assertEqual(list(next(i)),['Musk, E','10183','SSW 555','A','Rowland, J'])
        self.assertEqual(list(next(i)),['Musk, E','10183','SSW 810','A','Rowland, J'])
        
                
      



def main():   
    """ Main Function to interact with the user """

    Stevens:Repository = Repository(r'/Users/dharikapil/Documents/810/Assignment 11')

    Stevens.prettytable_major()
    print("\n")
    Stevens.prettytable_student()
    print("\n")
    Stevens.prettytable_instructor()

    prettytablesql()
    
    """"print(Stevens._instructor_dict)"""
   
    """Nyu:Repository = Repository()"""
    
    

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()               