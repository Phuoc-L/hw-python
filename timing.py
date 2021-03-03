import time

def calculate_time(func):
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
	def inner():
		x = time.time()
		func()
		print(f"Total time {int(time.time() - x)}")
	return inner
	
@calculate_time
def sleep():
	time.sleep(2)

sleep()
