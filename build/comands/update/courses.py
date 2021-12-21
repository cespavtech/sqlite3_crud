"""
======================
Course Data Updating
======================
This module is responsible for updating course data
If current module has no preveleges, nothing is processed

"""

#Database
import config

#Permissions
from build.users.security import permissions as module_permission

#Module table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays


"""

"""
def boot(moduleid, cmd):
	#Permissions
	allow = module_permission.allowed(module_permission.check_permission(moduleid), 'alt')

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

	#Check scope to search course with

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
	Update Course Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search course with
	Retrieve course from table using keyw as search using the selected field
	Update profile data and display newly updated course for confirmation

	"""

	print("Updating course using " + keyw + " as course " + field)

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

	#Item availability!

	sql = "SELECT id FROM courses WHERE " + field + "=?"

	cur.execute(sql, [keyw])

	item_rows = cur.fetchall()

	#Is course found!???
	if len(item_rows) < 1:
		print(error_displays.no_item)
		return

	#Check name availability!
	if 'name' in new_profile:
		#Name being updated

		sql = '''SELECT id FROM courses WHERE name=?'''

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
			sql = '''SELECT id FROM courses WHERE slug=?'''

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
				print("Updating course " + i + "...")
				sql = "UPDATE courses SET " + i + " = ? WHERE id =?"
				cur.execute(sql, [new_profile[i], item_id])
				conn.commit()
				#Updated!
				print("Course " + i + " updated....")

	print("New course profile updated with success")







