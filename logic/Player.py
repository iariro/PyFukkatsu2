from logic.InvalidItemException import InvalidItemException
from logic import InvalidItemCountException
from logic.ItemAndEquipment import ItemAndEquipment

#**
#* プレイヤー情報。
#*/
class Player:

	#**
	#* 経験値，アイテム情報を受け、プレイヤー情報を構築。
	#* @param exist true=存在する／false=しない
	#* @param 経験値 経験値
	#* @param itemCount アイテムの個数
	#* @param itemBitArray アイテム情報を内容とするビット配列
	#*/
	def __init__(self, exist=True, 経験値=0, itemCount=0, itemBitArray=None):
		self.exist = exist
		self.経験値 = 経験値
		self.itemCollection = []

		if itemCount > 8:
			# アイテムは多過ぎる。

			if exist:
				raise InvalidItemCountException(itemCount)

		for i in range(itemCount):
			index = itemBitArray.getAsInt(7 * i, 7)
			if index >= 1 and index <= 0x80 and (index % 0x40 >= 1) and (index % 0x40 <= 0x3f):
				# アイテムの値は正しい。
				self.itemCollection.append(ItemAndEquipment(code=index))
			else:
				# アイテムの値は不正。
				raise InvalidItemException(i, itemCount, index)
