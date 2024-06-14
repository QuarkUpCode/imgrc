from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class MenuWidget(QWidget):
	def __init__(self, listener):
		super().__init__()
		self.listener = listener
		
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)
		
		sendButton = QPushButton("Send Image")
		seeButton = QPushButton("See Image")
		settingsButton = QPushButton("Settings")
		sendButton.clicked.connect(lambda: self.OnSendClick())
		seeButton.clicked.connect(lambda: self.OnSeeClick())
		settingsButton.clicked.connect(lambda: self.OnSettingsClick())

		self.layout.addWidget(sendButton)
		self.layout.addWidget(seeButton)
		self.layout.addWidget(settingsButton)
		self.setLayout(self.layout)

	def OnSendClick(self):
		self.listener.OnSendClick()

	def OnSeeClick(self):
		self.listener.OnSeeClick()

	def OnSettingsClick(self):
		self.listener.OnSettingsClick()

