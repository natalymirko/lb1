import math

a=float(input('Введіть початок діапазону '))
b=float(input('Введіть кінець діапазону '))
h=float(input('Введіть крок розрахунку '))
n=0
t=a
x=[]
while (x<=b):
    if x<0:
       y.append(math.cos(x)*math.cos(x))
    else:
        y.append(math.sqrt(x*x+1))
    n+=1 #kiлькість елементів масиву
    x+=h
# печать
x=a
for i in range(0,n):
    print(x,' ',y[i])
    x+=h
#min
imin=0
for i in range(0,n):
    if y[i]<y[imin]:
        imin=i
print('Мінімальний елемент=',y[imin],'його номер=',imin+1)
#max
imax=0
for i in range(0,n):
    if y[i]>y[imax]:
        imax=i
print('Максимальний елемент=',y[imax],'його номер=',imax+1)
# перевірка порядку знаходження мінімального та максимального
if imax<imin:
    k=imax
    imax=imin
    imin=k
summa=0
for i in range(imin+1,imax):
    summa+=y[i]
print('Сумма елем., розташованих між мінімальним та максимальним елем.=',summa)




