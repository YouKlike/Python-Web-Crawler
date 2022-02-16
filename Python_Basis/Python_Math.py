'''
二元一次方程式求根
'''

def figura(a,b,c):
    num = int((b**2) - (4*a*c))
    return num

outputString = ['Two different roots' , 'Two same roots' , 'No real root']
string = input().split()

a = int(string[0])
b = int(string[1])
c = int(string[2])

num = figura(a,b,c)

if (num > 0):
    num_sqrt = num ** 0.5
    ans = [int(((-1)*b + num_sqrt) / (2*a)) , int(((-1)*b - num_sqrt) / (2*a))]
    print(outputString[0] + " x1=%s , x2=%s" % (ans[0] , ans[1]))

if (num == 0):
    ans = int((-1)*b/(2*a))
    print(outputString[1] + " x=%s" % ans)

if (num < 0):
    print(outputString[2])