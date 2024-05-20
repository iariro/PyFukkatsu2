import unittest
from logic import JumonGenerator
from logic.WordPatternGenerator2 import WordPatternGenerator2

class GenerateJumonTest(unittest.TestCase):
	def generate(self, words):
		phrases = WordPatternGenerator2(words)
		jumonList = JumonGenerator.generateWithExtraCharacter(phrases, False)

		returnStringList = []
		for jumon in jumonList:
			returnStringList.append(jumon.getJumonStringNoReturn())
		return returnStringList

	def test1(self):
		jumon = self.generate([ "ゆうてい", "みやおう", "きむこう", "ほりいゆうじ", "とりやまあきら" ])
		self.assertEqual(1, len(jumon))
		self.assertEqual("ゆうていみやおうきむこうほりいゆうじとりやまあきらぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺぺ", jumon[0])

	def test2(self):
		jumon = self.generate([ "それゆけ", "とらくえ", "すいそうがく", "がつきたずさえ", "たびたて", "ゆうしやたち", "れべるいちらいぶ", "おめてとう" ])
		self.assertEqual(1, len(jumon))
		self.assertEqual("それゆけとらくえすいそうがくがつきたずさえたびたてゆうしやたちれべるいちらいぶおめてとうねねねね", jumon[0])
