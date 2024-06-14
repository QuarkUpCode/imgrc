from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon


WINDOW_TITLE = "ImgRC"
ICON_FILE = "ressources/app_icon.png"


class MainWindow(QMainWindow):
	def __init__(self, settings):
		super().__init__()
		self.settings = settings
		self.setGeometry(10, 10,self.settings.width, self.settings.height)
		self.setWindowTitle(WINDOW_TITLE)
		self.setWindowIcon(QIcon(ICON_FILE))
		self.setCentralWidget(None)
		self.setContentsMargins(0,0,0,0)
		self.show()

