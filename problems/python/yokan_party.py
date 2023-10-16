def parse_input() -> [int, int, int, list[int]]:
  n, l = map(int, input().split())
  k = int(input())
  li = list(map(int, input().split()))
  li.append(l) # 末尾にlを追加しないと、最後の区間の長さが計算できない
  li.insert(0,0)# 先頭に0を追加することで、checkをしやすくする
  return n, l, k, li

def check(mid: int, k: int, li: list[int]) -> bool:
  i: int = 0
  j: int = 0
  d: int = 0
  # この可能性は、入力値に的にありえないが、可読性のために用意しておく．
  if mid > li[-1]:#一番後ろの要素を指定
    return False
  for i in range(len(li)):
    if (mid <= li[i] - li[j]):
      d = d + 1
      j = i
    if (d == k):
      return True
  return False

def binary_search(l: int, k: int, li: list[int]) -> int:
  max: int = l // (k + 1)
  min: int = 1
  while min < max:
    mid = (min + max + 1) // 2  # N=1 ,L=4, K=1, A_1=2 の時にmid==min=1になってしまうのを防ぐための+1
    if (check(mid, k + 1, li)): 
      min = mid
    else:
      max = mid - 1
  return min

def main():
  n, l, k, li = parse_input()
  result = binary_serch(l, k, li)
  print(result)
  
if __name__=="__main__":
  main()