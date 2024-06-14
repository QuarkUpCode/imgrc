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
		sendButton.clicked.connect(lambda: self.clicked(0))
		seeButton.clicked.connect(lambda: self.clicked(1))
		settingsButton.clicked.connect(lambda: self.clicked(2))

		self.layout.addWidget(sendButton)
		self.layout.addWidget(seeButton)
		self.layout.addWidget(settingsButton)
		self.setLayout(self.layout)

	def clicked(self, index):
		self.listener.clicked(index)

