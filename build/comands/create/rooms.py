"""
======================
New Room Creating
======================
This room is responsible for creating new room records
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

	#New room profile
	new_profile = {}
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'new')
	#Permission
	perm = user_permission.check_permission(userid)
	
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Create profile data for new room

	filed_lists = items.item_fields[cmd[1]]

	for i in cmd:
		#Loop through all currently selected arguments
		j = i.split()
		if len(j) > 1:
			#Thats an argument!
			raw_field = j[0]

			#Update new room profile
			if raw_field in filed_lists:
				key_value = i.replace(raw_field + " ", "")
				new_profile[filed_lists[raw_field]] = key_value

	#End updating new room pforile

	#Validation of new room profile completion

	for i in filed_lists:
		#Check wether its id
		if filed_lists[i] != 'id':
			#Not id, check wether it has been set for our new room
			if not filed_lists[i] in new_profile:
				#Not updated, force selection
				shell_displays.add_data(filed_lists[i], "room")
				print(shell_displays.quit_option)
				print(shell_displays.cancel_option)
				cmd = input(shell_displays.cmd_user(perm))
				shell_choice.is_quit(cmd)
				shell_choice.is_cancel(userid, cmd)
				new_profile[filed_lists[i]] = cmd

	#End updating new room profile

	"""
	=====================
	Creating room Profile
	=====================
	At this stage all validations have passed!
	Query database to see if slug is available, if available save new room profile
	After creating display newly created room to confirm

	"""

	print("Creating new room as " + new_profile['name'])
	
	#Check name availability

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Check name availability!

	sql = '''SELECT id FROM rooms WHERE name=?'''

	cur.execute(sql, [new_profile['name']])

	item_row = cur.fetchall()

	if len(item_row) > 0:
		#Name taken
		print(error_displays.no_name)
		return

	#Check slug availability!

	sql = '''SELECT id FROM rooms WHERE slug=?'''

	cur.execute(sql, [new_profile['slug']])

	item_row = cur.fetchall()

	if len(item_row) > 0:
		#Slug taken
		print(error_displays.no_slug)
		return

	#All is well, create new item

	sql = '''INSERT INTO rooms(name, slug)
	VALUES(?,?)'''

	cur.execute(sql, [new_profile['name'], new_profile['slug']])

	conn.commit()

	#Inform created
	print("New room created with success")

	#Display newly created module data
	print(new_profile)







