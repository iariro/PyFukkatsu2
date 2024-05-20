from logic.JumonBitArray import JumonBitArray

encountZeroMCK = [
	11765,  5600, 47076, 47076, 26668,  1369, 18922, 18922, 16560, 46575,
	52350, 52350, 60483, 12623, 16173, 16173, 64486,  2791,  7758,  7758,
	64212, 57856, 58408, 58408, 24052, 11253,  2313,  2313, 51346,  8017,
	63711, 63711, 60379, 23045, 50245
]

encountZeroHK = [
	61622, 30811,     0,     0, 63788, 17412,  8706, 59693, 37105, 29813,
		1591,  2945,  2426, 52262, 25139, 14723, 45815, 40282, 34358, 47927,
	20769, 55334, 26675, 49295, 20676, 58585, 20065, 59185, 31490, 49549,
	36976, 33923, 53408, 26704, 64691, 35535, 34150, 36360, 47880, 41352,
	53281, 39078, 18547,  7188,  2602, 63769, 34842, 16429, 55774, 42100,
	40577, 17402,  5482, 50702, 39723, 16687,     0,     0,     0, 52379,
	37595, 36172, 36413, 19364, 19083, 10751,     0,     0,     0,     0,
		0,     0,  5271, 64253, 48511, 26258, 52069, 42419, 41583, 38166,
	62038, 19900,  8958,  9704, 56911, 44838, 43935, 22901, 20793, 55338,
	26677, 49292, 24646, 64664, 31340,  3457, 45101, 43168, 20592,
	58499, 33527, 34138, 36374, 47879,
	57046, 24540,  8025, 53165, 27500,  1281, 62006, 33079, 41622, 43367,
	27806, 12911, 56598, 27307, 14831,  9434,   409, 61562, 46214, 23107,
	60704, 29360, 49524, 44033, 34907, 31744, 14880, 57628, 28814, 14407,
		9230,  4615, 38905, 36829, 34799, 34774, 30588,  3881,  2862, 63899,
		4449, 13501, 60136, 17859,  7916, 16321, 57313, 45041,  7126, 15708,
	54837, 25472, 51692, 44141, 28187, 15287, 19564, 61101, 31724,  3393,
	16013,  5116, 15721,  9881, 46478, 23239, 60770, 48682, 41753, 22806,
	10411, 57539, 39302, 18659,  7260, 50869, 27584,  1367, 16038, 58207,
	43771, 38268, 34309, 19352, 55744, 42107, 28208, 51988, 55345, 39054,
	18535,  7198,  2607,  2477, 61504, 46235,   911,  2397, 15491, 60119,
	46442, 38414, 45867, 20751,
	27209, 62757, 35364, 47390, 22703, 55489, 21581,  5675, 29593, 12630,
	54288, 27144, 51464, 24740, 12370, 54418, 65509, 49139, 40952, 32587,
	65444, 33758, 30072, 62983, 52280, 25148, 51506, 24761, 49386, 44238,
	40700, 32713, 54025, 24862, 12431, 59633, 19541,  7687,   953,  2374,
	15980, 12161,  7034, 15626,  6821,   488, 52303, 24074, 49712, 39220,
	18618,  8317, 11315, 57999, 31197,  1219, 49735, 42242, 21121,  8666,
	56406, 42672, 43892, 25869, 26771, 49375, 23650, 59050, 35705, 34237,
	45672, 28067, 64907, 35411, 34088, 17044, 55654, 42024, 21012, 53542,
	36307, 32452,  4053, 51179, 42964, 26493, 63391, 29525,  7552,  2784,
	13767,  9966, 10208, 10087, 55186, 37861, 33420, 47466, 37934, 18967,
	10673, 57422, 48284, 23150
]

