""" this agent will find and execute command by user pass it to store file for storing data """

class Action:
	"""docstring for action"""
	def __init__(self,usrInput):
		# super(action, self).__init__()
		self.input =  usrInput
	def takeAction(self):
		return self.input