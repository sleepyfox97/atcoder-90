def check(mid: int, k: int, li: list[int]) -> bool:
  i: int = 0
  j: int = 0
  d: int = 0
  for i in range(len(li)):
    if (mid <= li[i]):
      d = d + 1
      j = i
      break
  
  for i in range(len(li)):
    if (mid <= li[i] - li[j]):
      d = d + 1
      j = i
    if (d == k):
      return True
  return False

def main():
  n, l = map(int, input().split())
  k = int(input())
  li = list(map(int, input().split()))
  li.append(l) # 末尾にlを追加しないと、最後の区間の長さが計算できない

  max: int = l // (k + 1) + 1 # N=1 ,L=4, K=1, A_1=2 の時にmid==min=1になってしまうのを防ぐ(31行目に関わってくる．もっと綺麗な書き方ありそう)
  min: int = 1
  mid: int = (min + max) // 2

  while min <= max:
    if (check(mid, k + 1, li)):
      min = mid
    else:
      max = mid
    old_mid = mid
    mid =  (min + max) // 2
    if mid == old_mid:
      break
  print(mid)
  
main()