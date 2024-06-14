from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from .Settings import SettingsDTO

class SettingsWidget(QWidget):
	def __init__(self, listener):
		super().__init__()
		self.listener = listener
		self.settings = []

		self.layout = QVBoxLayout()
		self.layout.setSpacing(10)
		self.layout.setContentsMargins(0,0,0,0)

		self.addDimensionsLayout()
		self.addServerLayout()
		self.addLocalLayout()
		saveButton = QPushButton("Save")
		saveButton.clicked.connect(lambda: self.onSaveClick())
		self.layout.addWidget(saveButton)
		
		self.setLayout(self.layout)

	def onSaveClick(self):
		settings = []
		for lineEdit in self.settings:
			settings.append(lineEdit.text())
		settings[0], settings[2] = settings[2], settings[0]
		settings[1], settings[3] = settings[3], settings[1]
		settingsDto = SettingsDTO.fromList(settings)
		self.listener.onSaveButtonClick(settingsDto)

	def addLabelAndLineEdit(self, label, lineEdit):
		layout = QHBoxLayout()
		layout.addWidget(QLabel(label))
		self.settings.append(QLineEdit(lineEdit))
		layout.addWidget(self.settings[-1])
		self.layout.addLayout(layout)

	def addDimensionsLayout(self):
		self.addLabelAndLineEdit("Default width", str(self.listener.getWidth()))
		self.addLabelAndLineEdit("Default height", str(self.listener.getHeight()))
	
	def addServerLayout(self):
		self.addLabelAndLineEdit("Server IP", self.listener.getIp())
		self.addLabelAndLineEdit("Server Port", str(self.listener.getPort()))

	def addLocalLayout(self):
		self.addLabelAndLineEdit("Name", self.listener.getName())
		self.addLabelAndLineEdit("Folder", self.listener.getFolder())

