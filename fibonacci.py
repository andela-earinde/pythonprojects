
def fibonacci(number):
	fib = []
	a, b = 0, 1
	for i in range(number):
		fib.append(b)
		a, b = b, a+b
	return fib


if __name__ == '__main__':
	print "this is a module to compute the fibonacci sequence up to a specific value"


while True:
	number = int(raw_input('type in a number: '))
	if type(number) != type(1)
		print "please enter an integer value"

	else:
		print fibonacci(number)