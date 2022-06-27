import unittest
from translator import english_to_french, french_to_english

class TestEnglish_to_french(unittest.TestCase):
    # Test for null input for french_to_english
    def test_forNull(self):
        self.assertEqual(english_to_french(None),'Null value passed')
    def test_translateEnglish(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_translateFrench(self):
        self.assertEqual(english_to_french('Bonjour'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    # Test for null input for french_to_english
    def test_forNull(self):
        self.assertEqual(french_to_english(None),'Null value passed')
    # Test for the translation of the world 'Hello' and 'Bonjour'.
    def test_translateEnglish(self):
        self.assertEqual(french_to_english('Hello'),'Hello')
    # Test for the translation of the world 'Bonjour' and 'Hello'.
    def test_translateFrench(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()