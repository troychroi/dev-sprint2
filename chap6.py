# Enter your answrs for chapter 6 here
# Name: Troy Church

# Ex. 6.1

import math

def compare(x, y):
	if x > y:
		return 1
	if x == y:
		return 0
	if x < y:
		return -1
print(compare(1,2))

# Reading run-through 6.2

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result
print(distance(1, 2, 4, 6))

# Ex. 6.2

def hypotenuse(leg1, leg2):
	leg3 = leg1**2 + leg2**2
	return math.sqrt(leg3)
print 'The hypotenuse of this right triangle is', (hypotenuse(5, 5))


# Ex. 6.3

def is_divisible(x, y, z):
	return x <= y <= z

print(is_divisible(3, 2, 3))

# Reading run-through 6.5

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result 
print(factorial(3))

# Reading run-through 6.8

def factorial2(n):
	if not isinstance(n, int):
		print 'Factorial is only defined for integers.'
		return None
	elif n < 0:
		print 'Factorial is not defined for negative integers.'
		return None
	elif n == 0:
		return 1
	else:
		return n * factorial2(n-1)

print(factorial2(4))


# Ex. 6.6

def first(word):
	return word[0]

def middle(word):
	return word [1:-1]

def last(word):
	return word[-1]

print(first('kayak'))
print(middle('kayak'))
print(last('kayak'))

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))

print(is_palindrome('kayak'))
print(is_palindrome('bob'))
print(is_palindrome('o'))
print(is_palindrome('tree'))


# Ex 6.8

def gcd(a, b):
	if a > b:
		r = a % b
		if r == 0:
			return b
		else:
			return gcd(b, r)
	if a < b:
		r = b % a
		if r == 0:
			return a
		else:
			return gcd(a, r)

print gcd(9, 12)
