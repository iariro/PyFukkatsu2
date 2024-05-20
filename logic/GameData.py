from logic.ExtendedGameDataBitArray import ExtendedGameDataBitArray
from logic.CompressedGameDataBitArray import CompressedGameDataBitArray

#**
#* ゲームデータ。
#*/
class GameData:
	#**
	#* エンカウントゼロ呪文生成用にバリエーション値とゴールドを加工。
	#* @return 加工済みデータ
	#*/
	def trickEncountZero(self):
		variation = (self.バリエーション & 0x1) + 10
		gold = self.ゴールド

		extended = ExtendedGameDataBitArray(gamedata=self)
		compressed = CompressedGameDataBitArray(array=extended)

		compressed.set(0, True)
		compressed.set(1, False)
		compressed.set(2, False)
		compressed.set(3, False)
		compressed.set(4, True)

		compressed.setInt(56, 0, 2, 0)
		compressed.setInt(66, 0, 4, 0)

		goldDirection = False

		inc = gold
		dec = gold - 1

		for count in range(100000):
			compressed.setInt(32, gold, 7, 0)
			compressed.setInt(16, gold, 15, 8)

			compressed.set(48, (variation & 0x1) > 0)

			checksum = compressed.getEncountZeroChecksum()

			if (checksum & 0xfe3f) == 0xac3f:
				# エンカウントゼロ条件に合致した。

				compressed.set( 2, (checksum & 0x400) > 0)
				compressed.set( 3, (checksum & 0x200) > 0)
				compressed.set(56, (checksum & 0x100) > 0)
				compressed.set(57, (checksum & 0x80) > 0)
				compressed.set(58, (checksum & 0x40) > 0)
				compressed.set(66, (checksum & 0x20) > 0)
				compressed.set(67, (checksum & 0x10) > 0)
				compressed.set(68, (checksum & 0x8) > 0)
				compressed.set(69, (checksum & 0x4) > 0)
				compressed.set(70, (checksum & 0x2) > 0)
				compressed.set(71, (checksum & 0x1) > 0)

				return compressed
			else:
				# エンカウントゼロ条件に合致しない。

				variation = 21 - variation

				if variation == 11:
					if goldDirection:
						# 増やす番。

						if gold < 65535:
							# 範囲内。

							gold = inc
							inc += 1
						goldDirection = False
					else:
						# 減らす番。

						if gold > 0:
							# 範囲内。

							gold = dec
							dec -= 1
						else:
							#gold = 65535;
							pass
						goldDirection = True

		return None

	#**
	#* ローレシアの王子の名前を取得。
	#* @return ローレシアの王子の名前
	#*/
	def getローレシアの王子の名前(self):
		return self.ローレシアの王子の名前_

	#**
	#* ローレシアの王子の名前を設定。
	#* @param value ローレシアの王子の名前
	#*/
	def setローレシアの王子の名前(self, value):
		if len(value) > 4:
			# ４文字より長い。
			self.ローレシアの王子の名前_ = value[0:4]
		elif len(value) < 4:
			# ４文字より短い。
			self.ローレシアの王子の名前_ = value
			for i in range(4 - len(value)):
				self.ローレシアの王子の名前_ += '　'
		else:
			# ４文字。
			self.ローレシアの王子の名前_ = value

	#**
	#* データの正当性チェック。
	#* @return エラーメッセージ
	#*/
	def isValid(self):
		valid = None

		for i, player in enumerate(self.playerCollection):
			if player.exist == False:
				# 存在しない
				continue

			equip = [None] * 3

			for item in player.itemCollection:
				if (item.item.itemKind > 0 and
					((i == 0 and item.item.ローレシア王子装備可) or
					 (i == 1 and item.item.サマルトリア王子装備可) or
					 (i == 2 and item.item.ムーンブルク王女装備可))) == False:
					# 装備できないアイテム。

					if item.equipment:
						# 装備している。
						valid = "{}が{}を装備".format(i, item.item.name)

				if item.item.itemKind >= 1 and item.item.itemKind <= 3:
					# 武器・鎧・盾。

					if equip[item.item.itemKind - 1] == None:
						# 未装備状態。
						equip[item.item.itemKind - 1] = item.item
					else:
						# 装備状態。
						valid = "{}が{}に加え{}を装備".format(
							i,
							equip[item.item.itemKind - 1].name,
							item.item.name)
		return valid

	#**
	#* ビット配列からゲームデータを構築。
	#* @param bitArray ビット配列
	#*/
	def __init__(self, bitArray=None):
		if bitArray:
			self.セーブポイント = bitArray.getセーブポイント()
			self.setローレシアの王子の名前(bitArray.getローレシアの王子の名前())
			self.ゴールド = bitArray.getゴールド()
			self.バリエーション = bitArray.getバリエーション()
			self.月のかけら = bitArray.get月のかけら()
			self.水門 = bitArray.get水門()
			self.水のはごろも = bitArray.get水のはごろも()
			self.船 = bitArray.get船()
			self.少女 = bitArray.get少女()
			self.サマルトリア = bitArray.getサマルトリア()
			self.命の紋章 = bitArray.get命の紋章()
			self.水の紋章 = bitArray.get水の紋章()
			self.月の紋章 = bitArray.get月の紋章()
			self.星の紋章 = bitArray.get星の紋章()
			self.太陽の紋章 = bitArray.get太陽の紋章()
			self.playerCollection = bitArray.getPlayerCollection()
		else:
			self.セーブポイント = 0
			self.ローレシアの王子の名前_ = False
			self.ゴールド = 0
			self.バリエーション = 0
			self.月のかけら = False
			self.水門 = False
			self.水のはごろも = False
			self.船 = False
			self.少女 = False
			self.サマルトリア = 0
			self.命の紋章 = False
			self.水の紋章 = False
			self.月の紋章 = False
			self.星の紋章 = False
			self.太陽の紋章 = False
			self.playerCollection = []
