class SettingsController():
	def __init__(self, widgetManager, settings):
		self.widgetManager = widgetManager
		self.settings = settings

	def getWidth(self):
		return self.settings.WIDTH.value

	def getHeight(self):
		return self.settings.HEIGHT.value

	def getIp(self):
		return self.settings.SERVER_IP.value

	def getPort(self):
		return self.settings.SERVER_PORT.value

	def getName(self):
		return self.settings.NAME.value

	def getFolder(self):
		return self.settings.FOLDER

	def onSaveButtonClick(self, settingsForm):
		self.settings.applyForm(settingsForm)
		self.widgetManager.loadMenuView()

