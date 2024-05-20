from logic.IllegalCharacterException import IllegalCharacterException
from logic.ItemAndEquipment import ItemAndEquipment
from logic.JumonBitArray import JumonBitArray
from logic.Player import Player

#**
#* ローレシアの王子の名前文字。
#*/
nameChar = [
	'あ', 'い', 'う', 'え', 'お',
	'か', 'き', 'く', 'け', 'こ',
	'さ', 'し', 'す', 'せ', 'そ',
	'た', 'ち', 'つ', 'て', 'と',
	'な', 'に', 'ぬ', 'ね', 'の',
	'は', 'ひ', 'ふ', 'へ', 'ほ',
	'ま', 'み', 'む', 'め', 'も',
	'や', 'ゆ', 'よ', 'ら', 'り',
	'る', 'れ', 'ろ', 'わ', 'を',
	'ん', 'っ', 'ゃ', 'ゅ', 'ょ',
	'゛', '゜', '　'
]

#**
#* 最大314ビットのゲームデータビット配列。
#*/
class ExtendedGameDataBitArray(JumonBitArray):
	#**
	#* 指定の文字のインデックスを取得する。
	#* @param ch 対象文字
	#* @return 指定の文字のインデックス
	#*/
	def getNameIndex(self, ch):
		for i in range(len(nameChar)):
			if nameChar[i] == ch:
				# 対象の文字である。
				return i

		return -1

	#**
	#* ゲームデータからビット配列を構築。
	#* @param gamedata ゲームデータ
	#*/
	def __init__(self, gamedata=None, bitArray=None):
		if gamedata:
			super().__init__()
			# 必要な領域計算。
			size = 72

			for i, player in enumerate(gamedata.playerCollection):
				size += 24 + 7 * len(player.itemCollection)

				if i < 2:
					# ２人目まで。
					size += 1

			if size < 104:
				# 104ビットに達していない。
				size = 104

			# 領域確保。
			for i in range(size):
				self.add(False)

			if size < 314:
				# 314ビット未満。

				# パディング分領域確保。チェックサム計算のために必要。
				for i in range(6 - size % 6):
					self.add(False)

			self.setセーブポイント(gamedata.セーブポイント)
			self.setローレシアの王子の名前(gamedata.getローレシアの王子の名前())
			self.setゴールド(gamedata.ゴールド)
			self.setバリエーション(gamedata.バリエーション)
			self.set月のかけら(gamedata.月のかけら)
			self.set水門(gamedata.水門)
			self.set水のはごろも(gamedata.水のはごろも)
			self.set船(gamedata.船)
			self.set少女(gamedata.少女)
			self.setサマルトリア(gamedata.サマルトリア)
			self.set命の紋章(gamedata.命の紋章)
			self.set水の紋章(gamedata.水の紋章)
			self.set月の紋章(gamedata.月の紋章)
			self.set星の紋章(gamedata.星の紋章)
			self.set太陽の紋章(gamedata.太陽の紋章)
			self.setPlayerCollection(gamedata.playerCollection)

		if bitArray:
			super().__init__(size=bitArray.size() + (2 if bitArray.size() == 312 else 0))

			if bitArray.size() < 63:
				# ビット数が少ない。
				raise Exception(len(bitArray) + "bitとは少なすぎです")

			for i in range(5, 63 + 1):
				self.set(i, bitArray.get(i))

			for i in range(72,  bitArray.size()):
				self.set(i, bitArray.get(i))

			if len(self.array) == 314:
				# オーバーフロー分がある。
				self.set(312, bitArray.get(64))
				self.set(313, bitArray.get(65))

	#**
	#* 埋め込まれたチェックサムを取得。
	#* @return チェックサム
	#*/
	def getチェックサム１(self):
		return self.getAsInt(0, 5) + (self.getAsInt(66, 6) << 5)

	#**
	#* セーブポイントを取得。
	#* @return セーブポイント
	#*/
	def getセーブポイント(self):
		return self.getAsInt(5, 3)

	#**
	#* セーブポイントを割り当てる。
	#* @param value セーブポイント
	#*/
	def setセーブポイント(self, value):
		super().setInt(5, value, 2, 0)

	#**
	#* ローレシアの王子の名前が正当かを取得。
	#* @return エラー文字列
	#*/
	def isValidローレシアの王子の名前(self):

		name3 = self.getAsInt( 8, 6)
		name2 = self.getAsInt(14, 2) << 4
		name2 += self.getAsInt(24, 2) << 1
		name1 = self.getAsInt(26, 6)
		name2 += self.getAsInt(40, 1)
		name4 = self.getAsInt(41, 6)
		name2 += self.getAsInt(47, 1) << 3

		name1 -= 10
		name2 -= 10
		name3 -= 10
		name4 -= 10

		if name1 >= 0 and name1 < 53 and \
			name2 >= 0 and name2 < 53 and \
			name3 >= 0 and name3 < 53 and \
			name4 >= 0 and name4 < 53:
			# エラーなし。

			return None
		else:
			# エラーあり。
			return "{} {} {} {}".format(name1, name2, name3, name4)

	#**
	#* ローレシアの王子の名前を取得。
	#* @return ローレシアの王子の名前
	#*/
	def getローレシアの王子の名前(self):

		name3 = self.getAsInt( 8, 6)
		name2 = self.getAsInt(14, 2) << 4
		name2 += self.getAsInt(24, 2) << 1
		name1 = self.getAsInt(26, 6)
		name2 += self.getAsInt(40, 1)
		name4 = self.getAsInt(41, 6)
		name2 += self.getAsInt(47, 1) << 3

		name1 -= 10
		name2 -= 10
		name3 -= 10
		name4 -= 10

		return "{}{}{}{}".format(
			nameChar[name1],
			nameChar[name2],
			nameChar[name3],
			nameChar[name4])

	#**
	#* ローレシアの王子の名前を取得。
	#* @param value ローレシアの王子の名前
	#*/
	def setローレシアの王子の名前(self, value):
		name1 = self.getNameIndex(value[0])
		name2 = self.getNameIndex(value[1])
		name3 = self.getNameIndex(value[2])
		name4 = self.getNameIndex(value[3])

		for i, name in enumerate((name1, name2, name3, name4)):
			if name < 0:
				# 名前i文字目が不正。
				raise IllegalCharacterException("ローレシアの王子の名前", 1 + i, value[i])

		name1 += 10
		name2 += 10
		name3 += 10
		name4 += 10

		self.setInt( 8, name3, 5, 0)
		self.setInt(14, name2, 5, 4)
		self.setInt(24, name2, 2, 1)
		self.setInt(26, name1, 5, 0)
		self.setInt(40, name2, 0, 0)
		self.setInt(41, name4, 5, 0)
		self.setInt(47, name2, 3, 3)

	#**
	#* ゴールドを取得。
	#* @return ゴールド値
	#*/
	def getゴールド(self):
		return (self.getAsInt(16, 8) << 8) + self.getAsInt(32, 8)

	#**
	#* ゴールドを設定。
	#* @param value ゴールド値
	#*/
	def setゴールド(self, value):
		self.setInt(32, value, 7, 0)
		self.setInt(16, value, 15, 8)

	#**
	#* バリエーションを取得。
	#* @return バリエーション値
	#*/
	def getバリエーション(self):
		return (self.getAsInt(48, 1) << 3) + self.getAsInt(56, 3)

	#**
	#* バリエーションを設定。
	#* @param value バリエーション値
	#*/
	def setバリエーション(self, value):
		self.setInt(48, value, 3, 3)
		self.setInt(56, value, 2, 0)

	#**
	#* 月のかけら情報を取得または設定。
	#* @return 月のかけらフラグ
	#*/
	def get月のかけら(self):
		return self.get(49)

	#**
	#* 月のかけら情報を設定。
	#* @param value 月のかけらフラグ
	#*/
	def set月のかけら(self, value):
		self.set(49, value)

	#**
	#* 水門情報を取得。
	#* @return 水門フラグ
	#*/
	def get水門(self):
		return self.get(50)

	#**
	#* 水門情報を設定。
	#* @param value 水門フラグ
	#*/
	def set水門(self, value):
		self.set(50, value)

	#**
	#* 水のはごろも情報を取得。
	#* @return 水のはごろもフラグ
	#*/
	def get水のはごろも(self):
		return self.get(51)

	#**
	#* 水のはごろも情報を設定。
	#* @param value 水のはごろもフラグ
	#*/
	def set水のはごろも(self, value):
		self.set(51, value)

	#**
	#* 船情報を取得。
	#* @return 船フラグ
	#*/
	def get船(self):
		return self.get(52)

	#**
	#* 船情報を設定。
	#* @param value 船フラグ
	#*/
	def set船(self, value):
		self.set(52, value)

	#**
	#* 少女情報を取得。
	#* @return 少女フラグ
	#*/
	def get少女(self):
		return self.get(53)

	#**
	#* 少女情報を設定。
	#* @param value 少女フラグ
	#*/
	def set少女(self, value):
		self.set(53, value)

	#**
	#* サマルトリア情報を取得。
	#* @return サマルトリアの王子フラグ
	#*/
	def getサマルトリア(self):
		return self.getAsInt(54, 2)

	#**
	#* サマルトリア情報を設定。
	#* @param value サマルトリアの王子フラグ
	#*/
	def setサマルトリア(self, value):
		self.set(54, (value & 0x2) > 0)
		self.set(55, (value & 0x1) > 0)

	#**
	#* 命の紋章情報を取得。
	#* @return 命の紋章フラグ
	#*/
	def get命の紋章(self):
		return self.get(59)

	#**
	#* 命の紋章情報を設定。
	#* @param value 命の紋章フラグ
	#*/
	def set命の紋章(self, value):
		self.set(59, value)

	#**
	#* 水の紋章情報を取得。
	#* @return 水の紋章フラグ
	#*/
	def get水の紋章(self):
		return self.get(60)

	#**
	#* 水の紋章情報を設定。
	#* @param value 水の紋章フラグ
	#*/
	def set水の紋章(self, value):
		self.set(60, value)

	#**
	#* 月の紋章情報を取得。
	#* @return 月の紋章フラグ
	#*/
	def get月の紋章(self):
		return self.get(61)

	#**
	#* 月の紋章情報を設定。
	#* @param value 月の紋章フラグ
	#*/
	def set月の紋章(self, value):
		self.set(61, value)

	#**
	#* 星の紋章情報を取得。
	#* @return 星の紋章フラグ
	#*/
	def get星の紋章(self):
		return self.get(62)

	#**
	#* 星の紋章情報を設定。
	#* @param value 星の紋章フラグ
	#*/
	def set星の紋章(self, value):
		self.set(62, value)

	#**
	#* 太陽の紋章情報を取得。
	#* @return 太陽の紋章フラグ
	#*/
	def get太陽の紋章(self):
		return self.get(63)

	#**
	#* 太陽の紋章情報を設定。
	#* @param value 太陽の紋章フラグ
	#*/
	def set太陽の紋章(self, value):
		self.set(63, value)

	#**
	#* プレイヤー３人分の情報を取得。
	#* @return プレイヤー３人分の情報
	#*/
	def getPlayerCollection(self):
		playerCollection = []

		offset = 72
		next = True

		for i in range(3):
			if offset + 20 + 4 > self.size():
				# ビット数が足りない。

				if next == False:
					break
				raise Exception("少なくとももう" + (((offset + 24) - self.size() + 5) / 6) + "文字はあるはずです")

			itemCount = self.getAsInt(offset + 20, 4)

			if offset + 20 + 4 + 7 * itemCount + (1 if i < 2 else 0) > self.size():
				# ビット数が足りない。

				if next == False:
					break
				raise Exception("{}人目 - 少なくとももう{}文字はあるはずです".format(
							i + 1,
							(((offset + 20 + 4 + 7 * itemCount + (1 if i < 2 else 0)) - self.size() + 5) // 6)))

			playerCollection.append(
				Player(
					exist=next,
					経験値=self.getAsInt(offset, 16) + (self.getAsInt(offset + 16, 4) << 16),
					itemCount=itemCount,
					itemBitArray=self.getPart(offset + 24, 7 * itemCount)))

			offset += 20 + 4 + 7 * itemCount

			if i < 2:
				# ２人目まで。
				next &= self.get(offset)
				offset += 1

		return playerCollection

	#**
	#* サマルトリアの王子をいることに、またアイテムの不正を修正する
	#*/
	def setSamarutoriaEnable(self):
		offset = 72

		for i in range(3):
			itemCount = self.getAsInt(offset + 20, 4)

			for j in range(itemCount):
				index = self.getAsInt(offset + 7 * j, 7)

				if index >= 1 and index <= 0x80 and (index % 0x40 >= 1) and (index % 0x40 <= 0x3f):
					# アイテムの値は正しい。

					item = ItemAndEquipment(index)
					if (item.item.itemKind > 0 and
						((i == 0 and item.item.ローレシア王子装備可) or
						 (i == 1 and item.item.サマルトリア王子装備可) or
						 (i == 2 and item.item.ムーンブルク王女装備可))) == False:
						# 装備できないアイテム。

						self.setInt(offset + 7 + i, index & 0x3f, 6, 0)

			offset += 20 + 4 + 7 * itemCount
			if i == 1:
				if self.get(offset) == False:
					# ２人目いない。
					self.set(offset, True)
			elif i == 2:
				if self.get(offset):
					# ３人目いる。
					self.set(offset, False)
			offset += 1

	#**
	#* 余剰ビット有無判定。
	#* @return true=余剰ビットあり／false=なし
	#*/
	def hasExcessBit(self):
		offset = 72
		next = True
		find = False

		for i in range(3):
			if next == False:
				break

			if offset + 20 + 4 > self.size():
				# ビット数が足りない。
				raise Exception(
					"少なくとももう" +
					(((offset + 24) - self.size() + 5) / 6) +
					"文字はあるはずです")

			itemCount = self.getAsInt(offset + 20, 4)

			if offset + 20 + 4 + 7 * itemCount + (1 if i < 2 else 0) > self.size():
				# ビット数が足りない。
				raise Exception(
					"{}人目 - 少なくとももう{}文字はあるはずです".format(
						i + 1,
						(((offset + 20 + 4 + 7 * itemCount +
							(1 if i < 2 else 0)) - self.size() + 5) / 6)))

			offset += 20 + 4 + 7 * itemCount

			if i < 2:
				# ２人目まで。

				next = self.get(offset)

				offset += 1

				if next == False and offset + 20 + 4 < self.size():
					# 次のキャラはいないはずなのにビット数は足りる。

					find = True

		return find

	#**
	#* プレイヤー３人分の情報を設定。
	#* @param value プレイヤー３人分の情報
	#*/
	def setPlayerCollection(self, playerCollection):
		offset = 72

		for i, player in enumerate(playerCollection):
			self.setInt(offset, player.経験値, 15, 0)
			offset += 16

			self.setInt(offset, player.経験値, 19, 16)
			offset += 4

			self.setInt(offset, len(player.itemCollection), 3, 0)
			offset += 4

			for item in player.itemCollection:
				self.setInt(offset, item.getCode(), 6, 0)
				offset += 7

			if i < 2:
				# ２人目まで。
				self.set(offset, i + 1 < len(playerCollection))
				offset += 1

	#**
	#* 内容は正当かをチェック。
	#* @return true=正当
	#* @throws InvalidJumonException
	#*/
	def isValid(self):
		valid = True
		offset = 72
		next = True

		for i in range(3):
			if next == False:
				break

			if offset + 20 + 4 > self.size():
				# ビット数が足りない。
				raise Exception("少なくとももう" + (((offset + 24) - self.size() + 5) / 6) + "文字はあるはずです")

			itemCount = self.getAsInt(offset + 20, 4)

			if offset + 20 + 4 + 7 * itemCount + (1 if i < 2 else 0) > self.size():
				# ビット数が足りない。

				raise Exception(
						"少なくとももう" +
						(((offset + 20 + 4 + 7 * itemCount +
							(1 if i < 2 else 0)) - self.size() + 5) / 6) +
						"文字はあるはずです")

			itemBitArray = self.getPart(offset + 24, 7 * itemCount)

			for j in range(itemCount):
				if valid == False:
					break

				itemIndex = itemBitArray.getAsInt(7 * j, 7)

				print(itemIndex)

				if itemIndex < 0 or itemIndex >= 63:
					# 範囲外。
					valid = False

			offset += 20 + 4 + 7 * itemCount

			if i < 2:
				# ２人目まで。

				next = self.get(offset)

				offset += 1

		return valid
