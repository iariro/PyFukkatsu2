from logic.SavePoint import SavePoint

#class GameDataChecker:
#**
#* セーブポイントチェック処理。
#*/
def SavePointChecker(gameData):
	savepoint = SavePoint(gameData.セーブポイント).name

	if gameData.セーブポイント in (2, 3, 4, 5):
		if len(gameData.playerCollection) >= 3:
			# ３人揃っている。

			if gameData.船 == False:
				# 船を手に入れていない。
				return [ "船を手に入れていないのに{}には行けないはずです。".format(savepoint) ]
		else:
			# ３人揃っていない。
			return [ "３人揃っていないのに{}には行けないはずです。".format(savepoint) ]

		if gameData.セーブポイント == 5:
			# ロンダルキアの場合。

			if gameData.船 == False:
				# 船を手に入れていない。
				return [ "船を手に入れずに{}には行けないはずです。".format(savepoint) ]

			if gameData.月のかけら == False:
				# 月のかけらを使っていない。
				return [ "月のかけらを使わずに{}には行けないはずです。".format(savepoint) ]

	elif gameData.セーブポイント == 6:
		if len(gameData.playerCollection) <= 1:
			# １人しかいない。
			return [ "１人で{}には行けないはずです。".format(savepoint) ]

	return None

#**
#* ゴールドチェック処理。
#*/
def GoldChecker(gameData):
	if gameData.ゴールド < 0 or gameData.ゴールド > 65535:
		# ゴールドが範囲外。

		before = gameData.ゴールド

		if gameData.ゴールド < 0:
			# ゴールドが負の値。
			gameData.ゴールド = 0

		if gameData.ゴールド > 65535:
			# ゴールドが限界を越えている。
			gameData.ゴールド = 65535

		return [ "ゴールド{}が範囲外です。{}に調整しました。".format(before, gameData.ゴールド) ]

	return None

#**
#* バリエーションチェック処理。
#*/
def VariationChecker(gameData):
	if gameData.バリエーション < 0 or gameData.バリエーション > 15:
		# バリエーションが範囲外。

		before = gameData.バリエーション

		if gameData.バリエーション < 0:
			# バリエーションが負の値。
			gameData.バリエーション = 0

		if gameData.バリエーション > 15:
			# バリエーションが限界を越えている。
			gameData.バリエーション = 15

		return [ "バリエーション{}が範囲外です。{}に調整しました。".format(before, gameData.バリエーション) ]

	return None

#**
#* 経験値チェック処理。
#*/
def ExperienceChecker0(gameData):
    ExperienceChecker(gameData, 0)

def ExperienceChecker1(gameData):
    ExperienceChecker(gameData, 1)

def ExperienceChecker2(gameData):
    ExperienceChecker(gameData, 2)

def ExperienceChecker(gameData, index):
	if index < len(gameData.playerCollection):
		# 対象のプレイヤーは存在する。

		player = gameData.playerCollection[index]

		if player.経験値 < 0 or player.経験値 > 1000000:
			# 経験値が範囲外。

			before = player.経験値

			if player.経験値 < 0:
				# 経験値が負の値。
				player.経験値 = 0

			if player.経験値 > 1000000:
				# 経験値が限界を越えている。
				player.経験値 = 1000000

			if index == 0:
				name = "ローレシア"
			elif index == 1:
				name = "サマルトリア"
			elif index == 2:
				name = "ムーンブルク"

			return [ "{}の経験値{}が範囲外です。{}に調整しました。".format(name, before, player.経験値) ]

		return None
	else:
		# 対象のプレイヤーは存在しない。
		return None

#**
#* サマルトリアの王子のフラグチェック。
#*/
def SamarutoriaFlagChecker(gameData):
	if len(gameData.playerCollection) >= 2:
		# サマルトリアの王子は加わっている。

		if gameData.サマルトリア < 3:
			# ローレシアの王の話を聞いていない。
			return [ "サマルトリアの王子と出会う段階を経ていません。" ]

	return None

#**
#* 月のかけらチェック。
#*/
def 月のかけらChecker(gameData):
	if gameData.月のかけら:
		# 月のかけらを使った状態。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れていない。
				return [ "船を手に入れずに月のかけらは手に入れられないはずです。" ]
			if gameData.水門 == False:
				# 水門を開けていない。
				return [ "水門を開けずに月のかけらは手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに月のかけらは手に入れられないはずです。" ]
	return None

#**
#* 水門チェック。
#*/
def 水門Checker(gameData):
	if gameData.水門:
		# 水門を開けている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れずに水門を開けている。
				return [ "船を手に入れずに水門を開ける場所まで行けないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに水門を開ける場所まで行けないはずです。" ]
	return None

#**
#* 水のはごろもチェック。
#*/
def 水のはごろもChecker(gameData):
	if gameData.水のはごろも:
		# 水のはごろもを作成中である。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れていない。
				return [ "船を手に入れずに水のはごろもを作ってもらえる場所まで行けないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに水のはごろもを作ってもらえる場所まで行けないはずです。" ]
	return None

