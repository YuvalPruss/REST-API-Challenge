import re

class Widget(object):
	def __init__(self, name, parameters, query):
		"""
		Creat instance of the object by getting the login details to the DB from the user.
		Get:
		name -> widget's name
		parameters -> widget's parameters
		query -> widget's sql query
		"""
		self.name = name
		#Create empty list of parameters 
		self.parameters = []
		#Go over the parameters list
		for parameter in parameters:
			#add the parameters to the parameters list
			self.parameters.append({"name" : parameter["paramName"] , "type" : parameter["paramType"]})
		self.query = query
	def __str__(self):
		"""
		Print data about the instance of the object.
		"""
		return "name: %s \nparameters: %s \nquery: %s" % (self.name, self.parameters, self.query)
	def translateQueryToSQL(self, clientParameters):
		"""
		Put the user's parameters into the sql query
		Get:
		clientParameters -> The values the user give to put into the sql 
		Return:
		The sql query with the values which the user gave us
		"""
		returnSql = self.query
		#Validate that all parameters exists in the parameters given by the user
		for i , parameter in enumerate(self.parameters):
			if parameter['name'] in clientParameters:
				try:
					#Check if the parameter is in the correct type, otherwise raise an error
					if parameter['type'] == "int":
						var = int(clientParameters[parameter['name']])
					if parameter['type'] == "datetime":
						#Check if the parameter is in the datetime type using regex
						r = re.compile('^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}$')
						if r.search(clientParameters[parameter['name']]) is None:
							raise ValueError("The type of the parameter isn't correct!")
					#Other types goes here...
				except:
					raise ValueError("The type of the parameter isn't correct!")
			else:
				raise ValueError("Parameter isn't exists in the parameters given by the user!")

		#Go over the parameter's list, where i indicates the location of the parameter in the list
		for i , parameter in enumerate(self.parameters):
			#The replaced string, which is replaced by the value given by the user
			replaced = "{" + str(i) + "}"
			replacedBy = clientParameters[parameter['name']]
			#Replacing the replaced string by the value
			returnSql = returnSql.replace(replaced , replacedBy)
		#Returning the correct sql query
		return returnSql