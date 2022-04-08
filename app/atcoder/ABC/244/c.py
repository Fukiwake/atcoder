def main():
    n = int(input())

    num_list = [i + 1 for i in range(2 * n + 1)]

    while True:
        takahashi = num_list.pop(0)
        print(takahashi)
        aoki = int(input())
        if aoki == 0:
            break

        num_list.remove(aoki)





if __name__ == "__main__":
    main()

# 配列から要素を削除する方法
# リストのメソッドpop()で、指定した位置の要素を削除し、その要素の値を取得できる。
# リストのメソッドremove()で、指定した値と同じ要素を検索し、最初の要素を削除できる。
# del文でリストの要素を削除することもできる。

# 削除したい要素をインデックスで指定する。先頭（最初）は0で、末尾（最後）は-1。
