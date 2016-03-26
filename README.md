# REST-API-Challenge
REST-API Challenge

Run the main.py file.

The Chgallenge- REST API - layer:

In this test you are required to develop a small scale widget API by the following spec:
The system should get a web request with the following parameters - Widget name, widget parameters. For example the call should be in post to the URL localhost/method with the following payload:{widgetName=abc,params={fromDate:"1\2\2016",toDate:"2\2\2016",cust_id:"20"}}
The system should return the results of the query in JSON format
A widget object template contains SQL query and parameters (names and types) - a template will be saved in file in JSON/XML format (your call)
On load, the service should get a directory as parameter and loads all template files into dictionary
The query process should be as follow:
We should first resolve the widget name from the loaded widget dictionary
If the widget exists we should validate that all parameters are there and the types are correct
format the query with the given parameters
execute the query against mysql
return results as JSON
An example query on our data can be:

Widgit 1 (events per day for last x days):

ReceiveParams = { "clinet_id":int, "from_date":datetime, "to_date":datetime },
QueryText = "
SELECT clinet_id,count(*) AS events_count
FROM events
WHERE (event_ts >= {1} and event_ts < {2}
AND clinet_id = {0}
GROUP BY 1
ORDER BY 1,
"

Definitions:
events table
	event_id int
	event_ts datetime
	event_type int (1 = impression, 2 = click, 3 = purchase...)
	clinet_id into

you can use flask or django
