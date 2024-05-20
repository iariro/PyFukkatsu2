import unittest
from logic.JumonBitArray import JumonBitArray
from logic.GameData import GameData
from logic.ItemAndEquipment import ItemAndEquipment
from logic.ExtendedGameDataBitArray import ExtendedGameDataBitArray
from logic.Player import Player

#**
#* JumonBitArray, GameData, ExtendedGameDataBitArrayのテスト。
#*/
class GameDataBitArrayTest(unittest.TestCase):
	def testConstructorIndexer(self):
		byteArray = [ 0x26 ]

		array = JumonBitArray(byteArray=byteArray)

		self.assertEqual(6, array.size())
		self.assertTrue(array.get(0))
		self.assertFalse(array.get(1))
		self.assertFalse(array.get(2))
		self.assertTrue(array.get(3))
		self.assertTrue(array.get(4))
		self.assertFalse(array.get(5))

	def testCount(self):
		array = JumonBitArray(size=6)
		self.assertEqual(6, array.size())

	def testGetAsInt(self):
		array = JumonBitArray([ 0x26 ])
		self.assertEqual(0x26, array.getAsInt(0, 6))

	def testGetPart(self):
		array = JumonBitArray(byteArray=[ 0x26 ])
		part = array.getPart(1, 3)

		self.assertFalse(part.get(0))
		self.assertFalse(part.get(1))
		self.assertTrue(part.get(2))

	def testGameDataBitArray1(self):
		gamedata = GameData()

		ro = Player(経験値=10000)
		sa = Player(経験値=20000)
		mu = Player(経験値=30000)

		ro.itemCollection.append(ItemAndEquipment(code=10))

		gamedata.セーブポイント = 5
		gamedata.setローレシアの王子の名前("とんぬら")
		gamedata.ゴールド = 12345
		gamedata.バリエーション = 11
		gamedata.月のかけら = True
		gamedata.水門 = True
		gamedata.水のはごろも = False
		gamedata.船 = False
		gamedata.少女 = False
		gamedata.サマルトリア = 2
		gamedata.命の紋章 = True
		gamedata.水の紋章 = True
		gamedata.月の紋章 = False
		gamedata.星の紋章 = True
		gamedata.太陽の紋章 = True
		gamedata.playerCollection.append(ro)
		gamedata.playerCollection.append(sa)
		gamedata.playerCollection.append(mu)

		array = ExtendedGameDataBitArray(gamedata=gamedata)
		playerCollection = array.getPlayerCollection()

		self.assertEqual(5, array.getセーブポイント())
		self.assertEqual("とんぬら", array.getローレシアの王子の名前())
		self.assertEqual(12345, array.getゴールド())
		self.assertEqual(11, array.getバリエーション())
		self.assertTrue(array.get月のかけら())
		self.assertTrue(array.get水門())
		self.assertFalse(array.get水のはごろも())
		self.assertFalse(array.get船())
		self.assertFalse(array.get少女())
		self.assertEqual(2, array.getサマルトリア())
		self.assertTrue(array.get命の紋章())
		self.assertTrue(array.get水の紋章())
		self.assertFalse(array.get月の紋章())
		self.assertTrue(array.get星の紋章())
		self.assertTrue(array.get太陽の紋章())
		self.assertEqual(3, len(playerCollection))
		self.assertEqual(10000, playerCollection[0].経験値)
		self.assertEqual(1, len(playerCollection[0].itemCollection))
		self.assertEqual(10, playerCollection[0].itemCollection[0].getCode())
		self.assertEqual(20000, playerCollection[1].経験値)
		self.assertEqual(0, len(playerCollection[1].itemCollection))
		self.assertEqual(30000, playerCollection[2].経験値)
		self.assertEqual(0, len(playerCollection[2].itemCollection))

	def testGameDataBitArray2(self):
		gamedata = GameData()

		ro = Player(10000)
		sa = Player(20000)
		mu = Player(30000)

		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))
		ro.itemCollection.append(ItemAndEquipment(1))

		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))
		sa.itemCollection.append(ItemAndEquipment(1))

		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))
		mu.itemCollection.append(ItemAndEquipment(1))

		gamedata.setローレシアの王子の名前("とんぬら")
		gamedata.playerCollection.append(ro)
		gamedata.playerCollection.append(sa)
		gamedata.playerCollection.append(mu)

		array = ExtendedGameDataBitArray(gamedata)

		self.assertEqual(314, array.size())
