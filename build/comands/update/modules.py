"""
======================
Module Data Updating
======================
This module is responsible for updating module profile data
If current module has no preveleges, nothing is processed

"""

#Database
import config

#Permissions
from build.users.security import permissions as user_permission

#Module table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays


"""

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'alt')

	#Permission
	perm = user_permission.check_permission(userid)

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Validate comand arguments
	if len(cmd) < 4:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return 1
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Check scope to search module with

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
	Update Module Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search module with
	Retrieve module from table using keyw as search using the selected field
	Update profile data and display newly updated module for confirmation

	"""

	print("Updating module using " + keyw + " as module " + field)

	#New item profile
	new_profile = {}

	#Create profile data for current item

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

	#End updating new item profile

	#Update user with id
	if 'tutor' in new_profile:
		#Updating module tutor!
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

	#Update room with id
	if 'room' in new_profile:
		#Updating room 
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
	if 'course' in new_profile:
		#Updating course
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
	if 'day' in new_profile:
		#Updating day!
		week_days = items.week_days
		if not new_profile['day'] in week_days:
			#User selected invalid day!
			print(error_displays.no_item)
			return

		#Update with full day name
		new_day = week_days[new_profile['day']]
		new_profile['day'] = new_day

	#Item availability!

	sql = "SELECT id FROM modules WHERE " + field + "=?"

	cur.execute(sql, [keyw])

	item_rows = cur.fetchall()

	#Is module found!???
	if len(item_rows) < 1:
		print(error_displays.no_item)
		return

	#Check name availability!
	if 'name' in new_profile:
		#Name being updated

		sql = '''SELECT id FROM modules WHERE name=?'''

		cur.execute(sql, [new_profile['name']])

		item_row = cur.fetchall()

		if len(item_row) > 0:
			#Name taken
			print(error_displays.no_name)
			return

	#Check slug availability!
	if 'slug' in new_profile:
		#Slug being updated

		if field != 'slug':
			#Field not slug
			sql = '''SELECT id FROM modules WHERE slug=?'''

			cur.execute(sql, [new_profile['slug']])

			item_row = cur.fetchall()

			if len(item_row) > 0:
				#Slug taken
				print(error_displays.no_slug)
				return

	#All is well, update data
	item_id = item_rows[0][0]

	for i in new_profile:
		#Loop through arguments passed!
		if i != 'id':
			#Not id, update data
			if i != field:
				print("Updating module " + i + "...")
				sql = "UPDATE modules SET " + i + " = ? WHERE id =?"
				cur.execute(sql, [new_profile[i], item_id])
				conn.commit()
				#Updated!
				print("Module " + i + " updated....")

	print("New module profile updated with success")







