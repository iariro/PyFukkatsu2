
#**
#* 与えられた単語を組み合わせて２０文字の文字列を生成する。
#*/
# class WordPatternGenerator:
#**
#* 再帰呼び出しを使って単語を組み合わせて１８文字以上の文字列を生成する
#* @param s1 文字列を足していく文字列変数
#* @param list 単語一式 再帰呼び出しされるごとに減っていく
#*/
def generateRecursive(s1, list):
    loop = True

    for i, s2 in enumerate(list):
        if loop == False:
            break

        if len(s1) + len(s2) >= 18:
            # 文字数は足りている。
            pass

        if len(list) > 1:
            # 使用できる文字列はまだある。

            list2 = list[:]
            list2.remove(i)

            if len(s1) < 20:
                # まだ２０文字には達しない。
                generateRecursive(s1 + s2, list2)
