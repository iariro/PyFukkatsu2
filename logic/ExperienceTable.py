
#**
#* 経験値テーブルの基底クラス。
#*/
class ExperienceTable:
	#**
	#* 経験値テーブル情報を構築する。
	#* @param table 経験値テーブル情報
	#*/
	def __init__(self, table):
		self.table = table

	#**
	#* 経験値からレベルを取得。
	#*
	#* @param experience 経験値
	#*
	#* @return レベル
	#*/
	def getLevel(self, experience):
		for i in range(len(self.table)):
			if experience < self.table[i]:
				# テーブルの値が指定の経験値よりも大きい。
				return i
		else:
			return i + 1

	#**
	#* 次のレベルまでの経験値を取得。
	#*
	#* @param experience 経験値
	#*
	#* @return 次のレベルまでの経験値
	#*/
	def getPointForNextLevel(self, experience):
		level = self.getLevel(experience)
		return self.table[level] - experience if level < len(self.table) else 0
