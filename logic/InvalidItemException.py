
#**
#* 不正なアイテムの例外。
#* @author kumagai
#*/
class InvalidItemException(Exception):
	#**
	#* 基底クラスを初期化し例外オブジェクトを構築。
	#* @param index 位置
	#* @param itemCount アイテム数
	#* @param item 項目
	#*/
	def __init__(self, index, itemCount, item):
		self.message = "アイテム{}/{}={}が不正です".format(index, itemCount, item)

	def __str__(self):
		return self.message
