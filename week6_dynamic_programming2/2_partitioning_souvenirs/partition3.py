# Uses python3
import sys

def subsetSum(S, n, a, b, c):

	# return true if subset is found
	if a == 0 and b == 0 and c == 0:
		return True

	# base case: no items left
	if n < 0:
		return False

	# Case 1. current item becomes part of first subset
	A = False
	if a - S[n] >= 0:
		A = subsetSum(S, n - 1, a - S[n], b, c)

	# Case 2. current item becomes part of second subset
	B = False
	if not A and (b - S[n] >= 0):
		B = subsetSum(S, n - 1, a, b - S[n], c)

	# Case 3. current item becomes part of third subset
	C = False
	if (not A and not B) and (c - S[n] >= 0):
		C = subsetSum(S, n - 1, a, b, c - S[n])

	# return true if we get solution
	return A or B or C


# Function for solving 3-partition problem. It return true if given
# set S[0..n-1] can be divided into three subsets with equal sum
def partition3(S):

	if len(S) < 3:
		return False

	# return true if sum is divisible by 3 and the set can can
	# be divided into three subsets with equal sum
	return (sum(S) % 3) == 0 and \
		   subsetSum(S, len(S) - 1, sum(S) / 3, sum(S) / 3, sum(S) / 3)

if __name__ == '__main__':
    n = int(input())
    A = [*map(int, input().split())]
    print(1 if partition3(A) else 0)

