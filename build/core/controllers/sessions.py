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
		if e != False:
			print(e)
		return False


def search_session(key, where='id'):
	sql = '''SELECT * FROM sessions WHERE '''+ str(where) +'''=?'''
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


"""

"""
def module_sessions(module):
	sql = '''SELECT * FROM sessions WHERE module=? ORDER BY id ASC'''
	try:
		cur.execute(sql, [module])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		if e != False:
			print(e)
		return False
	

"""

"""
def save_session(data):
	#Save new session data!
	sql = '''INSERT INTO sessions(tutor, day, start, end, room, module, slug, cat)
	VALUES(?,?,?,?,?,?,?,?)'''

	try:
		cur.execute(sql, data)
		conn.commit()
		return True
	except Exception as e:
		if e != False:
			print(e)
		return False



"""

"""
def update_session(update, new_data, session):
	#Update session data!
	sql = "UPDATE sessions SET " + update + " = ? WHERE id =?"
	try:
		cur.execute(sql, [new_data, session])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		if e != False:
			print(e)
		return False


"""

"""
def delete_session(session):
	#Update session data!
	sql = "DELETE FROM sessions WHERE id=?"
	try:
		cur.execute(sql, [session])
		conn.commit()
		return True
	except Exception as e:
		if e != False:
			print(e)
		return False