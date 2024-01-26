#20demo.py by Abhi Sharma

print('hello again') #greeting

"""
This
is a 
multi line
comment
"""
import math

print(1 + 1)
print(1 - 1)
print(2 * 2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1)) 
print(math.ceil(2.4))
print(math.log(400))
print(0.1 * 3)

a = 3 #side
b = 4 #side
c = math.sqrt(a**2 + b**2) #hypotenuse
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ')

def greeting():
	print=('hello yourself')


def pythagoras(a,b):
	c = math.sqrt(a**2 + b**2)
	return c
	
x = pythagoras(3,4)
print(x)


#Practice

def signswitcher(a):
	print(a * -1)
	
print(signswitcher(3))

def circleareacalculator(a):
	# circle area
	print((a ** 2)*3.14)
	
s = "hello world"
print(s, type(s))

a = 2
b = 3
if a == b:
	print("a equals b")
print(a,b)


c = a == b
print(c)
print(type(c))

if a < b:
	print("a < b")
elif a > b:
	print("a > b")
else:
	print("a == b")

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

if math.isclose(a, b): print('close enough')



















