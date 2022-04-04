import unittest
import palindrome

class Testpalindrome(unittest.TestCase):
	def testPalindrome(self):
		self.assertEqual(palindrome.palindrome(''), False)
		self.assertEqual(palindrome.palindrome('COnNOc'), True)
		self.assertEqual(palindrome.palindrome('Python'), False)
		self.assertEqual(palindrome.palindrome('I have a pen'), False)
		self.assertEqual(palindrome.palindrome('20522502'), True)

if __name__ == '__main__':
	unittest.main(verbosity = 2)