#**
#* 船チェック。
#*/
def 船Checker(gameData):
	if gameData.船:
		# 船を手に入れている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.少女 == False:
				# 少女を助けていない。
				return [ "少女を助けずに船を手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに船を手に入れる場所まで行けないはずです。" ]
	return None

#**
#* 少女チェック。
#*/
def 少女Checker(gameData):
	if gameData.少女:
		# 少女を助けている。
		if len(gameData.playerCollection) < 3:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに少女を助ける場所まで行けないはずです。" ]
	return None

#**
#* 命の紋章チェック。
#*/
def 命の紋章Checker(gameData):
	if gameData.命の紋章:
		# 命の紋章を手に入れている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れずに命の紋章を手に入れている。
				return [ "船を手に入れずに命の紋章を手に入れられないはずです。" ]
			if gameData.月のかけら == False:
				# 月のかけらを使わずに命の紋章を手に入れている。
				return [ "月のかけらを使わずに命の紋章を手に入れる場所まで行けないはずです。" ]
			if gameData.船 == False:
				# 船を手に入れずに命の紋章を手に入れている。
				return [ "船を手に入れずに命の紋章を手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに命の紋章を手に入れられないはずです。" ]
	return None

#**
#* 水の紋章チェック。
#*/
def 水の紋章Checker(gameData):
	if gameData.水の紋章:
		# 水の紋章を手に入れている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れずに水の紋章を手に入れている。
				return [ "船を手に入れずに水の紋章を手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに水の紋章を手に入れられないはずです。" ]
	return None

#**
#* 月の紋章チェック。
#*/
def 月の紋章Checker(gameData):
	if gameData.月の紋章:
		# 月の紋章を手に入れている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れずに月の紋章を手に入れている。
				return [ "船を手に入れずに月の紋章を手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに月の紋章を手に入れられないはずです。" ]
	return None

#**
#* 星の紋章チェック。
#*/
def 星の紋章Checker(gameData):
	if gameData.星の紋章:
		# 星の紋章を手に入れている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れずに星の紋章を手に入れている。
				return [ "船を手に入れずに星の紋章を手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに星の紋章を手に入れられないはずです。" ]
	return None

#**
#* 太陽の紋章チェック。
#*/
def 太陽の紋章Checker(gameData):
	if gameData.太陽の紋章:
		# 太陽の紋章を手に入れている。
		if len(gameData.playerCollection) >= 3:
			# プレイヤーは３人いる。
			if gameData.船 == False:
				# 船を手に入れずに太陽の紋章を手に入れている。
				return [ "船を手に入れずに太陽の紋章を手に入れられないはずです。" ]
		else:
			# プレイヤーは３人いない。
			return [ "３人揃っていないのに太陽の紋章を手に入れられないはずです。" ]
	return None

#**
#* 没アイテムチェック。
#*/
def 没アイテムChecker(gameData):
	for player in gameData.playerCollection:
		for item in player.itemCollection:
			if item.item.name == "みみせん" or item.item.name == "しのオルゴール":
				# 没アイテムである。
				return [ "没アイテムが指定されています。" ]
	return None

#**
#* アイテム入手チェック。
#*/
def アイテム入手Checker(gameData):
	getLevel = 0

	if len(gameData.playerCollection) >= 2:
		# ２人いる。
		getLevel = 1
		if len(gameData.playerCollection) >= 3:
			# ３人揃っている。
			getLevel = 2
			if gameData.船:
				# 船を手に入れている。
				getLevel = 3
				if gameData.月のかけら:
					# 月のかけらを使っている。
					getLevel = 4

	errors = []

	for player in gameData.playerCollection:
		for item in player.itemCollection:
			if item.item.getLevel > getLevel:
				# 入手できないはずのアイテムである。
				condition = None
				if item.item.getLevel == 1:
					condition = "２人"
				elif item.item.getLevel == 2:
					condition = "３人揃って"
				elif item.item.getLevel == 3:
					condition = "船を手に入れて"
				elif item.item.getLevel == 4:
					condition = "月のかけらを使って"

				errors.append("{}は{}いない状態では入手できないはずです。".format(item.item.name, condition))

			if item.item.name == 'ルビスのまもり':
				# ルビスのまもりである。
				if (gameData.命の紋章 and
					gameData.水の紋章 and
					gameData.月の紋章 and
					gameData.星の紋章 and
					gameData.太陽の紋章) == False:
					# 紋章が揃っていない。

					errors.append("紋章を揃えずにルビスのまもりを手に入れられないはずです。")

	return errors

#**
#* ゲームデータチェックオブジェクト。
#*/
checkers = [
	SavePointChecker,
	GoldChecker,
	VariationChecker,
	ExperienceChecker0,
	ExperienceChecker1,
	ExperienceChecker2,
	SamarutoriaFlagChecker,
	月のかけらChecker,
	水門Checker,
	水のはごろもChecker,
	船Checker,
	少女Checker,
	命の紋章Checker,
	水の紋章Checker,
	月の紋章Checker,
	星の紋章Checker,
	太陽の紋章Checker,
	アイテム入手Checker,
	没アイテムChecker
]

def checkAll(gameData):
    for checker in checkers:
        result = checker(gameData)
        if result:
            yield checker.__name__, checker(gameData)
