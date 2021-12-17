"""
*****************************************************

********************USER PROFILE MODULE**************

@param userid > Current user id from users table

"""

#Database configs
import config


"""
Return current user profile data
@param user_data[] > Single row from users table [PRIMARY KEY = email]

"""
def current_user(userid):

	user_data = []

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Fetch user from database!

	sql = "SELECT id FROM users WHERE email=?"

	cur.execute(sql, [username])

	user_row = cur.fetchall()

	user_data = user_row[0]
	
	return user_data


"""
Get user ID

"""
def user_id(username):

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Fetch user from database!

	sql = "SELECT id FROM users WHERE email=?"

	cur.execute(sql, [username])

	user_row = cur.fetchall()

	#Assign the id from database
	userid = user_row[0][0]

	#Return the fetched id
	return userid