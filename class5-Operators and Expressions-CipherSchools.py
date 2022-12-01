##  operators and expressions
#sum(1,2) #it is also an expression (fancy way of calling a function)
#1.Arithmetic Operetors
a=5+5
b=10-5
c=10/3 #it treats this as float (in case of float)
#in py3 it is treated float as number type int
#Floor Division
d=10//3 #now it does not belong to float type
isinstance(10.0,int) #integer and float are two diffent things
m=10%3 #gives the remainder
e=2**3 #(exponentiation)to raise to the power
str1='hello' + 'world'
mul='abc'*6
#Comparision operators
q=1==2
w=1 !=2
r=1<2
e=2>3
z="ab" < "z" #it gives true (due to lexigographical way)
s="a" <"A" #it gives false (these are only possible in dunders) (since intrepreter is slow so they implemented dunder)
#  Logical Operators
a=True and False
b=True and False
c=True and 1
d= 1 and 0
e=1 and 5 #in py there is no boolean data tpe in py
isinstance(True,int)
type(True)
#in py 3 we cannot to True,but in py 2 it is possible , but now it is fixed
#so True and False are fixed
#it works on Truky and Falsy (none is false and non zero is true in binary nature )
#Short Circuiting:
type(True)
'''a or true = true
a or false = a
a and true =a
a and false = false'''
#you can solve bool operant with using only one operant
'''true or b=b(if b is truthy)
false or b=a(if a is falsy)
true and b=a(if b is truthy)
false and b=b (if b is falsy)'''
a="hello" and 6
a="" and 6 # output=""
b="" or 1.6 #output=1.6
a=bool("")
a=bool([1,2,3])
a=112 and 0
