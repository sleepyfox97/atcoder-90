"""
貪欲法(Greedy Algorithm)とは、その時点で最適と思われるものを選択していく方法です．
- 保持する状態は常に1つ
- 一度選択した要素を再考しない
という特徴があります．
atcoderの典型問題として[https://atcoder.jp/contests/abc076/tasks/abc076_b](https://atcoder.jp/contests/abc076/tasks/abc076_b)があるので、それを解いてみます．
"""
n = int(input())
k = int(input())

r: int = 1
i: int = 0
while i < n:
  if r * 2 < r + k:
    r = r * 2
  else:
    r = r + k
  i = i + 1
print(r)