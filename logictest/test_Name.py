import unittest
from logic import ローレシアの王子の名前テーブル
from logic.SamarutoriaMuunburukuName import SamarutoriaMuunburukuName

class NameTest(unittest.TestCase):
	def test01(self):
		self.assertEqual(
			10,
			ローレシアの王子の名前テーブル.hashmap['あ'])

	def test02(self):
		name = SamarutoriaMuunburukuName("くらけ゛")

		self.assertEqual("パウロ", name.サマルトリアの王子の名前)
		self.assertEqual("サマンサ", name.ムーンブルクの王女の名前)
