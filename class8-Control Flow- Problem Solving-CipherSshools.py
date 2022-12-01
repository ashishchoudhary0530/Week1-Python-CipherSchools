n=5
for i in range(n):
    for j in range(n):
        print(i,end="")# it print in single row but end with space
        #empty print call call empty new line
        print()
        for in range(n):
n=10
for i in range(n):
    for j range(n):
        print(n-j, end=" ")
        print()
a=max(1,2,3,4,5)
n=6
for i in range(n):
    for j range(n):
        print(max(n-j, end=" "))
        print()
n=0
for i in range(n):
    for j range(n):
        print(max(n-i, end=" "))
        print()
# all takes constant amount of time
n=0
for i in range(n):
    for j range(n):
        print((i,j, end=" "))
        print()
# all takes constant amount of time
n=2
for i in range(n):
    for j range(n):
        print((n-i-j-1, end=" "))
        print()
# all takes constant amount of time
n=3
for i in range(n):
    for j range(n):
        print((i+1,j+1,max(n-j,n-1) end=" "))
        print()
# all takes constant amount of time
#max can accept n number of arguments
