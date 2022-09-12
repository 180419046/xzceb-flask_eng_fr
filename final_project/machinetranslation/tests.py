import unittest

from translator import *

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello, World"), "Bonjour, Monde")
        self.assertNotEqual(englishToFrench("Hello"), "Peter") 
        self.assertEqual(englishToFrench(""), "")  


class TestDouble(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour, Monde"), "Hello, World") 
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Peter") 
        self.assertEqual(frenchToEnglish(""), "") 
        
unittest.main()