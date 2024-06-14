import re

class ValueObject():
	def __init__(self, value):
		self.verifyValue(value)
		self.value = value
	
	def verifyValue(self, value):
		raise NotImplementedError("verifyValue() not implemented in subclass")


class Ip(ValueObject):
	def verifyValue(self, value):
		if not isinstance(value, str):
			raise ValueError("Value is not a string.")
		if not self.checkIpFormat(value):
			raise ValueError(f"Value does not match IP format 'xxx.xxx.xxx.xxx' : {value}")

	def checkIpFormat(self, value):
		numbers = value.split(".")
		if len(numbers) != 4:
			return False
		for number in numbers:
			if not number.isdigit():
				return False
			number = int(number)
			if number < 0 or number > 255:
				return False
		return True

class Number(ValueObject):
	def __init__(self, value):
		super().__init__(value)
		self.value = int(value)

class PortNumber(Number):
	def verifyValue(self, value):
		try:
			value = int(value)
		except:
			raise ValueError("Value is not an integer.")
		else:
			if value <= 0 or value >= 65535:
				raise ValueError(f"Value is not between 0 and 65535 : {value}")


class PosInt(Number):
	def verifyValue(self, value):
		try:
			value = int(value)
		except:
			raise ValueError("Value is not an integer.")
		else:
			if  value < 0:
				raise ValueError(f"Value is not positive : {value}")


class Name(ValueObject):
	def verifyValue(self, value):
		if not isinstance(value, str):
			raise ValueError("Value is not a string.")
		elif len(value) == 0:
			return
		elif len(value) > 32:
			raise ValueError("Name is too long (max 32 characters).")
		elif not re.match(r"[\x00-\x7F]+", value):
			raise ValueError("Name is not valid UTF-8.")

