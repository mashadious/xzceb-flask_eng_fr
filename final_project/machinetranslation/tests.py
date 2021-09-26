'''
This code is the test for the translator
'''
import unittest #importing testing tools
from translator import english_to_french, french_to_english #importing functions to be tested'''

class TESTE2F(unittest.TestCase):
    def test1(self):
        '''
        function to test the english to french translation
        '''
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('sun'),'Soleil')
        self.assertNotEqual(english_to_french('year'),'Year')

class TESTF2E(unittest.TestCase):
    def test2(self):
        '''
        function to test the french to english translation
        '''
        self.assertEqual(french_to_english(' '),' ')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('lune'),'Moon')
        self.assertNotEqual(french_to_english('lune'),'Lune')


unittest.main()
