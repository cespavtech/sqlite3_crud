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
		if e != False:
			print(e)
		return False


def search_room(key, where='id'):
	sql = '''SELECT * FROM rooms WHERE '''+ str(where) +'''=?'''
	try:
		cur.execute(sql, [key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		if e != False:
			print(e)
		return False



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
		if e != False:
			print(e) #Coment this to turn off debugging
		return False


def update_room(update, new_data, room):
	sql = "UPDATE rooms SET " + update + " = ? WHERE id =?"
	try:
		cur.execute(sql, [new_data, room])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		if e != False:
			print(e)
		return False


def save_room(data):
	sql = '''INSERT INTO rooms(name, slug) VALUES(?,?)'''
	try:
		cur.execute(sql, data)
		return True
	except Exception as e:
		if e != False:
			print(e)
		return False