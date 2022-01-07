"""
*****************************************************

********************KERNEL MODULE********************

@param userid > Current user id from users table
"""

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#User Permissions
from build.users.security import permissions as user_permission

#Shell clobal options [e.g. q/Q for quit]
from build.core import shell_options as shell_choice

#Window comands
from build.core.inputs import items as user_comands

#Process comands
from build.core.kernel import process as process_cmd


"""
NEW COMAND
Every new comand will pass through this
@param cmd > New user comand

"""
def new_comand(userid, cmd):

	#Check wether is quit!
	shell_choice.is_quit(cmd)

	#Check wether is help/guide
	shell_choice.user_help(userid, cmd)

	#Permission
	perm = user_permission.check_permission(userid)

	#Check wether empty!
	if cmd == "":
		#Empty!
		shell_displays.invalid_comand("[~ empty ~]")
		print(shell_displays.quit_option)
		cmd = input(shell_displays.cmd_user(perm))
		new_comand(userid, cmd)

	

	#Parse selected action

	user_cmd = cmd.split()
	comand_list = user_comands._windows
	new_cmd = user_cmd[0]

	#Check if comand valid!
	if new_cmd in comand_list:
		#Comand found!
		#Parse data
		process_cmd.boot(userid, comand_list[new_cmd], cmd)
	else:
		shell_displays.invalid_comand(new_cmd)

	print(shell_displays.quit_option)
	cmd = input(shell_displays.cmd_user(perm))
	new_comand(userid, cmd)
