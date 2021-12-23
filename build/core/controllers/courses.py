"""
======================
Courses Controller
======================
This file is responsible for actions related to courses,
Updating deleting creating etc

"""

#Database
import config

conn = config.con #Establish connection to the database!
cur = conn.cursor()

def get_courses(key, where = "id"):
	sql = '''SELECT * FROM courses WHERE ''' + where + '''=?'''
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

def get_modules(course):
	sql = '''SELECT * FROM modules WHERE course=?'''
	try:
		cur.execute(sql, [course])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		if e != False:
			print(e)
		return False

def update_course(update, new_data, course_id):
	sql = "UPDATE courses SET " + update + " = ? WHERE id =?"
	try:
		cur.execute(sql, [new_data, course_id])
		row = cur.fetchall()
		if len(row) < 1:
			#Nothing found!
			return False
		return row
	except Exception as e:
		if e != False:
			print(e)
		return False

def save_course(data):
	sql = '''INSERT INTO courses(name, slug) VALUES(?,?)'''
	try:
		cur.execute(sql, data)
		return True
	except Exception as e:
		if e != False:
			print(e)
		return False
	

