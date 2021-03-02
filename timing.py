import time

def calculate_time(func, x):
	'''
	Calculate the run time of the inputed function.

	Parameters
	----------
	func : function
		The function to test for run time.

	Returns
	----------
	sting
		The run time of the inputed function in seconds.
	'''
	a = time.time()
	d = func(x)
	b = time.time()
	c = int(b - a)
	print(f"Total time {c}")
	return f"Total time {c}"

calculate_time(time.sleep, 2)
