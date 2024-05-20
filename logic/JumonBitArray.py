
#/**
# * ビット配列基底部。
# */
class JumonBitArray:

	#**
	#* 8ビットのうち上位6ビットからビット配列を構築。
	#* @param byteArray バイト配列
	#*/
	def __init__(self, byteArray=None, size=None, array=None):
		if byteArray:
			self.array = []
			for b in byteArray:
				for i in range(6):
					self.array.append((b & (1 << (5 - i))) > 0)
		elif size:
			self.array = [False] * size
		elif array:
			self.array = array
		else:
			self.array = []

	def size(self):
		return len(self.array)

	def get(self, i):
		return self.array[i]

	def set(self, startOnArray, value):
		self.array[startOnArray] = value

	def add(self, value):
		self.array.append(value)

	#**
	#* 指定部分をint値として取得。
	#* @param start 取得開始ビット位置
	#* @param bitsize ビットサイズ
	#* @return 取得したint値
	#*/
	def getAsInt(self, start, bitsize):
		ret = 0
		for i in range(bitsize):
			ret = (ret << 1) + (1 if self.get(start + i) else 0)
		return ret

	#**
	#* 指定の位置に指定の値をセット。
	#* 値のセット開始位置は上位ビットで値のセット終端位置は下位ビットである
	#* ことに注意。
	#* @param startOnArray 配列中のセット開始位置
	#* @param value セットする値
	#* @param startOnValue 値のセット開始ビット位置
	#* @param endOnValue 値のセット終端ビット位置
	#*/
	def setInt(self, startOnArray, value, startOnValue, endOnValue):
		for i in range(startOnValue, endOnValue-1, -1):
			self.set(startOnArray, (value & 1 << i) > 0)
			startOnArray += 1

	#**
	#* 部分配列を取得。
	#* @param start 取得開始ビット位置
	#* @param bitsize 取得ビットサイズ
	#* @return 部分配列
	#*/
	def getPart(self, start, bitsize):
		return JumonBitArray(array=[self.array[start + i] for i in range(bitsize)])

	#**
	#* 内容を文字列化して取得。デバッグ用。
	#* @return 文字列化した内容
	#*/
	def toString(self):
		return '{} : {}'.format(len(self.array), ''.join(['1' if b else '0' for b in self.array]))
