"""
======================
Users Controller
======================
This file is responsible for actions related to users,
Updating deleting creating etc

"""

#User modules
from build.core.controllers import modules as modules_controller

#Database
import config

conn = config.con #Establish connection to the database!
cur = conn.cursor()

def get_profile(key):
	sql = '''SELECT * FROM users WHERE id=? OR email=?'''
	try:
		cur.execute(sql, [key, key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row[0]
	except Exception as e:
		return e

def get_courses(user):
	sql = """SELECT * FROM user_courses WHERE uid=?"""
	try:
		cur.execute(sql, [user])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		return e

def get_sessions(user):
	sql = """SELECT * FROM sessions WHERE tutor=?"""
	try:
		cur.execute(sql, [user])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		return e

def save_user(data):
	#Save new user account
	sql = ''' INSERT INTO users(name, email, password, account)
              VALUES(?, ?, ?, ?) '''
	try:
		cur.execute(sql, data)
		conn.commit()
		return True
	except Exception as e:
		return e
