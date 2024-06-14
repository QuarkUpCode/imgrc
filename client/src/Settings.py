from .exceptions import UndefinedSettingError
from .ValueObjects import Ip, PortNumber, PosInt, Name


class SettingsDTO():
	@classmethod
	def fromList(cls, list):
		settings = cls()
		settings.SERVER_IP = Ip(list[0])
		settings.SERVER_PORT = PortNumber(list[1])
		settings.WIDTH = PosInt(list[2])
		settings.HEIGHT = PosInt(list[3])
		settings.NAME = Name(list[4])
		settings.FOLDER = list[5]
		return settings
	
	def __init__(self):
		self.SERVER_IP = None
		self.SERVER_PORT = None
		self.WIDTH = None
		self.HEIGHT = None
		self.NAME = None
		self.FOLDER = None


class Settings():
	@classmethod
	def fromBuilder(cls, builder):
		settings = cls()
		settings.SERVER_IP = builder.SERVER_IP
		settings.SERVER_PORT = builder.SERVER_PORT
		settings.WIDTH = builder.WIDTH
		settings.HEIGHT = builder.HEIGHT
		settings.NAME = builder.NAME
		settings.FOLDER = builder.FOLDER
		return settings

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

	def update(self, dto):
		self.SERVER_IP = dto.SERVER_IP
		self.SERVER_PORT = dto.SERVER_PORT
		self.WIDTH = dto.WIDTH
		self.HEIGHT = dto.HEIGHT
		self.NAME = dto.NAME
		self.FOLDER = dto.FOLDER

