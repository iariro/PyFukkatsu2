from logic.Item import Item

#**
#* アイテム一覧情報を構築する。
#*/
item_list = [
	Item("ひのきのぼう", 1, True, True, True, True, 0),
	Item("せいなるナイフ", 1, True, True, True, True, 0),
	Item("まどうしのつえ", 1, True, True, True, True, 2),
	Item("いかずちのつえ", 1, True, True, True, True, 3),
	Item("こんぼう", 1, True, True, True, False, 0),
	Item("どうのつるぎ", 1, True, True, True, False, 0),
	Item("くさりがま", 1, True, True, True, False, 0),
	Item("てつのやり", 1, True, True, True, False, 1),
	Item("はやぶさのけん", 1, True, True, True, False, 3),
	Item("はがねのつるぎ", 1, True, True, False, False, 1),
	Item("おおかなづち", 1, True, True, False, False, 3),
	Item("はかいのつるぎ", 1, True, True, False, False, 4),
	Item("ドラゴンキラー", 1, True, True, False, False, 3),
	Item("ひかりのつるぎ", 1, True, True, False, False, 3),
	Item("ロトのつるぎ", 1, True, True, False, False, 3),
	Item("いなずまのけん", 1, True, True, False, False, 4),
	Item("ぬののふく", 2, True, True, True, True, 0),
	Item("みかわしのふく", 2, True, True, True, True, 2),
	Item("みずのはごろも", 2, True, True, True, True, 3),
	Item("ミンクのコート", 2, True, True, True, True, 3),
	Item("かわのよろい", 2, True, True, True, False, 0),
	Item("くさりかたびら", 2, True, True, True, False, 0),
	Item("あくまのよろい", 2, True, True, True, False, 4),
	Item("まほうのよろい", 2, True, True, True, False, 3),
	Item("はがねのよろい", 2, True, True, False, False, 1),
	Item("ガイアのよろい", 2, True, True, False, False, 3),
	Item("ロトのよろい", 2, True, True, False, False, 4),
	Item("かわのたて", 3, True, True, True, False, 0),
	Item("ちからのたて", 3, True, True, True, False, 3),
	Item("はがねのたて", 3, True, True, False, False, 1),
	Item("しにがみのたて", 3, True, True, False, False, 4),
	Item("ロトのたて", 3, True, True, False, False, 3),
	Item("ふしぎなぼうし", 4, True, True, True, True, 3),
	Item("てつかぶと", 4, True, True, False, False, 2),
	Item("ロトのかぶと", 4, True, True, False, False, 3),
	Item("ロトのしるし", 0, True, False, False, False, 3),
	Item("ふねのざいほう", 0, True, False, False, False, 3),
	Item("つきのかけら", 0, True, False, False, False, 3),
	Item("ルビスのまもり", 0, True, False, False, False, 4),
	Item("じゃしんのぞう", 0, True, False, False, False, 4),
	Item("せかいじゅのは", 0, True, False, False, False, 3),
	Item("やまびこのふえ", 0, True, False, False, False, 3),
	Item("ラーのかがみ", 0, True, False, False, False, 1),
	Item("あまつゆのいと", 0, True, False, False, False, 2),
	Item("せいなるおりき", 0, True, False, False, False, 3),
	Item("かぜのマント", 5, True, True, True, True, 1),
	Item("あくまのしっぽ", 5, True, True, True, True, 3),
	Item("まよけのすず", 5, True, True, True, True, 2),
	Item("ふっかつのたま", 0, True, False, False, False, 3),
	Item("ゴールドカード", 0, True, False, False, False, 0),
	Item("ふくびきけん", 0, True, False, False, False, 0),
	Item("せいすい", 0, True, False, False, False, 0),
	Item("キメラのつばさ", 0, True, False, False, False, 0),
	Item("みみせん", 0, False, False, False, False, 0),
	Item("きんのかぎ", 0, True, False, False, False, 3),
	Item("ぎんのかぎ", 0, True, False, False, False, 0),
	Item("ろうやのかぎ", 0, True, False, False, False, 3),
	Item("すいもんのかぎ", 0, True, False, False, False, 3),
	Item("どくけしそう", 0, True, False, False, False, 0),
	Item("やくそう", 0, True, False, False, False, 0),
	Item("いのりのゆびわ", 0, True, False, False, False, 0),
	Item("しのオルゴール", 0, False, False, False, False, 0),
	Item("あぶないみずぎ", 0, False, False, False, False, 0)
]

#**
#* アイテム一覧。
#* アイテムの番号が１－６４であることに注意。
#*/

#**
#* 一覧中のアイテムの個数。
#* @return アイテムの個数
#*/
def getCount():
	return len(item_list)

#**
#* アイテム情報からアイテムの番号を取得。
#* @param item アイテム情報
#* @return アイテムの番号
#*/
def indexOf(item):
	for i in range(len(item_list)):
		if item_list[i].name == item.name:
			return i + 1
	else:
		return None

#**
#* アイテムの番号からアイテム情報を取得。
#*/
def get(i):
	return item_list[i - 1]

#**
#* アイテム名からアイテムの番号を取得。
#* @param name アイテム名
#* @return アイテムの番号
#*/
def getCodeFromName(name):
	for i in range(len(item_list)):
		if item_list[i].name == name:
			# 名前は一致する。
			return i + 1
	return -1
