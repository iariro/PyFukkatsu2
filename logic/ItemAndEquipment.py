from logic import ItemCollection

#**
#* アイテム情報と装備しているかの情報。
#*/
class ItemAndEquipment:
	#public final Item item;
	#public boolean equipment;

	#**
	#* 呪文コードに格納されているコードから情報を構築。
	#* @param name アイテム名
	#* @param code 呪文コードに格納されているコード
	#* @param equipment 装備フラグ
	#*/
	def __init__(self, name=None, code=None, equipment=None):
		if name:
			code = ItemCollection.getCodeFromName(name)
		self.item = ItemCollection.get(code % 0x40)
		if equipment:
			self.equipment = equipment
		else:
			self.equipment = (code & 0x40) == 0x40

	#**
	#* 呪文コード格納用のコードを取得。
	#* @return 呪文コード格納用のコード
	#*/
	def getCode(self):
		return ItemCollection.indexOf(self.item) + (0x40 if self.equipment else 0x00)
