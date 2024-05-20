import unittest
from logic.CompressedGameDataBitArray import CompressedGameDataBitArray
from logic.ExtendedGameDataBitArray import ExtendedGameDataBitArray
from logic.ItemAndEquipment import ItemAndEquipment
from logic.Jumon import Jumon
from logic.GameData import GameData
from logic import GameDataChecker
from logic.Player import Player

class JumonTest(unittest.TestCase):
	def testあいうえお(self):
		jumon = Jumon("あいうえお")

		self.assertEqual(0, jumon.get(0))
		self.assertEqual(1, jumon.get(1))
		self.assertEqual(2, jumon.get(2))
		self.assertEqual(3, jumon.get(3))
		self.assertEqual(4, jumon.get(4))

	def test不正な文字(self):
		try:
			Jumon("漢")
			self.fail()
		except:
			pass

	def testぺぺぺ呪文からデータ取得(self):
		stringBuilder = "ゆうて いみや おうきむ" + \
			"こうほ りいゆ うじとり" + \
			"やまあ きらぺ ぺぺぺぺ" + \
			"ぺぺぺ ぺぺぺ ぺぺぺぺ" + \
			"ぺぺぺ ぺぺぺ ぺぺぺぺ ぺぺ"

		jumon = Jumon(stringBuilder)

		compressedGameDataBitArray = CompressedGameDataBitArray(byteArray=jumon.getPlainArray())
		gamedata = GameData(bitArray=ExtendedGameDataBitArray(bitArray=compressedGameDataBitArray))

		playerCollection = gamedata.playerCollection

		self.assertEqual(1, gamedata.セーブポイント)
		self.assertEqual("もょもと", gamedata.getローレシアの王子の名前())
		self.assertEqual(27671, gamedata.ゴールド)
		self.assertEqual(3, gamedata.バリエーション)
		self.assertFalse(gamedata.月のかけら)
		self.assertFalse(gamedata.水門)
		self.assertFalse(gamedata.水のはごろも)
		self.assertFalse(gamedata.船)
		self.assertTrue(gamedata.少女)
		self.assertEqual(1, gamedata.サマルトリア)
		self.assertTrue(gamedata.命の紋章)
		self.assertTrue(gamedata.水の紋章)
		self.assertFalse(gamedata.月の紋章)
		self.assertFalse(gamedata.星の紋章)
		self.assertTrue(gamedata.太陽の紋章)
		self.assertEqual(3, len(playerCollection))
		self.assertEqual(942197, playerCollection[0].経験値)
		self.assertEqual(0, len(playerCollection[0].itemCollection))
		self.assertEqual(
			compressedGameDataBitArray.getチェックサム１(),
			compressedGameDataBitArray.getチェックサム２())

	def testはにまる呪文からデータ取得(self):
		jumon = Jumon(
				"こゆわ　るめむ　すじぐが\r\n" +
				"れろぱ　むゆほ　らべにぜ\r\n" +
				"ぶぽべ　あきい　きりくす\r\n" +
				"ずふべ　そのた　らわぷそ\r\n" +
				"ずびぐ　つらひ　きぴたふ　へ")

		compressedGameDataBitArray = CompressedGameDataBitArray(jumon.getPlainArray())
		gamedataBitArray = ExtendedGameDataBitArray(bitArray=compressedGameDataBitArray)
		gamedata = GameData(gamedataBitArray)

		playerCollection = gamedata.playerCollection

		self.assertEqual(5, gamedata.セーブポイント)
		self.assertEqual("はにまる", gamedata.getローレシアの王子の名前())
		self.assertEqual(48362, gamedata.ゴールド)
		self.assertEqual(14, gamedata.バリエーション)
		self.assertTrue(gamedata.月のかけら)
		self.assertTrue(gamedata.水門)
		self.assertFalse(gamedata.水のはごろも)
		self.assertTrue(gamedata.船)
		self.assertTrue(gamedata.少女)
		self.assertEqual(3, gamedata.サマルトリア)
		self.assertTrue(gamedata.命の紋章)
		self.assertTrue(gamedata.水の紋章)
		self.assertTrue(gamedata.月の紋章)
		self.assertTrue(gamedata.星の紋章)
		self.assertTrue(gamedata.太陽の紋章)
		self.assertEqual(3, len(playerCollection))

		self.assertEqual(1000000, playerCollection[0].経験値)
		self.assertEqual(8, len(playerCollection[0].itemCollection))
		self.assertEqual(16, playerCollection[0].itemCollection[0].getCode())
		self.assertEqual(64 + 9, playerCollection[0].itemCollection[1].getCode())
		self.assertEqual(64 + 27, playerCollection[0].itemCollection[2].getCode())
		self.assertEqual(64 + 32, playerCollection[0].itemCollection[3].getCode())
		self.assertEqual(64 + 35, playerCollection[0].itemCollection[4].getCode())
		self.assertEqual(57, playerCollection[0].itemCollection[5].getCode())
		self.assertEqual(12, playerCollection[0].itemCollection[6].getCode())
		self.assertEqual(23, playerCollection[0].itemCollection[7].getCode())

		self.assertEqual(1000000, playerCollection[1].経験値)
		self.assertEqual(8, len(playerCollection[1].itemCollection))
		self.assertEqual(64 + 9, playerCollection[1].itemCollection[0].getCode())
		self.assertEqual(64 + 19, playerCollection[1].itemCollection[1].getCode())
		self.assertEqual(64 + 29, playerCollection[1].itemCollection[2].getCode())
		self.assertEqual(40, playerCollection[1].itemCollection[3].getCode())
		self.assertEqual(39, playerCollection[1].itemCollection[4].getCode())
		self.assertEqual(50, playerCollection[1].itemCollection[5].getCode())
		self.assertEqual(64 + 33, playerCollection[1].itemCollection[6].getCode())
		self.assertEqual(8, playerCollection[1].itemCollection[7].getCode())

		self.assertEqual(1000000, playerCollection[2].経験値)
		self.assertEqual(6, len(playerCollection[2].itemCollection))
		self.assertEqual(64 + 4, playerCollection[2].itemCollection[0].getCode())
		self.assertEqual(64 + 19, playerCollection[2].itemCollection[1].getCode())
		self.assertEqual(29, playerCollection[2].itemCollection[2].getCode())
		self.assertEqual(61, playerCollection[2].itemCollection[3].getCode())
		self.assertEqual(41, playerCollection[2].itemCollection[4].getCode())
		self.assertEqual(11, playerCollection[2].itemCollection[5].getCode())

		self.assertEqual(
			compressedGameDataBitArray.getチェックサム１(),
			compressedGameDataBitArray.getチェックサム２())

	def testはにまるデータから呪文生成(self):
		gamedata = GameData()

		gamedata.セーブポイント = 5
		gamedata.setローレシアの王子の名前("はにまる")
		gamedata.ゴールド = 48362
		gamedata.バリエーション = 14
		gamedata.月のかけら = True
		gamedata.水門 = True
		gamedata.水のはごろも = False
		gamedata.船 = True
		gamedata.少女 = True
		gamedata.サマルトリア = 3
		gamedata.命の紋章 = True
		gamedata.水の紋章 = True
		gamedata.月の紋章 = True
		gamedata.星の紋章 = True
		gamedata.太陽の紋章 = True

		ro = Player(経験値=1000000)
		ro.itemCollection.append(ItemAndEquipment(code=16))
		ro.itemCollection.append(ItemAndEquipment(code=64 + 9))
		ro.itemCollection.append(ItemAndEquipment(code=64 + 27))
		ro.itemCollection.append(ItemAndEquipment(code=64 + 32))
		ro.itemCollection.append(ItemAndEquipment(code=64 + 35))
		ro.itemCollection.append(ItemAndEquipment(code=57))
		ro.itemCollection.append(ItemAndEquipment(code=12))
		ro.itemCollection.append(ItemAndEquipment(code=23))
		gamedata.playerCollection.append(ro)

		sa = Player(経験値=1000000)
		sa.itemCollection.append(ItemAndEquipment(code=64 + 9))
		sa.itemCollection.append(ItemAndEquipment(code=64 + 19))
		sa.itemCollection.append(ItemAndEquipment(code=64 + 29))
		sa.itemCollection.append(ItemAndEquipment(code=40))
		sa.itemCollection.append(ItemAndEquipment(code=39))
		sa.itemCollection.append(ItemAndEquipment(code=50))
		sa.itemCollection.append(ItemAndEquipment(code=64 + 33))
		sa.itemCollection.append(ItemAndEquipment(code=8))
		gamedata.playerCollection.append(sa)

		mu = Player(経験値=1000000)
		mu.itemCollection.append(ItemAndEquipment(code=64 + 4))
		mu.itemCollection.append(ItemAndEquipment(code=64 + 19))
		mu.itemCollection.append(ItemAndEquipment(code=29))
		mu.itemCollection.append(ItemAndEquipment(code=61))
		mu.itemCollection.append(ItemAndEquipment(code=41))
		mu.itemCollection.append(ItemAndEquipment(code=11))
		gamedata.playerCollection.append(mu)

		extendedGameDataBitArray = ExtendedGameDataBitArray(gamedata=gamedata)
		compressedGameDataBitArray = CompressedGameDataBitArray(array=extendedGameDataBitArray)
		jumon = Jumon(codeArray=compressedGameDataBitArray.getJumonCode())

		self.assertEqual(
			"こゆわ るめむ すじぐが\r\n" +
			"れろぱ むゆほ らべにぜ\r\n" +
			"ぶぽべ あきい きりくす\r\n" +
			"ずふべ そのた らわぷそ\r\n" +
			"ずびぐ つらひ きぴたふ へ",
			jumon.getJumonStringOnly())

	def testとんぬら呪文からデータ取得(self):
		jumon = Jumon("ぬもじ ばざか すごぜぶ ぴねふ みやり わげ")

		compressedGameDataBitArray = CompressedGameDataBitArray(jumon.getPlainArray())
		gamedata = GameData(ExtendedGameDataBitArray(bitArray=compressedGameDataBitArray))

		playerCollection = gamedata.playerCollection

		self.assertEqual(0, gamedata.セーブポイント)
		self.assertEqual("とんぬら", gamedata.getローレシアの王子の名前())
		self.assertEqual(0, gamedata.ゴールド)
		self.assertEqual(0, gamedata.バリエーション)
		self.assertFalse(gamedata.月のかけら)
		self.assertFalse(gamedata.水門)
		self.assertFalse(gamedata.水のはごろも)
		self.assertFalse(gamedata.船)
		self.assertFalse(gamedata.少女)
		self.assertEqual(0, gamedata.サマルトリア)
		self.assertFalse(gamedata.命の紋章)
		self.assertFalse(gamedata.水の紋章)
		self.assertFalse(gamedata.月の紋章)
		self.assertFalse(gamedata.星の紋章)
		self.assertFalse(gamedata.太陽の紋章)
		self.assertEqual(1, len(playerCollection))
		self.assertEqual(
			compressedGameDataBitArray.getチェックサム１(),
			compressedGameDataBitArray.getチェックサム２())

	def testとんぬらデータから呪文生成(self):
		gamedata = GameData()

		gamedata.セーブポイント = 0
		gamedata.setローレシアの王子の名前("とんぬら")
		gamedata.ゴールド = 0
		gamedata.バリエーション = 0
		gamedata.月のかけら = False
		gamedata.水門 = False
		gamedata.水のはごろも = False
		gamedata.船 = False
		gamedata.少女 = False
		gamedata.サマルトリア = 0
		gamedata.命の紋章 = False
		gamedata.水の紋章 = False
		gamedata.月の紋章 = False
		gamedata.星の紋章 = False
		gamedata.太陽の紋章 = False
		gamedata.playerCollection.append(Player(0))

		extendedGameDataBitArray = ExtendedGameDataBitArray(gamedata=gamedata)
		compressedGameDataBitArray = CompressedGameDataBitArray(array=extendedGameDataBitArray)
		jumon = Jumon(codeArray=compressedGameDataBitArray.getJumonCode())

		self.assertEqual(
			"ぬもじ ばざか すごぜぶ\r\nぴねふ みやり わげ",
			jumon.getJumonStringOnly())

	def testろろのあ呪文からデータ取得(self):
		stringBuilder = "いひさ さぶけ かひぼぴ" + \
			"べぴせ じばぐ とけとざ" + \
			"なする ぬしに ぬにみが" + \
			"ためろ たらざ たまあこ" + \
			"つえの うびじ ちむやし むめ"
		jumon = Jumon(stringBuilder)

		compressedGameDataBitArray = CompressedGameDataBitArray(jumon.getPlainArray())
		gamedata = GameData(ExtendedGameDataBitArray(bitArray=compressedGameDataBitArray))

		playerCollection = gamedata.playerCollection

		self.assertEqual("ろろのあ", gamedata.getローレシアの王子の名前())
		self.assertEqual(65535, gamedata.ゴールド)
		self.assertEqual(
			compressedGameDataBitArray.getチェックサム１(),
			compressedGameDataBitArray.getチェックサム２())
		self.assertEqual(1000000, playerCollection[0].経験値)

	def testとんぬら(self):
		jumon = Jumon(
				"えほが　つさみ　けろりむ\r\n" +
				"まぞず　ざなま　ねざぽへ\r\n" +
				"かるぼ　れにぜ　がつへよ\r\n" +
				"りひべ　ぬいぴ　しまぱわ\r\n" +
				"られざ　わぺく　しぎにさ　す")

		compressedGameDataBitArray = CompressedGameDataBitArray(jumon.getPlainArray())
		gamedata = GameData(ExtendedGameDataBitArray(bitArray=compressedGameDataBitArray))

		self.assertEqual("とんぬら", gamedata.getローレシアの王子の名前())
		self.assertEqual(
			compressedGameDataBitArray.getチェックサム１(),
			compressedGameDataBitArray.getチェックサム２())

	def test福引券呪文からデータ取得(self):
		jumon = Jumon("わひは てぷゆ ぷぴほら" +
				"りるぼ むよみ ぼるむぷ" +
				"すぜれ おじぐ ぜぬびぴ" +
				"しずる えざれ きにぺち" +
				"ばぱぞ ちぺば ともさぽ ひけ")

		compressedGameDataBitArray = CompressedGameDataBitArray(jumon.getPlainArray())
		gamedataBitArray = ExtendedGameDataBitArray(bitArray=compressedGameDataBitArray)

		self.assertEqual(314, gamedataBitArray.size())
		self.assertEqual(
			compressedGameDataBitArray.getチェックサム１(),
			compressedGameDataBitArray.getチェックサム２())

		self.assertEqual(
			"わひは てぷゆ ぷぴほら\r\n"+
			"りるぼ むよみ ぼるむぷ\r\n"+
			"すぜれ おじぐ ぜぬびぴ\r\n"+
			"しずる えざれ きにぺち\r\n"+
			"ばぱぞ ちぺば ともさぽ ひけ",
			Jumon(codeArray=CompressedGameDataBitArray(array=gamedataBitArray).getJumonCode()).getJumonStringOnly())

	def testこはやし１呪文からデータ取得(self):
		jumon = Jumon(
				"すひぞ ぶたう とあやが" +
				"げくさ せがば やねいり" +
				"ぐぷは ほぞれ ぱれぎば" +
				"ぽした とずぷ ゆびうれ" +
				"ぽぽぽ")

		compressed = CompressedGameDataBitArray(jumon.getPlainArray())
		extended = ExtendedGameDataBitArray(bitArray=compressed)

		self.assertEqual("こはやし", extended.getローレシアの王子の名前())
		self.assertEqual(3, extended.getゴールド())

	def testこはやし２呪文からデータ取得(self):
		jumon = Jumon(
				"ぐぷぱ ほぞが てあゆが" +
				"ごほは めぞぱ れまうに" +
				"すてぎ ごぐぼ わのぱお" +
				"くかけ おりの なけじの")

		gamedata = GameData(ExtendedGameDataBitArray(bitArray=CompressedGameDataBitArray(jumon.getPlainArray())))

		playerCollection = gamedata.playerCollection

		self.assertEqual("こはよし", gamedata.getローレシアの王子の名前())
		self.assertEqual(2, len(playerCollection))
		self.assertEqual(57412, playerCollection[0].経験値)
