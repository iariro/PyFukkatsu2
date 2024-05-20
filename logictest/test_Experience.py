import unittest
from logic.ローレシアの王子の経験値 import ローレシアの王子の経験値

class ExperienceTest(unittest.TestCase):
	def test01(self):
		self.assertEqual(
			1,
			ローレシアの王子の経験値().getLevel(0))

	def test02(self):
		self.assertEqual(
			1,
			ローレシアの王子の経験値().getLevel(1))

	def test03(self):
		self.assertEqual(
			1,
			ローレシアの王子の経験値().getLevel(11))

	def test04(self):
		self.assertEqual(
			2,
			ローレシアの王子の経験値().getLevel(12))

	def test05(self):
		self.assertEqual(
			49,
			ローレシアの王子の経験値().getLevel(999999))

	def test06(self):
		self.assertEqual(
			50,
			ローレシアの王子の経験値().getLevel(1000000))

	def test11(self):
		self.assertEqual(
			12,
			ローレシアの王子の経験値().getPointForNextLevel(0))

	def test12(self):
		self.assertEqual(
			20,
			ローレシアの王子の経験値().getPointForNextLevel(12))

	def test13(self):
		self.assertEqual(
			1,
			ローレシアの王子の経験値().getPointForNextLevel(999999))

	def test14(self):
		self.assertEqual(
			0,
			ローレシアの王子の経験値().getPointForNextLevel(1000000))
