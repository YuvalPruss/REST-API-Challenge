import MySQLdb

class DB(object):
	def __init__(self, server, user, password, db_name):
		"""
		Creat instance of the object by getting the login details to the DB from the user.
		Get:
		server -> The server name runs the db
		user -> The user name to the db
		password -> The password to the db
		db_name -> The selected database name
		"""
		self.server = server
		self.user = user
		self.password = password
		self.db_name = db_name
	def __str__(self):
		"""
		Print data about the instance of the object.
		"""
		return "Server: " + self.server + "\nUser:" + self.user + "\nPassword:" + self.password + "\nDB Name:" + self.db_name
	def connect_db(self):
		"""
		Connect to the database and create cursor to it.
		"""
		try:
			#Connect to the DB
			self.cnx = MySQLdb.connect(host=self.server,user=self.user,passwd=self.password,db=self.db_name)
			#Create cursor to the DB
			self.cur = self.cnx.cursor()
		except:
			raise ValueError("Problem connecting to DB!")
	def sql_select(self,sql):
		"""
		Execute query to the database and return the result.
		Get:
		sql -> SQL query which shoult be execute
		Return:
		Result of this query as a dictionary
		"""
		try:
			#Execute the sql query
			self.cur.execute(sql)
			#Get the selected columns and arrange it on the list
			field_names = [i[0] for i in self.cur.description]
			#Fetch the result into a row 
			row = self.cur.fetchone()
			#Get the selected columns values and arrange it on the list
			result_values = [i for i in row]
			#Create a dictionary from the columns names and values
			res = dict(zip(field_names , result_values))
		except:
			raise ValueError("Problem in executing the query to the database!")
		#Return this dictionary
		return res