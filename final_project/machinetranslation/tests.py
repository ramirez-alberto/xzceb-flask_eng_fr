''' Unit tests for translator module'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    ''' Test for null input for french_to_english'''

    def test_for_null(self):
        ''' Test for null'''
        self.assertEqual(english_to_french(None),'Null value passed')

    def test_translate_english(self):
        '''Test for English translation'''
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_translate_french(self):
        '''Test for French translation'''
        self.assertEqual(english_to_french('Bonjour'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    ''' Test for null input for french_to_english'''

    def test_for_null(self):
        ''' Test for null'''
        self.assertEqual(french_to_english(None),'Null value passed')

    def test_translate_english(self):
        '''Test for English translation'''
        self.assertEqual(french_to_english('Hello'),'Hello')

    def test_translate_french(self):
        '''Test for French translation'''
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()
