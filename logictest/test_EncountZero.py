import unittest
from logic.GameData import GameData
from logic.Jumon import Jumon
from logic.Player import Player
from logic.ItemAndEquipment import ItemAndEquipment

class EncountZeroTest(unittest.TestCase):
	def test1(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("えにくす")
		compressed = gamedata.trickEncountZero()
		jumon = Jumon(codeArray=compressed.getJumonCode())
		self.assertEqual("ろごこさぽのぴわぎずぞばぶぼぴぺあう", jumon.getJumonStringNoReturn())

	def test2(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("えにくす")
		rooreshia = Player(経験値=0)
		gamedata.playerCollection.append(rooreshia)
		rooreshia.itemCollection.append(ItemAndEquipment(code=1))
		rooreshia.itemCollection.append(ItemAndEquipment(code=2))
		compressed = gamedata.trickEncountZero()
		jumon = Jumon(codeArray=compressed.getJumonCode())
		self.assertEqual("ろごきひたゆへしせつとなぬのひまむうゆ", jumon.getJumonStringNoReturn())

	def test3(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("えにくす")
		rooreshia = Player(経験値=0)
		gamedata.playerCollection.append(rooreshia)
		rooreshia.itemCollection.append(ItemAndEquipment(code=1))
		rooreshia.itemCollection.append(ItemAndEquipment(code=2))
		samarutoria = Player(経験値=0)
		gamedata.playerCollection.append(samarutoria)
		samarutoria.itemCollection.append(ItemAndEquipment(code=3))
		compressed = gamedata.trickEncountZero()
		jumon = Jumon(codeArray=compressed.getJumonCode())
		self.assertEqual("ろごきしあへゆとぞいえおきけさそちじへまむもがぼ", jumon.getJumonStringNoReturn())

	def test4(self):
		gamedata = GameData()
		gamedata.setローレシアの王子の名前("えにくす")
		rooreshia = Player(経験値=0)
		samarutoria = Player(経験値=0)
		muunburuku = Player(経験値=0)
		gamedata.playerCollection.append(rooreshia)
		rooreshia.itemCollection.append(ItemAndEquipment(code=1))
		rooreshia.itemCollection.append(ItemAndEquipment(code=2))
		gamedata.playerCollection.append(samarutoria)
		samarutoria.itemCollection.append(ItemAndEquipment(code=3))
		gamedata.playerCollection.append(muunburuku)
		muunburuku.itemCollection.append(ItemAndEquipment(code=4, equipment=True))
		compressed = gamedata.trickEncountZero()
		jumon = Jumon(codeArray=compressed.getJumonCode())
		self.assertEqual("ろごきせうまぐほぽこしすそちてぬのぼゆらるろぜおきけさたにね", jumon.getJumonStringNoReturn())
