import unittest
from logic.WordPatternGenerator2 import WordPatternGenerator2

class WordPatternGenerator2Test(unittest.TestCase):
	def test0(self):
		splitted = "aaa|bbb".split("|")
		self.assertEqual(2, len(splitted))
		self.assertEqual("aaa", splitted[0])
		self.assertEqual("bbb", splitted[1])

	def test1(self):
		list = [
			"aaa",
			"bbb|ccc",
			"111|222"
		]

		phrases = WordPatternGenerator2(list)

		self.assertEqual(4, len(phrases.phrase_list))
		self.assertEqual("aaabbb111", phrases.phrase_list[0])
		self.assertEqual("aaabbb222", phrases.phrase_list[1])
		self.assertEqual("aaaccc111", phrases.phrase_list[2])
		self.assertEqual("aaaccc222", phrases.phrase_list[3])
