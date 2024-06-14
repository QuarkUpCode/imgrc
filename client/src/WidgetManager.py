from .MenuController import MenuController
from .MenuWidget import MenuWidget

class WidgetManager():
	def __init__(self, settings, mainWindow):
		self.settings = settings
		self.mainWindow = mainWindow
		self.currentController = MenuController(self)
		menuWidget = MenuWidget(self.currentController)
		self.mainWindow.loadWidget(menuWidget)

	def loadSendView(self):
		self.currentController = SenderController(self)
		senderWidget = SenderWidget(self.currentController)
		self.mainWindow.loadWidget(senderWidget)

	def loadSeeView(self):
		self.currentController = ViewerController(self)
		viewerWidget = ViewerWidget(self.currentController)
		self.mainWindow.loadWidget(viewerWidget)

	def loadSettingsView(self):
		self.currentController = SettingsController(self)
		settingsWidget = SettingsWidget(self.currentController)
		self.mainWindow.loadWidget(settingsWidget)

