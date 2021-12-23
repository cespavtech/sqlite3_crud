"""
======================
Modules Controller
======================
This file is responsible for actions related to modules,
Updating deleting creating etc

"""

#Database
import config

conn = config.con #Establish connection to the database!
cur = conn.cursor()

def get_modules(key, where = "id"):
	sql = '''SELECT * FROM modules WHERE ''' + where + '''=?'''
	try:
		cur.execute(sql, [key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		else:
			return row
	except Exception as e:
		if e != False:
			print(e)
		return False

def guess_modules(key):
	sql = '''SELECT * FROM modules WHERE id=? OR slug=?'''
	try:
		cur.execute(sql, [key, key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		else:
			return row
	except Exception as e:
		if e != False:
			print(e)
		return False

def get_course(key):
	sql = '''SELECT * FROM courses WHERE id=? OR slug=?'''
	try:
		cur.execute(sql, [key, key])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		else:
			return row
	except Exception as e:
		if e != False:
			print(e)
		return False
	


"""

"""
def save_module(data):
	#Save new session data!
	conn = config.con #Establish connection to the database!
	cur = conn.cursor()
	sql = '''INSERT INTO modules(name, slug, course)
	VALUES(?,?,?)'''

	try:
		cur.execute(sql, data)
		conn.commit()
		return True
	except Exception as e:
		if e != False:
			print(e)
		return False

def update_module(update, new_data, module):
	#Save new session data!
	conn = config.con #Establish connection to the database!
	cur = conn.cursor()
	sql = "UPDATE modules SET " + update + " = ? WHERE id =?"

	try:
		cur.execute(sql, [new_data, module])
		conn.commit()
		return True
	except Exception as e:
		if e != False:
			print(e)
		return False