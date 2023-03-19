class Date(object):  

	"""A class representing a month, day and year
	Attribute MONTHS: A CLASS ATTRIBUTE list of all month abbreviations in order
	Attribute DAYS: A CLASS ATTRIBUTE that is a dictionary. Keys are the strings from MONTHS; values are days in that month ('Feb' is 28 days)"""
	# Attribute _year: The represented year. An int >= 2000 (IMMUTABLE)
	# Attribute _month: The month. A valid 3-letter string from MONTHS (IMMUTABLE)
	# Attribute _day: The day. An int representing a valid day of _month (MUTABLE)

	# CLASS ATTRIBUTES.  ( Fill in missing part)
	MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	DAYS = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,
	'Sep':30,'Oct':31,'Nov':30,'Dec':31}


	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS not needed
	

	def getYear(self):

		"""Returns the year of this date"""
		return self._year

	def getMonth(self):
		"""Returns the month of this date"""
		
		return self._month

	def getDay(self):
		"""Returns the day of this date"""
		return self._day

	def isleapyear(self):
		"""Returns True if y is a leap year. False otherwise
		Precondition: y is an int >= 0"""
		assert isinstance(self.getYear(), int) and self.getYear() >= 0, repr(self.getYear()) + 'invalid year'
		if (self.getYear() % 400 == 0) and (self.getYear() % 100 == 0):
			return True
		elif (self.getYear() % 4 == 0) and (self.getYear() % 100 != 0):
			return True
		else:
			return False


	def setDay(self, value):
		"""Sets the day of this date
		Parameter value: The new day
		Precondition: value is a valid day in the month"""
		assert isinstance(value, int),'day should be integer'
		if self.isleapyear():
			assert 1 <= value <= 29 and self.getMonth() == 'Feb'
		else:
			assert 1 <= value <= (Date.DAYS)[self.getMonth()],'invalid day'
		
		self._day = value
		

	def __init__(self, d, mon, y):  
		"""Initializes a new date for the given month, day, and year

		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month

		Precondition: d is an int and a valid day for month m"""
		
		assert isinstance(y, int) and y >= 2000
		assert mon in self.MONTHS, 'it is not valid month'
		# self.setDay(d)
		self._month = mon
		self._year = y
		self.setDay(d)

		
	def __str__(self):
		"""Returns a string representation of this date.
		The representation is month day, year like this: 'Jan 2, 2002' """
		return str(self._month) + ' ' + str(self._day) + ', ' + str(self._year)

	def __lt__(self, other):
		"""Returns True if this date happened before other (False otherwise)

		Precondition: other is a Date

		This method causes a TypeError if the precondition is violated."""

		# IMPORTANT: You are limited to 20 lines. Do NOT brute force this.
		
		if isinstance(other, Date):
			if self.getYear() > other.getYear():
				return True
			elif self.getYear() == other.getYear() and ((self.MONTHS).index(self.getMonth()) < (self.MONTHS).index(other.getMonth())):
				return True
			elif (self.getYear() == other.getYear() and self.getMonth() == other.getMonth()) and self.getDay() > other.getDay():
				return True
			else:
				return False
		else:
			msg = 'invalid day'
			err = TypeError(msg)
			raise err

class DateTime(Date):
   # Fill in missing part
	"""A class representing a month, day and year, plus time of day (hours, minutes)"""
	# Attribute _hour: The hour of the day. An int in range 0..23 (MUTABLE)
	# Attribute _minute: The minute of the hour. An int in range 0..59 (MUTABLE)

	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.

	def getHour(self):
		"""Returns the hour of the day"""
		# Fill in missing part
		return self._hour

	def setHour(self, value):
		"""Sets the hour of the day
		Parameter value: The new hour
		Precondition: hour is an int in 0..23"""
		# Fill in missing part
		
		assert isinstance(value, int), 'invalid hour'
		assert 0<= value <=23 
		self._hour = value


	def getMinute(self):
		# """Returns the minute of the hour"""
		# Fill in missing part
		return self._minute

	def setMinute(self, value):
		assert isinstance(value, int), repr(value) + 'is invalid minute'
		assert value < 60
		self._minute = value

	def __init__(self, d, m, y, h=0, min=0): # Fill in missing part
		# """Initializes a new datetime for the given month, day, year, hour and minute
		# This method adds two additional (default) parameters to the initialize for
		# Date. They are hr (for hour) and mn (for minute).
		# Precondition: y is an int >= 2000 for the year
		# Precondition: m is a 3-letter string for a valid month
		# Precondition: d is an int and a valid day for month m
		# Precondition: hr is an int in the range 0..23 (OPTIONAL; default 0)
		# Precondition: mn is an int in the range 0..59 (OPTIONAL; default 0)"""
		# Fill in missing part
		super().__init__(d, m, y)
		self.setHour(h)
		self.setMinute(min)

	def __str__(self): # Fill in missing part
		# """Returns a string representation of this DateTime object
		# The representation is 'hh:mm on month day, year' like this: '9:45 on Jan 2, 2002'
		# Single digit minutes should be padded with 0s. Hours do not need to be padded."""
		
		# Fill in missing part
		return str(self._hour) + ':'+ str(self._minute) + ' on ' + super().__str__() 
d1 = DateTime(24, 'Feb', 2019, 9, 45)
d2 = DateTime(5, 'Mar', 2035, 8, 9)
