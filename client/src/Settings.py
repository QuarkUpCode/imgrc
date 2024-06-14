from .exceptions import UndefinedSettingError
from .ValueObjects import Ip, PortNumber, PosInt, Name


class SettingsBuilder():
	def __init__(self):
		self.SERVER_IP = None
		self.SERVER_PORT = None
		self.WIDTH = None
		self.HEIGHT = None
		self.NAME = None
		self.FOLDER = None

	def setIp(self, value):
		self.SERVER_IP = Ip(value)

	def setPort(self, value):
		self.SERVER_PORT = PortNumber(value)

	def setWidth(self, value):
		self.WIDTH = PosInt(value)

	def setHeight(self, value):
		self.HEIGHT = PosInt(value)

	def setName(self, value):
		self.NAME = Name(value)

	def setFolder(self, value):
		self.FOLDER = value

	def build(self):
		return Settings.fromBuilder(self)


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

	def update(self, form):
		if form.SERVER_IP is not None:
			self.setSetting("SERVER_IP", form.SERVER_IP.value)
		if form.SERVER_PORT is not None:
			self.setSetting("SERVER_PORT", form.SERVER_PORT.value)
		if form.WIDTH is not None:
			self.setSetting("WIDTH", form.WIDTH.value)
		if form.HEIGHT is not None:
			self.setSetting("HEIGHT", form.HEIGHT.value)
		if form.NAME is not None:
			self.setSetting("NAME", form.NAME.value)
		if form.FOLDER is not None:
			self.setSetting("FOLDER", form.FOLDER)

