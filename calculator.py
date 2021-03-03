def calculator(number1, number2, operator):
	'''
	Calculate the value of two numbers.

	This function do math on two numbers by the inputed operation.

	Parameters
	----------
	number1 : float
		The first number.
	number2 : float
		The second number.
	perator : string
		The math operator to preform on the two numbers.

	Return
	----------
	float
		The result of the math operation between the two numbers.

	'''
	number1 = float(number1)
	number2 = float(number2)
	if(operator == "+"):
		print(number1 + number2)
		return number1 + number2
	elif(operator == "-"):
		print(number1 - number2)
		return number1 - number2
	elif(operator == "*"):
		print(number1 * number2)
		return number1 * number2
	elif(operator == "/"):
		print(number1 / number2)
		return number1 / number2
	elif(operator == "**"):
		print(number1 ** number2)
		return number1 ** number2


def input_output():
	'''
	Take inputs from the user and calculate.

	This function collect two values from the user and then preform a math operation on them.

	Condition
	---------
	Will continuously ask the user for two values and operator until the user exits.
	'''
	done = False
	while not(done):
		num1 = input("Enter the first number: ")
		num2 = input("Enter the second number: ")
		op = input("Enter the operation: ")
		if (op != "+" and op != "-" and op != "*" and op != "/" and op != "**"):
			done = True
			print("False")
			return False
		else:
			calculator(num1, num2, op)
			print(" ")
			exit = input("Do you want to exit? ")
			if (exit == 'y'):
				done = True


