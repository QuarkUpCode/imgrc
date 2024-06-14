from .exceptions import UndefinedSettingError
from .ValueObjects import Ip, PortNumber, PosInt, Name

class Settings():
	def __init__(self, config_file):
		with open(config_file, "r") as f:
			self.config = f.readlines()

		self.SERVER_IP = Ip(self.__getSetting("SERVER_IP"))
		self.SERVER_PORT = PortNumber(self.__getSetting("SERVER_PORT"))
		self.WIDTH = PosInt(self.__getSetting("WIDTH"))
		self.HEIGHT = PosInt(self.__getSetting("HEIGHT"))
		self.NAME = Name(self.__getSetting("NAME"))
		self.FOLDER = self.__getSetting("FOLDER")


	def __getSetting(self, setting):
		for line in self.config:
			if setting in line:
				return line.split("=")[1].strip()
		raise UndefinedSettingError(setting)

	def setSetting(self, setting, value):
		for line in self.config:
			if setting in line:
				line = f"{setting}={value}\n"
		self.__saveSettings()

	def __saveSettings(self):
		with open(CONFIG_FILE, "w") as f:
			f.writelines(self.config)

	@property
	def width(self):
		return self.WIDTH.value

	@property
	def height(self):
		return self.HEIGHT.value

