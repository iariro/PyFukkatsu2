from logic.IllegalCharacterException import IllegalCharacterException
from logic.NumberString import NumberString
from logic.SamarutoriaMuunburukuName import SamarutoriaMuunburukuName

#**
#* 呪文に使用する文字。
#*/
characterSet = [
	'あ', 'い', 'う', 'え', 'お',
	'か', 'き', 'く', 'け', 'こ',
	'さ', 'し', 'す', 'せ', 'そ',
	'た', 'ち', 'つ', 'て', 'と',
	'な', 'に', 'ぬ', 'ね', 'の',
	'は', 'ひ', 'ふ', 'へ', 'ほ',
	'ま', 'み', 'む', 'め', 'も',
	'や', 'ゆ', 'よ', 'ら', 'り',
	'る', 'れ', 'ろ', 'わ', 'が',
	'ぎ', 'ぐ', 'げ', 'ご', 'ざ',
	'じ', 'ず', 'ぜ', 'ぞ', 'ば',
	'び', 'ぶ', 'べ', 'ぼ', 'ぱ',
	'ぴ', 'ぷ', 'ぺ', 'ぽ'
]

serifu11 = "＊「おうじ　%sよ。\r\n" \
	"　　よくぞ　ぶじで　もどってきた。\r\n" \
	"\r\n"

serifu12 = "＊「これは　%s　おうじ！\r\n" \
	"　　よくぞ　まいられた。\r\n" \
	"\r\n"

serifu13 = "＊「おお！%sよ。\r\n" \
	"　　なんと　ここでも　ふっかつの\r\n" \
	"　　じゅもんが　きけるのじゃ。\r\n" \
	"＊「べんりな　よのなかに　なったもの\r\n" \
	"　　よのう。\r\n" \
	"\r\n"

serifu21 = "＊「%sが　つぎのレべルになる\r\n" \
	"　　には　あと%sポイントの\r\n" \
	"　　けいけんが　ひつようじゃ。\r\n" \
	"\r\n"

serifu31 = "＊「そなたに　ふっかつのじゅもんを\r\n" \
	"　　おしえよう！\r\n" \
	"\r\n" \
	"%s\r\n\r\n"

serifu41 = "＊「そなたが　ハーゴンをたおしてくる\r\n" \
	"　　ひを　たのしみに　まっておるぞ！\r\n" \
	"　　では　またあおう　わがむすこよ。"

serifu42 = "＊「わがむすこ　%s　を\r\n" \
	"　　よろしく　たのむぞよ。"

serifu43 = "＊「では　また　あおう！\r\n" \
	"　　ロトのしそんたちよ！"

serifu5 = "どこからともなく　うつくしい\r\n" \
	"こえが　きこえる……。\r\n" \
	"\r\n" \
	"＊「あなたがたに\r\n" \
	"　　ふっかつの　じゅもんを\r\n" \
	"　　おしえましょう。\r\n"

serifu6 = "＊「いまのを　かきとって\r\n" \
	"　　くれましたか？\r\n" \
	"\r\n"

serifu7 = "＊「わたしは　いつも　あなたがたを\r\n" \
	"　　みまもっています。わたしと\r\n" \
	"　　いとしきひとの　しそんたちよ。"

whitespace = " 　\r\n"

