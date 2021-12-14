"""
*****************************************************

********************USER PROFILE MODULE**************

@param userid > Current user id from users table

"""


"""
Return current user profile data
@param user_data[] > Single row from users table [PRIMARY KEY = email]

"""
def current_user(userid):
	user_data = [1, 'Abdirahim Abdi', 'connectabduu@gmail.com']

	return user_data


"""
Get user ID

"""
def user_id(username):
	userid = 1
	return userid