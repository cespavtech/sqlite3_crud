"""
==========================
Boot Method for Comands
==========================
Use this function to call other methods
User selected choices will be parsed here for every comand
The value from build.core.inputs.items_windows will be present in @param choice

@param cmd => Raw comand line
@param choice => selected comand [show/create etc]
@param userid
"""

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Guess data to show
from build.comands.show import guess as show_data

#Guess data to create
from build.comands.create import guess as create_data

#Guess data to update
from build.comands.update import guess as update_data

#Guess data to delete
from build.comands.delete import guess as delete_data

#Guess data to assign
from build.comands.assign import guess as assign_data


"""


@param data_disp
"""

def boot(userid, choice, cmd):
	#Run check
	new_cmd = cmd.split(' -')

	#Validate comand arguments
	if len(new_cmd) < 2:
		#Invalid arguments
		shell_displays.invalid_args(new_cmd[0])
		return 1

	#Choice detect
	if choice == "disp":
		#Display data!
		show_data.start_guess(userid, new_cmd)
	elif choice == "new":
		#Create data!
		create_data.start_guess(userid, new_cmd)
	elif choice == "alt":
		#Update data!
		update_data.start_guess(userid, new_cmd)
	elif choice == "del":
		#Delete data
		delete_data.start_guess(userid, new_cmd)
	elif choice == "ass":
		#Assign data
		assign_data.start_guess(userid, new_cmd)
	else:
		shell_displays.invalid_comand(new_cmd)