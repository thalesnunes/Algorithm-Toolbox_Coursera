# Uses python3
import sys


def fibonacci_sum_naive(n): 
  
    # The first two Fibonacci numbers 
    prev = 0
    curr = 1
  
    # Base case 
    if n <= 1: 
        return n
      

    mod = n % 60

    # Checking the remainder 
    if(mod == 0): 
        return 0

    # The loop will range from 2 to  
    # two terms after the remainder 
    for i in range(2, mod + 3): 
        temp =(prev + curr)% 60
        prev = curr 
        curr = temp 

    total = curr-1
    return(total)

if __name__ == '__main__':
    input1 = str(input())
    n = int(input1)
    print(fibonacci_sum_naive(n)%10)
