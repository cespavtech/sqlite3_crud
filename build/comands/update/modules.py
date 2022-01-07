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
	allow = module_permission.allowed(module_permission.check_permission(moduleid))

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







