from flask import Flask , jsonify
from widgetsReader import WidgetsReader
from db import DB
import ast
app = Flask(__name__)

@app.route("/widget/" , methods=['POST'])
def widgets():
	try:
		#Receive data from the user- POST Method
		widgetName = request.form['widgetName']
		#check values:
		#widgetName = "total_events"
		#widgetName = "events"
		params = request.form['params']
		#check values:
		#params = '{"client_id" : "3"}'
		#params = '{"client_id" : "2", "from_date" : "2014-03-23 19:56:31", "to_date" : "2017-03-23 00:00:00"}'
	except:
		raise ValueError("Error receiving data from the user!")
	try:
		#Convert the dictionart string into a real dictionary
		params = ast.literal_eval(params)
	except:
		raise ValueError("Error converting the paramter's into dictionary!")

	#Check if the widget exists
	if widgetsReader.isWidgetNameExist(widgetName):
		#Get the widget
		widget = widgetsReader.getWidgetByName(widgetName)
		#Put the user's parameters into the sql query
		sql = widget.translateQueryToSQL(params)
		#Execute the query to the database
		res = db.sql_select(sql)
	else:
		raise ValueError("Called Widget Doesn't Exist!")
	#Convert the dictionary result into json format and return it
	return jsonify(res)

if __name__ == "__main__":
	#Load the widgets settings
	widgetsReader = WidgetsReader("config.json")
	try:
		#Create connection to the DB
		db = DB("localhost" , "root", "", "system")
		#Connect to the DB
		db.connect_db()
	except:
		raise ValueError("Problem connecting to DB!")
	#Run application
	app.debug = True
	app.run()