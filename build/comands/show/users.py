"""
======================
User Displaying
======================
This module is responsible for displaying users from database
If current user has no preveleges, nothing is shown

@param item_data{}

"""

#Database

import config

#Permissions

from build.users.security import permissions as user_permission

#Item table fields

from build.core.inputs import items

#Error displays

from vendor.views.core import error_prompt as error_displays

#Shell display messages

from vendor.views.core import shell_prompts as shell_displays

#When displaying item profile data
#We will use views from this folder

from vendor.views.actions.show import users as user_show

#We will use this to create item_data{}
#This value will be passed to the rendor function to display item profile
#This is for users table structure

from configs.database.structures import users as item_table

"""
======================
Item Display Method
======================

This is method called when displaying data

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'disp')

	#Permission
	perm = user_permission.check_permission(userid)

	#Validate comand arguments
	if len(cmd) < 3:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return 1
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Check scope to search user with

	raw_keyw = cmd[2].split()

	#Validation
	if len(raw_keyw) < 2:
		shell_displays.invalid_args(cmd[0])
		return 1

	keyw = raw_keyw[1]

	#Check field to search in 

	raw_field = raw_keyw[0]
	filed_lists = items.item_fields[cmd[1]]

	#Validation
	if raw_field in filed_lists:
		pass
		field = filed_lists[raw_field]
	else:
		shell_displays.invalid_args(cmd[0])
		return 1

	"""
	=====================
	Display User Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search user with
	Display user from table using keyw as search using the selected field

	"""

	print("Searching in users using " + keyw + " as user " + field)

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Check wether user is found!

	sql = "SELECT * FROM users WHERE " + field + "=?"

	cur.execute(sql, [keyw])

	user_row = cur.fetchall()

	#Is user found!???
	if len(user_row) < 1:
		print(error_displays.no_account)
		return


	#User is found!
	#Load profile display view

	"""
	=================
	Create Item Profile
	=================

	"""
	profile_field = item_table.table_structure
	new_profile = {}
	#Loop through the table fields
	for i in profile_field:
		#Assign value if field exists in the sql row
		print("Looking for [" + str(i) + "]...")
		new_user_row = user_row[0]
		if profile_field[i] < len(new_user_row):
			#Field found
			print("Found [" + str(i) + "] data...")
			#Assing value
			new_profile[i] = new_user_row[profile_field[i]]
		else:
			print(error_displays.table_field_not_found)
		
	#End loop!

	"""
	==========================
	Create User Modules Profile
	==========================
	We will fetch all module associated with the user,
	The show method will determin how to display these data
	Based on account type of the user we are displaying profile data for
	"""

	sql = """SELECT * FROM user_modules WHERE uid=?"""
	cur.execute(sql, [keyw])
	#Fetch data if any!
	user_modules_row = cur.fetchall()

	print(item_table.table_structure)

	user_show.rendor(new_profile, user_modules_row)







