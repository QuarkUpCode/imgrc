from .Settings import Settings
from .MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication


CONFIG_FILE = "config.txt"
DEFAULT_CONFIG_FILE = "src/default_config.txt"


def loadSettings():
	try:
		settings = Settings(CONFIG_FILE)
	except FileNotFoundError:
		print(f"Settings file {CONFIG_FILE} not found. Using default settings.")
		settings = Settings(DEFAULT_CONFIG_FILE)
	return settings

def main():
	settings = loadSettings()

	app = QApplication([])
	mainwindow = MainWindow(settings)
	app.exec_()
	# Nothing shall be executed after this point

if __name__ == "__main__":
	main()

