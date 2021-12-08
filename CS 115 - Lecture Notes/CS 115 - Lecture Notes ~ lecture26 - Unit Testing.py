# Sid Bhatia
# CS115-C
# Lecture #26 - Unit Testing

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        # Final Exam will mainly cover writing assertEqual test cases
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('fOo'.upper(), 'FOO')
        self.assertNotEqual('FOO'.upper(), 'foo')
        self.assertEqual('bAr'.upper(), 'BAR')
    
    def test_isupper(self):
        self.assertFalse('Foo'.isupper())
        self.assertFalse('BaR'.isupper())
        self.assertTrue('FOO'.isupper())
        self.assertEqual('fOO'.isupper(), False) # same as as 'self.assertFalse('fOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check if s.split fails when seperator is a non-string
        self.assertRaises(TypeError, str.split, s, 3.5)
        with self.assertRaises(TypeError):
            s.split(3.5)

TestStringMethods()