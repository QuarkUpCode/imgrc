from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class SettingsWidget(QWidget):
	def __init__(self, listener):
		super().__init__()
		self.listener = listener

		self.layout = QVBoxLayout()
		self.layout.setSpacing(10)
		self.layout.setContentsMargins(0,0,0,0)

		self.addDimensionsLayout()
		self.addServerLayout()
		self.addLocalLayout()
		
		self.setLayout(self.layout)

	def addLabelAndLineEdit(self, label, lineEdit):
		layout = QHBoxLayout()
		layout.addWidget(QLabel(label))
		layout.addWidget(QLineEdit(lineEdit))
		self.layout.addLayout(layout)

	def addDimensionsLayout(self):
		self.addLabelAndLineEdit("Width", str(self.listener.getWidth()))
		self.addLabelAndLineEdit("Height", str(self.listener.getHeight()))
	
	def addServerLayout(self):
		self.addLabelAndLineEdit("Server IP", self.listener.getIp())
		self.addLabelAndLineEdit("Server Port", str(self.listener.getPort()))

	def addLocalLayout(self):
		self.addLabelAndLineEdit("Name", self.listener.getName())
		self.addLabelAndLineEdit("Folder", self.listener.getFolder())

