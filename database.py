import MySQLdb

from pysqlite2 import dbapi2 as sqlite 
class Database:
	
	def getConnection(self):
		try:
			#conn = MySQLdb.connect(host = "localhost",
			#					user = "root",
			#					passwd = "zeus",
			#					db = "repository")
			
			connection = sqlite.connect('repository.db')
			
			return connection 
		except (MySQLdb.Error, e):
			print ('Error %d : %s' % (e.args[0], e.args[1]))
			sys.exit(1)
