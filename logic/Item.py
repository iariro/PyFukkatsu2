
#**
#* アイテム。
#* @author kumagai
#*/
class Item:
	#**
	#* アイテムオブジェクトを構築。
	#* @param name 名前
	#* @param itemKind アイテムの種類
	#* @param valid true=採用アイテム／false=没アイテム
	#* @param ローレシア王子装備可 true=ローレシア王子装備可
	#* @param サマルトリア王子装備可 true=サマルトリア王子装備可
	#* @param ムーンブルク王女装備可 true=ムーンブルク王女装備可
	#* @param getLevel 0=無制限 1=２人必要 2=３人必要 3=船必要 4=月のかけら必要
	#*/
	def __init__(self, name, itemKind, valid, ローレシア王子装備可, サマルトリア王子装備可, ムーンブルク王女装備可, getLevel):
		self.name = name
		self.itemKind = itemKind
		self.valid = valid
		self.ローレシア王子装備可 = ローレシア王子装備可
		self.サマルトリア王子装備可 = サマルトリア王子装備可
		self.ムーンブルク王女装備可 = ムーンブルク王女装備可
		self.getLevel = getLevel