#**
#* 最大312ビットに圧縮されたゲームデータビット配列。
#*/
class CompressedGameDataBitArray(JumonBitArray):

	#**
	#* ゲームデータビット配列を受けて、312文字以内に収まるようビット配列を
	#* 構築。
	#* @param array ゲームデータビット配列
	#*/
	def __init__(self, byteArray=None, array=None):
		if byteArray:
			super().__init__(byteArray=byteArray)
		elif array:
			super().__init__()
			size = array.size()
			overflow = False

			if size == 314:
				# 314ビットの配列が指定された。

				overflow = True
				size = 312

			for i in range(size):
				self.add(array.get(i))

			if overflow:
				# オーバーした。

				self.set(64, array.get(312))
				self.set(65, array.get(313))

			# チェックサム埋め込み。
			checksum = self.getチェックサム２()
			self.setInt(0, checksum, 4, 0)
			self.setInt(66, checksum, 10, 5)

	#**
	#* 埋め込まれたチェックサムを取得。
	#* @return チェックサム
	#*/
	def getチェックサム１(self):
		return self.getAsInt(0, 5) + (self.getAsInt(66, 6) << 5)

	#**
	#* チェックサムを算出。
	#* @return チェックサム
	#*/
	def getチェックサム２(self):
		n = self.size() // 8

		# チェックサムを求める。
		checksum = n * 257

		for t in range(n-1, -1, -1):
			b = 0

			for j in range(8):
				index = t * 8 + j

				if index >= 0 and index <= 4 or index >= 66 and index <= 71:
					# チェックサム部分、つまりチェックサム計算非対象部分である。
					pass
				else:
					# チェックサム計算対象部分である。
					b |= ((1 if self.get(index) else 0) << (8 - j - 1))

			for j in range(8):
				d = ((checksum & 0x8000) // 0x8000) + ((b & 0x80) // 0x80)

				checksum = (checksum * 2) % 0x10000
				b = (b * 2) % 0x0100

				if d == 1:
					checksum ^= 4129

		return checksum % 0x0800

	#**
	#* エンカウントゼロであるか判定する
	#* @return true=エンカウントゼロである／false=エンカウントゼロではない
	#*/
	def isEncountZero(self):
		return (self.getEncountZeroChecksum() & 0xfe3f) == 0xac3f

	#**
	#* エンカウントゼロであるか判定用のチェックサムを求める
	#* 0xfe3fとの論理積が0xac3fであればエンカウントゼロ呪文である
	#* @return エンカウントゼロであるか判定用のチェックサム
	#*/
	def getEncountZeroChecksum(self):
		checksum = encountZeroMCK[self.size() // 6 - 18]

		for i in range(self.size()):
			checksum ^= (encountZeroHK[i] * (1 if self.get(i) else 0))
		return checksum

	#**
	#* 末尾の正当性チェック。
	#* @return true=正当
	#*/
	def isValidTerminate(self):
		charNum = self.size() // 6 - 1

		if (charNum & 0x3) < 3:
			if self.size() >= charNum * 6 + 6:
				if self.get(charNum * 6 + 4) | self.get(charNum * 6 + 5):
					return False

		if (charNum & 0x3) < 2:
			if self.size() >= charNum * 6 + 4:
				if self.get(charNum * 6 + 2) | self.get(charNum * 6 + 3):
					return False

		if (charNum & 0x3) == 0:
			if self.size() >= charNum * 6 + 2:
				if self.get(charNum * 6) | self.get(charNum * 6 + 1):
					print("[{}]={} [{}]={}\n".format(
						charNum * 6 + 0,
						self.get(charNum * 6 + 0),
						charNum * 6 + 1,
						self.get(charNum * 6 + 1)))
					return False
		return True

	#**
	#* 呪文コード生成。
	#* @return 呪文コード
	#*/
	def getJumonCode(self):
		ret = [0] * (self.size() // 6)

		shift = self.getAsInt(3, 2) + 1

		for i in range(len(ret)):
			ret[i] = self.getAsInt(6 * i, 6)

			if i >= 1:
				# ２文字目以降。
				ret[i] = ((ret[i] + (ret[i - 1] + shift)) % 0x40)

		return ret

	#**
	#* ビット内容比較。
	#* @param compressed1 比較対象
	#*/
	def compare(self, compressed1):
		for i in range(304):
			if i < self.size() and i < len(compressed1):
				# 範囲内。
				if self.get(i) != compressed1.get(i):
					# 値は異なる。
					print("{}:{}, {}\n".format(i, self.get(i), compressed1.get(i)))
