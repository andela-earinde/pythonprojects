from random import randint

def flip_coin(number):
	head = []
	tail = []
	for i in range(number):
		occur = randint(0, 1)
		if occur == 1:
			head.append(1)
		elif occur == 0:
			tail.append(0)
	return "you flipped the coin %d times. the outcome is %d heads"\
	       " and %d tails." %(number, len(head), len(tail))


if __name__ == '__main__':
	print """this is a simple program for simulating 
	         coin flipping"""

while True:
	number = int(raw_input("Enter the number of times you want to flip the coin: "))
	print flip_coin(number)



