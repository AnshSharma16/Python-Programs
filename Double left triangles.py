n=int(input('Enter number of rows: '))
for i in range(n):
     print(' '*(n-1-i)+"*"*(i+1)+' '*(n-i)+'*'*(i+1))