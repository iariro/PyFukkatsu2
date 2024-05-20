import unittest
from logic import ItemCollection
from logic.ItemAndEquipment import ItemAndEquipment

class ItemTest(unittest.TestCase):
	def testひのきのぼう(self):
		self.assertEqual(
			1,
			ItemCollection.getCodeFromName("ひのきのぼう"))

	def testやくそう(self):
		self.assertEqual(
			60,
			ItemCollection.getCodeFromName("やくそう"))

	def testあぶないみずぎ(self):
		self.assertEqual(
			63,
			ItemCollection.getCodeFromName("あぶないみずぎ"))

	def test見つからない(self):
		self.assertEqual(
			-1,
			ItemCollection.getCodeFromName("あいうえお"))

	def testItemAndEquipment01(self):
		itemAndEquipment = ItemAndEquipment(code=73)
		self.assertEqual(73, itemAndEquipment.getCode())
		self.assertEqual("はやぶさのけん", itemAndEquipment.item.name)
		self.assertTrue(itemAndEquipment.equipment)

	def testItemAndEquipment02(self):
		itemAndEquipment = ItemAndEquipment(name="はがねのつるぎ", equipment=True)
		self.assertEqual(74, itemAndEquipment.getCode())
