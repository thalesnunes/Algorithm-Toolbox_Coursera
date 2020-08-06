# Uses python3
import sys

def get_change(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]
    

if __name__ == '__main__':
    m = int(input())
    coinCount = [0]*(m+1)
    coinUsed = [0]*(m+1)
    print(get_change([1, 3, 4], m, coinCount, coinUsed))
