# Uses python3
import sys

def fibonacci_sum_naive(n): 
  
    prev = 0
    curr = 1
    
    if n <= 0: 
        return 0
    if n == 1: 
        return 1
      

    mod = n % 60

    if(mod == 0): 
        return 0

    for i in range(2, mod + 3): 
        temp =(prev + curr)% 60
        prev = curr 
        curr = temp 

    total = curr-1
    return(total)


if __name__ == '__main__':
    input1 = str(input())
    from1, to = map(int, input1.split())
    
    print((fibonacci_sum_naive(to)-fibonacci_sum_naive(from1-1))%10)