"""
======================
User Account Creating
======================
This module is responsible for creating new user records
If current user has no preveleges, nothing is processed

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

	#New user profile
	new_profile = {}
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid))
	#Permission
	perm = user_permission.check_permission(userid)
	
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Create profile data for new user

	filed_lists = items.item_fields[cmd[1]]

	for i in cmd:
		#Loop through all currently selected arguments
		j = i.split()
		if len(j) > 1:
			#Thats an argument!
			raw_field = j[0]

			#Update new user profile
			if raw_field in filed_lists:
				key_value = i.replace(raw_field + " ", "")
				new_profile[filed_lists[raw_field]] = key_value

	#End updating new user pforile

	#Validation of new user profile completion

	for i in filed_lists:
		#Check wether its id
		if filed_lists[i] != 'id':
			#Not id, check wether it has been set for our new user
			if not filed_lists[i] in new_profile:
				#Not updated, force selection
				shell_displays.add_data(filed_lists[i], "user")
				print(shell_displays.quit_option)
				print(shell_displays.cancel_option)
				cmd = input(shell_displays.cmd_user(perm))
				shell_choice.is_quit(cmd)
				shell_choice.is_cancel(userid, cmd)
				new_profile[filed_lists[i]] = cmd

	#End updating new user profile

	"""
	=====================
	Creating User Profile
	=====================
	At this stage all validations have passed!
	Query database to see if email is available, if available save new user profile
	After creating display newly created user to confirm

	"""

	print("Creating new user as " + new_profile['name'])
	print(new_profile)







