from logic.Jumon import Jumon, characterSet
from logic.GameData import GameData
from logic.CompressedGameDataBitArray import CompressedGameDataBitArray
from logic.ExtendedGameDataBitArray import ExtendedGameDataBitArray

#**
#* 復活の呪文生成処理
#*/
#public class JumonGenerator
#**
#* 指定の文字列に余計な文字を追加して復活の呪文生成を試みる。
#* @param phrases 元となるフレーズ
#* @param enableSamarutoria true=サマルトリアの王子を有効にする
#*/
def generateWithExtraCharacter(phrases, enableSamarutoria):
	countError = 0
	loop = True
	jumonList = []

	for phrase0 in phrases.phrase_list:
		for ch in characterSet:
			if loop == False:
				break

			phrase = phrase0

			while True:
				phrase += ch

				try:
					jumon = Jumon(jumon=phrase)
					compressed = CompressedGameDataBitArray(byteArray=jumon.getPlainArray())
					extended = ExtendedGameDataBitArray(bitArray=compressed)

					if enableSamarutoria:
						extended.setSamarutoriaEnable()
						compressed = CompressedGameDataBitArray(array=extended)

					namecheck = extended.isValidローレシアの王子の名前()

					if namecheck == None:
						# ローレシアの王子の名前は正しい。
						gameData = GameData(bitArray=extended)
						datacheck = gameData.isValid()

						if datacheck == None:
							# データ内容は正しい。
							if compressed.getチェックサム１() == compressed.getチェックサム２():
								# チェックサムは正当。
								if compressed.isValidTerminate():
									# 端数OK。
									if enableSamarutoria:
										jumon = Jumon(codeArray=compressed.getJumonCode())
									jumonList.append(jumon)
				finally:
					pass

				if countError >= 20:
					# エラーは２０件を超えた。
					loop = False

				if (len(phrase) < 52 and loop) == False:
					break

	return jumonList
