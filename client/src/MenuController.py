class MenuController():
	def __init__(self, widgetManager):
		self.widgetManager = widgetManager
	
	def OnSendClick(self):
		self.widgetManager.loadSendView()
	
	def OnSeeClick(self):
		self.widgetManager.loadSeeView()
	
	def OnSettingsClick(self):
		self.widgetManager.loadSettingsView()

