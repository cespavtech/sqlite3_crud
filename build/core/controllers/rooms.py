"""
======================
Rooms Controller
======================
This file is responsible for actions related to rooms,
Updating deleting creating etc

"""

#Database
import config

conn = config.con #Establish connection to the database!
cur = conn.cursor()

def get_room(key):
	sql = '''SELECT * FROM rooms WHERE id=? OR slug=?'''
	try:
		cur.execute(sql, [key, key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row[0]
	except Exception as e:
		return e



def sessions(key):
	sql = '''SELECT * FROM sessions WHERE room=?'''
	try:
		cur.execute(sql, [key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		print(e) #Coment this to turn off debugging
		return False