# Enter your answrs for chapter 7 here
# Name:

# Ex. 7.2

def square_root(a):
	x = 2 
	y = (x + a/x) / 2
	epsilon = 0.00000000001
	if abs(y - x) < epsilon:
		print y
	while abs(y - x) > epsilon: 
		x = y
		y = (x + a/x) / 2
		break
	else:
		return
	print y		
square_root(33)



# up to this number (33), it estimates the correct square root.

# Ex. 7.5

import math

def pi_approx():
	factor = (2 * math.sqrt(2))/9801 
	k = 0
	total = 0
	1e-15
	
	while True:
		k_run = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k)**4 * 396**(4 * k))
		term = k_run * factor 
		total += term
		if abs(term) < 1e-15: break
		k += 1
	return 1 / total  

print(pi_approx())

# How many iterations does it take to converge?