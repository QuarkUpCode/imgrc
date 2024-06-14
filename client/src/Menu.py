class Menu():
	def __init__(self, widgetManager):
		self.widgetManager = widgetManager

	def clicked(self, index):
		print(f"Button {index} clicked")
