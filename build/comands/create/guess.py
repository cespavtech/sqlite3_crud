"""
=======================
Select Data to Create
=======================
We run tests to see if the selected item can be created!


"""

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Shell windows/items
from build.core.inputs import items as shell_windows



"""

"""
def start_guess(userid, cmd):
	item_list = shell_windows.items

	#Check wether comand found!
	active_item = cmd[1]
	if active_item in item_list:
		#Item found!
		module_name = str(item_list[active_item])
		new_module = __import__(module_name, globals(), locals(), [], 1)
		new_module.boot(userid, cmd)
	else:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return 1