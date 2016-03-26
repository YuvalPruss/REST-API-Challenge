from widget import Widget
import json

class WidgetsReader(object):
	def __init__(self, config_file):
		"""
		Creat instance of the object by getting the config json file path.
		config_file -> json configuration file, which contains the information about the widgets
		"""
		#Create empty list of widgets
		self.widgets = []
		#Read the json file into a data dictionary
		with open(config_file) as data_file:
			data = json.load(data_file)
		#In this data dictionary, go to the value of widgets, which contains the information about the widgets
		for widget in data["widgets"]:
			#Put the widget name into name variable
			name = widget["widgetName"]
			#Put the widget parameters into parameters variable
			parameters = widget["receiveParams"]
			#Put the widget query into query variable
			queryText = widget["queryText"]
			#Create widget instance
			w = Widget(name, parameters, queryText)
			#Add this widget to the widgets list
			self.widgets.append(w)
	def isWidgetNameExist(self, widgetName):
		"""
		Check whether the widget name given by the user is equal to one of the widget names in the list
		Get:
		Widget name
		Return:
		If the widget exist, returns True. If not, returns False.
		"""
		#Go over the widget list
		for widget in self.widgets:
			#Check whether the widget name given by the user is equal to one of the widget names in the list
			if widget.name == widgetName:
				#If the widget exist, returns True
				return True
		#If the widget doesn't exist, return False
		return False
	def getWidgetByName(self, widgetName):
		"""
		Get a widget by his name
		Get:
		widgetName -> Widget name
		Return:
		If the widget exist, returns the widget. If not, returns False.
		"""
		#Go over the widget list
		for widget in self.widgets:
			#Check whether the widget name given by the user is equal to one of the widget names in the list
			if widget.name == widgetName:
				#If exist, return the widget
				return widget
		#If the widget doesn't exist, return False
		return False
	def __str__(self):
		"""
		Print data about the instance of the object.
		"""
		res = "Widgets:\n"
		#Go over the widget list
		for widget in self.widgets:
			#Get widget info
			res += widget.__str__()
			#Add new line
			res += "\n"
		return res