from .Menu import Menu
from .MenuWidget import MenuWidget

class WidgetManager():
	def __init__(self, settings, mainwindow):
		self.settings = settings
		self.mainwindow = mainwindow
		self.currentManager = Menu(self)
		menuwidget = MenuWidget(self.currentManager)
		self.mainwindow.loadWidget(menuwidget)

