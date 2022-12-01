#LOOPS
a=1
while a<10 :
    print(a)
    #to increase a value by 1 use:
    a+=1
name="hello"
print(name.__iter__)
for c in name:
    print(c)
    print(type(c)) #everything is a string
for i in 1:
    print(i)  #gives error
for i in range(5):
    print(i)
for i in range(5):
    print(i)
    i = 100 #what ever you do or create a new value to i , py corrects and gives the correct that is previous
    print(i)
for i in [0,1,2,3,4]: #i=
    print(i) #i=2
    i=10000 #i=10000
    print(i) #i=10000
if True:
    pass #it is empty statement
else:
    print("hello")
#in py for loop can have else statement
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Something")