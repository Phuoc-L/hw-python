def calculate_apr(principal, interest_rate, years):
	"""
	Calculate investment after some years.

	This function will calculate the total amount of money you will earn after some
	years with a certain interest rate.

	Parameters
	----------
	principal : float or int
		The starting amount of money.
	interest_rate : float
		The interestn rate of the investment (yearly).
	years : int
		The number of years of your investment.

	Returns
	----------
	int
		The total amount of money after the time of investment.
	boolean
		False if parameters are invalid.
	"""
	if((isinstance(principal, float) or isinstance(principal, int)) and isinstance(interest_rate, float) and interest_rate > 0 and isinstance(years, int) and years > 0):
		for i in range(years):
			principal = principal * (1 + interest_rate)
		print(principal)
		return principal
	print(False)
	return False

calculate_apr(100, 0.03, -3)
