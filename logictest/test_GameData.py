import unittest
from logic.GameData import GameData

class GameDataTest(unittest.TestCase):
	def test名前1(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("あいうえ")
		self.assertEqual("あいうえ", gamedata.getローレシアの王子の名前())

	def test名前2(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("あいう")
		self.assertEqual("あいう　", gamedata.getローレシアの王子の名前())

	def test名前3(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("あいうえお")
		self.assertEqual("あいうえ", gamedata.getローレシアの王子の名前());
