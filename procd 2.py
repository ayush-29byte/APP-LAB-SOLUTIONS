#SUM OF NATURAL NUMBERS USING RECURSION
def rsum(n):
    if n <= 1:
        return n
    else:
        return n + rsum(n-1)

num = int(input("Enter a number: "))
recsum=rsum(num)
print("The sum is",recsum)
#code by ayush saxena