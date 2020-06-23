from array import *
num=[]
n=int(input("enter the length of the array"))

for i in range(n):
    x=int(input("enter the value"))
    if x<0:
        x=x*-1
        num.append(x)
    else:   
        num.append(x)
print(num)
def specialLarge(x,y):
    xf=int(str(x)+str(y))
    yf=int(str(y)+str(x))
    if xf> yf:
        return True
    else:
        return False
def getLargeNumber(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if not specialLarge(num[i],num[j]):
                num[i],num[j]=num[j],num[i]
    y=[str(a)for a in num]
    str_y=''.join(y)
    return int(str_y)
print(getLargeNumber(num))