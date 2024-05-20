
#**
#* 不正な文字検出時の例外。
#* @author kumagai
#*/
class IllegalCharacterException(Exception):
	#**
	#* 基底クラスを初期化し例外オブジェクトを構築。
	#* @param item 文字列項目
	#* @param index 文字位置
	#* @param ch 不正な文字
	#*/
	def __init__(self, item, index, ch):
		self.item = item
		self.index = index
		self.ch = ch

	def __str__(self):
		return self.item + "の" + self.index + "文字目“" + self.ch + "”が不正です"
