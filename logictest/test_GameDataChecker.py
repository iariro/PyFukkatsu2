import unittest
from logic.ItemAndEquipment import ItemAndEquipment
from logic.GameData import GameData
from logic import GameDataChecker
from logic.Player import Player

class JumonTest(unittest.TestCase):

	def test(self):
		gamedata = GameData()

		gamedata.セーブポイント = 2
		gamedata.setローレシアの王子の名前("とんぬら")
		#gamedata.ゴールド = 48362
		#gamedata.バリエーション = 14
		#gamedata.月のかけら = True
		#gamedata.水門 = True
		#gamedata.水のはごろも = False
		#gamedata.船 = True
		#gamedata.少女 = True
		gamedata.サマルトリア = 3
		#gamedata.命の紋章 = True
		#gamedata.水の紋章 = True
		#gamedata.月の紋章 = True
		#gamedata.星の紋章 = True
		#gamedata.太陽の紋章 = True

		ro = Player(経験値=1000000)
		#ro.itemCollection.append(ItemAndEquipment(name='ふっかつのたま'))
		gamedata.playerCollection.append(ro)

		sa = Player(経験値=1000000)
		gamedata.playerCollection.append(sa)

		mu = Player(経験値=1000000)
		gamedata.playerCollection.append(mu)

		results = list(GameDataChecker.checkAll(gamedata))
		find = False
		for result in results:
			if ('SavePointChecker' == result[0]) and ('船を手に入れていないのにラダトーム城には行けないはずです。' == result[1][0]):
				find = True
		self.assertTrue(find)

