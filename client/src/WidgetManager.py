from .MenuController import MenuController
from .MenuWidget import MenuWidget
from .SenderController import SenderController
from .SenderWidget import SenderWidget
from .ViewerController import ViewerController
from .ViewerWidget import ViewerWidget
from .SettingsController import SettingsController
from .SettingsWidget import SettingsWidget

class WidgetManager():
	def __init__(self, settings, mainWindow):
		self.settings = settings
		self.mainWindow = mainWindow
		self.loadMenuView()

	def reloadSettings(self):
		self.mainWindow.reloadSettings()

	def loadMenuView(self):
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
		self.currentController = SettingsController(self, self.settings)
		settingsWidget = SettingsWidget(self.currentController)
		self.mainWindow.loadWidget(settingsWidget)

