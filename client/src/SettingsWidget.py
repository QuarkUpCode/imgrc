from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class SettingsWidget(QWidget):
    def __init__(self, listener, settings):
		super().__init__()
		self.listener = listener
		self.settings = settings

		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)

		self.layout.addLayout(self.getDimensionsLayout())
		self.layout.addLayout(self.getServerLayout())
		self.layout.addLayout(self.getLocalLayout())
		
		self.setLayout(self.layout)

	def getDimensionsLayout(self):
		dimensionsLayout = QHBoxLayout()
		dimensionsLayout.setSpacing(0)
		dimensionsLayout.setContentsMargins(0,0,0,0)
		dimensionsLayout.addWidget(QLabel("Width "))
		dimensionsLayout.addWidget(QLineEdit(settings.WIDTH.value))
		dimensionsLayout.addWidget(QLabel("Height "))
		dimensionsLayout.addWidget(QLineEdit(settings.HEIGHT.value))
		return dimensionsLayout
	
	def getServerLayout(self):
		serverLayout = QHBoxLayout()
		serverLayout.setSpacing(0)
		serverLayout.setContentsMargins(0,0,0,0)
		serverLayout.addWidget(QLabel("Server IP "))
		serverLayout.addWidget(QLineEdit(settings.SERVER_IP.value))
		serverLayout.addWidget(QLabel("Server Port "))
		serverLayout.addWidget(QLineEdit(settings.SERVER_PORT.value))
		return serverLayout

	def getLocalLayout(self):
		localLayout = QHBoxLayout()
		localLayout.setSpacing(0)
		localLayout.setContentsMargins(0,0,0,0)
		localLayout.addWidget(QLabel("Name "))
		localLayout.addWidget(QLineEdit(settings.NAME.value))
		localLayout.addWidget(QLabel("Folder "))
		localLayout.addWidget(QLineEdit(settings.FOLDER.value))
		return localLayout
