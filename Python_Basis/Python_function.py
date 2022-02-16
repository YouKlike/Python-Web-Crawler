'''
利用函數的概念計算圓周長與圓面積
'''

def circle(r):
    a1 = 2 * 3.14 * r
    a2 = 3.14 *r *r
    return(a1,a2)
    
r = float(input('輸入半徑='))
b1 , b2 = circle(r)
print('圓周長=' , b1 , '園面積=' ,b2)