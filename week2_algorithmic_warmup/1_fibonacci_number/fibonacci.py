# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    else:
        n1 = 0
        n2 = 1
        for ind in range(2, n+1):
            soma = n1 + n2
            if ind % 2 == 0:
                n1 = soma
            else:
                n2 = soma

    return soma

n = int(input())
print(calc_fib(n))
