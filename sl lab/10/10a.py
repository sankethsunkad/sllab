from functools import reduce
li=[1,2,3,4]
print(li)
newli=(i*3 for i in li)
print(newli)
sum1=reduce(lambda x,y:x+y,li)
sum2=reduce(lambda x,y:x+y,newli)
print(sum1)
print(sum2)