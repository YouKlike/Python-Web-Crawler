'''
利用物件導向的概念找出平均成績以及不及格科目
'''

class Student():
    def __init__(self , name):
        self.name = name
        self.grades = []
        
    def add(self , add):
        self.grades.append(add)
    
    def avg(self):
        sum = 0
        
        for i in range(0 , len(self.grades)):
            sum =  sum + self.grades[i]
            
        avg =  sum / len(self.grades)
            
        return avg
 
    def ficount(self):
        failed = 0
        
        for i in range(0 , len(self.grades)):
            if self.grades[i] < 60:
                failed += 1
                
        return failed


a = Student('蔡秉岑')
a.add(60)
a.add(60)
a.add(20)


print('平均分數' , a.avg())
print('不及格科目數量' , a.ficount())