#**
#* 呪文。
#*/
class Jumon:
	#**
	#* 呪文文字列を受けてコード配列を取得。
	#* @param jumon 呪文文字列
	#*/
	def __init__(self, jumon=None, codeArray=None):
		if jumon:
			count = 0
			length = 0

			for ch in jumon:
				if whitespace.find(ch) < 0:
					# 空白文字ではない。
					length += 1

			self.codeArray = [0] * length

			for ch in jumon:
				if whitespace.find(ch) < 0:
					# 空白文字ではない。
					index = -1
					for j in range(len(characterSet)):
						if characterSet[j] == ch:
							# 一致した。
							index = j
							break

					if index >= 0:
						# 使用可能な文字。
						self.codeArray[count] = index

					count += 1

					if index < 0:
						# 使用できない文字を検出。
						raise IllegalCharacterException("呪文", count, ch)
		elif codeArray:
			self.codeArray = codeArray

	#**
	#* コード配列を集約する。
	#* @param codeArray コード配列
	#*/

	#**
	#* 文字数を取得。
	#* @return 文字数
	#*/
	def getCodeCount(self):
		return self.codeArray.length

	#**
	#* 文字コードを取得。
	#* @param index インデックス
	#* @return 文字コード
	#*/
	def get(self, index):
		return self.codeArray[index]

	#**
	#* 呪文文字列を生成。
	#* @return 呪文文字列
	#*/
	def getJumonStringNoReturn(self):
		return ''.join([characterSet[c] for c in self.codeArray])

	#**
	#* 呪文文字列を生成。
	#* @return 呪文文字列
	#*/
	def getJumonStringOnly(self):
		builder = ''

		for i, code in enumerate(self.codeArray):
			builder += characterSet[code]

			if i % 10 == 2 or i % 10 == 5:
				# 各行の３文字目，５文字目。
				builder += " "
			elif i % 10 == 9:
				# 各行の行末。
				if i < 49:
					# ４行目まで。
					builder += "\r\n"
				else:
					# ５行目。
					builder += " "

		return builder

	#**
	#* 呪文文字列を生成。
	#* @param gameData ゲームデータ
	#* @param type 0/1/2
	#* @return 呪文文字列
	#*/
	def getJumonAndSerifuString(self, gameData, type):
		builder = ''

		ローレシアの王子の経験値 = 0
		サマルトリアの王子の経験値 = 0
		ムーンブルクの王女の経験値 = 0

		if len(gameData.playerCollection) >= 1:
			ローレシアの王子の経験値 = gameData.playerCollection.get(0).経験値

		if len(gameData.playerCollection) >= 2:
			サマルトリアの王子の経験値 = gameData.playerCollection.get(1).経験値

		if len(gameData.playerCollection) >= 3:
			ムーンブルクの王女の経験値 = gameData.playerCollection.get(2).経験値

		ローレシアの王子 = len(gameData.playerCollection) >= 1
		サマルトリアの王子 = len(gameData.playerCollection) >= 2
		ムーンブルクの王女 = len(gameData.playerCollection) >= 3

		for i, code in enumerate(self.codeArray):
			if i % 10 == 0:
				# 各行１文字目。
				if i == 0:
					# １行目。
					builder += "　　"
				elif i >= 10 and i <=40:
					# ２行目から４行目。
					builder += "\r\n　　"
				else:
					# ５行目。
					builder += " "

			builder += characterSet[code]

			if i + 1 < len(self.codeArray):
				# まだ続く。
				if i % 10 == 2 or i % 10 == 5:
					# 各行３文字目６文字目。
					builder += " "

		name = gameData.getローレシアの王子の名前()

		ret = None
		if type == 0:
			ret = serifu11.format(name)
		elif type == 1:
			ret = serifu12.format(name)
		elif type == 2:
			ret = serifu13.format(name)

		if ローレシアの王子:
			# ローレシアの王子は仲間。
			ret += serifu21.format(
				name,
				NumberString(ローレシアの王子の経験値().getPointForNextLevel(ローレシアの王子の経験値)))

		name2 = SamarutoriaMuunburukuName(name)

		if サマルトリアの王子:
			# サマルトリアの王子は仲間。
			ret += serifu21.format(
				name2.サマルトリアの王子の名前,
				NumberString(サマルトリアの王子の経験値().getPointForNextLevel(サマルトリアの王子の経験値)))

		if ムーンブルクの王女:
			# ムーンブルクの王女は仲間。
			ret += serifu21.format(
				name2.ムーンブルクの王女の名前,
				NumberString(ムーンブルクの王女の経験値().getPointForNextLevel(ムーンブルクの王女の経験値)))

		ret += serifu31.format(builder.toString())

		if type == 0:
			ret += serifu41
		elif type == 1:
			ret += serifu42.format(name2.サマルトリアの王子の名前)
		elif type == 2:
			ret += serifu43

		return ret

	#**
	#* ふっかつのたま仕様の呪文文字列を生成。
	#* @return 呪文文字列
	#*/
	def getJumonStringByTama(self):
		builder = serifu5
		builder += "\r\n"

		for i, code in enumerate(self.codeArray):
			if i % 10 == 0:
				# 各行１文字目。
				if i == 0:
					# １行目。
					builder += "　　"
				elif i >= 10 and i <=40:
					# ２行目から４行目。
					builder += "\r\n　　"
				else:
					# ５行目。
					builder += " "

			builder += characterSet[code]

			if i + 1 < len(self.codeArray):
				# まだ続く。
				if i % 10 == 2 or i % 10 == 5:
					# 各行３文字目６文字目。
					builder += " "

		builder += "\r\n"
		builder += "\r\n"

		builder += serifu6
		builder += serifu7

		return builder

	#**
	#* シフトを解除したバイト列を取得。
	#* @return シフトを解除したバイト列
	#*/
	def getPlainArray(self):
		shift = (((self.codeArray[0] & 0x06) >> 1) + 1)

		ret = [0] * len(self.codeArray)

		for i in range(len(ret)):
			ret[i] = self.codeArray[i]

			if i >= 1:
				# ２文字目以降。
				ret[i] = ((ret[i] + 0x40 - (self.codeArray[i - 1] + shift)) % 0x40)

		return ret
