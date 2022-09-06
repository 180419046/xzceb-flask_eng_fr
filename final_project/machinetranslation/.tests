import unittest

from translator import *

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello, World"), "Bonjour, Monde")
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        self.assertEqual(englishToFrench(""), "")  


class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour, Monde"), "Hello, World") 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertEqual(frenchToEnglish(""), "") 
        
unittest.main()