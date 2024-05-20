
#**
#* 全角数字文字列。
#* @author kumagai
#*/
class NumberString:
	#**
	#* 指定の数値を全角数字文字列化しオブジェクトを構築。
	#* @param num 数値
	#*/
	def __init__(self, num):
		self.str = ""

		while num > 0:
			c = chr(ord('０') + (num % 10))
			self.str = c + str
			num //= 10

	#**
	#* 全角数字文字列を取得。
	#* @see java.lang.Object#toString()
	#* @return 全角数字文字列
	#*/
	def toString(self):
		return self.str
