def main():
  n = int(input())
  if n % 2 == 1: # n is oddの場合を除く
    return
  else:
    # bit全探索
    bit = 0;
    for bit in range(2 ** n):
      result = ""
      # bitの数がnの半分でない場合には、以降の処理をスキップする
      count = 0
      test = bit
      while test:
        count += test & 1
        test >>= 1
      if count != n // 2:
        continue

      # bitの数値に応じて、"("と")"を出力する
      for j in range(n):
        if (bit & (1 << j)) == 0:
          result = "(" + result
        else:
          result = ")" + result
      if check(result):
        print(result)

def check(s: str) -> bool:
  stack = []
  for c in s:
    if c == "(":
      stack.append(c)
    else:
      if len(stack) == 0:
        return False
      stack.pop()
  return len(stack) == 0

if __name__=="__main__":
  main()