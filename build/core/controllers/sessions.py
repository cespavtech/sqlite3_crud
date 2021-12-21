"""
======================
Sessions Controller
======================
This file is responsible for actions related to sessions,
Updating deleting creating etc

"""

#Database
import config

conn = config.con #Establish connection to the database!
cur = conn.cursor()

def get_session(key):
	sql = '''SELECT * FROM sessions WHERE id=? OR slug=?'''
	try:
		cur.execute(sql, [key, key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row[0]
	except Exception as e:
		print(e)
		return False


"""

"""
def module_sessions(module):
	sql = '''SELECT * FROM sessions WHERE module=?'''
	try:
		cur.execute(sql, [module])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		print(e)
		return e
	

"""

"""
def save_session(data):
	#Save new session data!
	sql = '''INSERT INTO sessions(tutor, day, start, end, room, module, slug)
	VALUES(?,?,?,?,?,?,?)'''

	try:
		cur.execute(sql, data)
		conn.commit()
		return True
	except Exception as e:
		print(e)
		return e