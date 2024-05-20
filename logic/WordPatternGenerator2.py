
#**
#* 指定の文字列パターンの組み合わせを作成する。
#* @author kumagai
#*/
class WordPatternGenerator2:
	#**
	#* 指定の文字列パターンの組み合わせを作成する。
	#* @param words 文字列パターン
	#*/
	def __init__(self, words):
		self.phrase_list = []
		self.generateRecursive(words, 0, "")

	#**
	#* 指定の文字列パターンの組み合わせを再帰的に作成する。
	#* @param words 文字列パターン
	#* @param depth 深さ
	#* @param phrase フレーズ
	#*/
	def generateRecursive(self, words, depth, phrase):
		if depth < len(words):
			# 範囲内。
			for word in words[depth].split("|"):
				self.generateRecursive(words, depth + 1, phrase + word)
		else:
			# 終端に達した。
			self.phrase_list.append(phrase)
