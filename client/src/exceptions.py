class UndefinedSettingError(Exception):
	def __init__(self, setting):
		super().__init__(f"Setting {setting} not defined.")
