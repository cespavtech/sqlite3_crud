"""
======================
New Module Creating
======================
This module is responsible for creating new course modules records
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

	#New module profile
	new_profile = {}
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'new')
	#Permission
	perm = user_permission.check_permission(userid)
	
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Create profile data for new module

	filed_lists = items.item_fields[cmd[1]]

	for i in cmd:
		#Loop through all currently selected arguments
		j = i.split()
		if len(j) > 1:
			#Thats an argument!
			raw_field = j[0]

			#Update new module profile
			if raw_field in filed_lists:
				key_value = i.replace(raw_field + " ", "")
				new_profile[filed_lists[raw_field]] = key_value

	#End updating new module pforile

	#Validation of new module profile completion

	for i in filed_lists:
		#Check wether its id
		if filed_lists[i] != 'id':
			#Not id, check wether it has been set for our new module
			if not filed_lists[i] in new_profile:
				#Not updated, force selection
				shell_displays.add_data(filed_lists[i], "module")
				print(shell_displays.quit_option)
				print(shell_displays.cancel_option)
				cmd = input(shell_displays.cmd_user(perm))
				shell_choice.is_quit(cmd)
				shell_choice.is_cancel(userid, cmd)
				new_profile[filed_lists[i]] = cmd

	#End updating new module profile

	"""
	=====================
	Creating Module Profile
	=====================
	At this stage all validations have passed!
	Query database to see if slug is available, if available save new module profile
	After creating display newly created module to confirm

	"""

	print("Creating new module as " + new_profile['name'])

	#Check name availability

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Check name availability!

	sql = '''SELECT id FROM modules WHERE name=?'''

	cur.execute(sql, [new_profile['name']])

	item_row = cur.fetchall()

	if len(item_row) > 0:
		#Name taken
		print(error_displays.no_name)
		return

	#Check slug availability!

	sql = '''SELECT id FROM modules WHERE slug=?'''

	cur.execute(sql, [new_profile['slug']])

	item_row = cur.fetchall()

	if len(item_row) > 0:
		#Slug taken
		print(error_displays.no_slug)
		return

	#All is well, create new item

	#Update module tutor with uiser id

	tutor_guess = new_profile['tutor']
	sql = '''SELECT id FROM users WHERE id=? and account =? OR email=? and account =?'''

	cur.execute(sql, [tutor_guess, 'staff', tutor_guess, 'staff'])

	tutor_row = cur.fetchall()

	if len(tutor_row) < 1:
		#No tutor found!
		print(error_displays.no_account)
		return
	#Update with id
	new_profile['tutor'] = tutor_row[0][0]

	#Update room with room id
	room_guess = new_profile['room']
	sql = '''SELECT id FROM rooms WHERE id=? OR slug=?'''

	cur.execute(sql, [room_guess, room_guess])

	room_row = cur.fetchall()

	if len(room_row) < 1:
		#No tutor found!
		print(error_displays.no_item)
		return
	#Update with id
	new_profile['room'] = room_row[0][0]

	#Update course with course id
	course_guess = new_profile['course']
	sql = '''SELECT id FROM courses WHERE id=? OR slug=?'''

	cur.execute(sql, [course_guess, course_guess])

	course_row = cur.fetchall()

	if len(course_row) < 1:
		#No tutor found!
		print(error_displays.no_item)
		return
	#Update with id
	new_profile['course'] = course_row[0][0]

	#Update week day with full name
	week_days = items.week_days
	if not new_profile['day'] in week_days:
		#User selected invalid day!
		print(error_displays.no_item)
		return

	#Update with full day name
	new_day = week_days[new_profile['day']]
	new_profile['day'] = new_day


	sql = '''INSERT INTO modules(name, slug, tutor, start, end, day, cat, room, course)
	VALUES(?,?,?,?,?,?,?,?,?)'''

	cur.execute(sql, [new_profile['name'], 
		new_profile['slug'], 
		new_profile['tutor'], 
		new_profile['start'],
		new_profile['end'],
		new_profile['day'],
		new_profile['cat'],
		new_profile['room'],
		new_profile['course']])

	conn.commit()

	#Inform created
	print("New module created with success")

	#Display newly created module data
	print(new_profile)







