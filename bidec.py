if __name__ == '__main__':
	print "Enter B to convert decimal to binary \n"\
	      "and D to convert binary to decimal"

def converter(num, letter):
	if letter == "B":
		return bin(int(num))[2:]
	elif letter == "D":
		con = "%s%s" %("0b", num)
		return int(con, base=2)


while True: 
	input = raw_input("Enter a letter: ")
	if input.isalpha():
		try:
			inp = raw_input("Enter the number to convert: ")
			print converter(inp, input)
		except ValueError:
			print "enter a valid decimal or binary Number"		
	else:
		print "Please input a valid letter"
		