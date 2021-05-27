# def factorial(n):
#     ''' n表示要求的数的阶乘 '''
#     if n==1:
#         return n
#     else:
#         return n*factorial(n-1) # n! = n*(n-1)!
# res = factorial(5)
# print(res)



def factorial(n):
    ''' n表示要求的数的阶乘 '''
    if n==1:
        return n
    n=n*factorial(n-1) # n! = n*(n-1)!
    return n
res = factorial(5)
print(res)