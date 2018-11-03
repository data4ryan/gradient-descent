from math import isnan,nan

L = 12.0  #L-smooth value for function f(x) = x^4

def fg(x=None):
	try:
		fval = x ** 4   #calculate function value
	except OverflowError: 
		fval = nan

	try:	
		gval = 4.0*x ** 3 #calculate gradient value
	except OverflowError:
		gval = nan

	return (fval,gval)

def termtest(fg, x, fval, gval, i):
	maxiters = 10 ** 4
	if i>maxiters:
		return True
	else:
		return False

def gradient_descent(fg=None, x0=0, eta=None, termtest=None):
	i = 1  #iteration number
	x = x0
	fval,gval = fg(x)
	while not termtest(fg,x,fval,gval,i):
		x = x - eta(L)*gval
		fval,gval = fg(x)
		i += 1
	return x

if __name__ == "__main__":
	x0=1  #initial value
	print("Gradient Descent with eta1 = 1/L (or {eta1}), where L = {myl}:".format(myl=L,eta1=round(1/L,5)))
	print(gradient_descent(fg=fg, x0=x0, eta=lambda x: 1/x, termtest=termtest))

	print("Gradient Descent with eta2 = 1/20L (or {eta2}), where L = {myl}:".format(myl=L,eta2=round(1/(20*L),5)))
	print(gradient_descent(fg=fg, x0=x0, eta=lambda x: 1/(20*x), termtest=termtest))

	print("Gradient Descent with eta3 = 20/L (or {eta3}), where L = {myl}:".format(myl=L,eta3=round(20/L,5)))
	print(gradient_descent(fg=fg, x0=x0, eta=lambda x: 20/x, termtest=termtest))
