"""
======================
User Modules Assigning
======================
This module is responsible for creating new user courses records
If current user has no preveleges, nothing is processed
If a course is assigned to the user, all modules under that course will be assigned to the user
Once the course has been removed, all the modules are also removed!

"""

#Database
import config

#Permissions
from build.users.security import permissions as user_permission

#User table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Shell clobal options [e.g. q/Q for quit]
from build.core import shell_options as shell_choice


"""

"""
def boot(userid, cmd):
	print("Assigning items to user...")
	new_cmd = cmd
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'ass')

	#Permission
	perm = user_permission.check_permission(userid)


	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return

	#Validate comand arguments
	if len(new_cmd) < 5:
		#Invalid arguments
		shell_displays.invalid_args(new_cmd[0])
		return

	#Check scope to search user with

	raw_keyw = cmd[3].split()

	#Validation
	if len(raw_keyw) < 2:
		shell_displays.invalid_args(cmd[0])
		return

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
		return

	#Check wether using email or id
	#If not, return error and force email/id
	if not raw_field in ('ui', 'ue'):
		#Invalid user selection!
		print(error_displays.no_account)
		return

	#Check user availability!

	sql = "SELECT id FROM users WHERE " + field + "=?"

	cur.execute(sql, [keyw])

	user_row = cur.fetchall()

	#Is user found!???
	if len(user_row) < 1:
		print(error_displays.no_account)
		return


	#User is found!

	new_userid = user_row[0][0]

	#New user permission
	new_perm = user_permission.check_permission(new_userid)

	if cmd[2] == 'c':
		#Assigning course to user
		print("Assigning course...")
	elif cmd[2] == 'm':
		print("Assigning modules...")

		#Check wether the user to assign module to is a staff!

		if new_perm != 'staff':
			#User to assign is not a staff,
			#Return user not found error!
			print(error_displays.no_account)
			return

	print("New data assigned with success...")

