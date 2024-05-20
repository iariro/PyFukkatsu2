
#**
#* 不正なアイテムの例外。
#* @author kumagai
#*/
class InvalidItemException(Exception):
	#**
	#* 基底クラスを初期化し例外オブジェクトを構築。
	#* @param itemCount アイテム数
	#*/
	def __init__(self, itemCount):
		self.message = "アイテム{}個は多過ぎ".format(itemCount)
