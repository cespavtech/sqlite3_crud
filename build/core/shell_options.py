"""
*****************************************************

********************SHELL OPTIONS MODULE*********************



"""

#For quiting and starting new session process
from build.users.security import login as user_login

#Display quit success message
from vendor.views.core import shell_prompts as shell_displays

#User Permissions
from build.users.security import permissions as user_permission



#Process user comands
from build.core.kernel import kernel as user_comands

#Quit option [./ = q/Q]
def is_quit(cmd):
	#Check wether user entered q/Q
	if cmd in ('q', 'Q'):
		print(shell_displays.quit_success)
		exit()


#Cancel option [./ = 0/00]
def is_cancel(userid, cmd):
	#Check wether user entered 0/00
	if cmd in ('0', '00'):
		print(shell_displays.cancel_success) #Display cancel success message
		perm = user_permission.check_permission(userid) #Permission
		print(shell_displays.quit_option) #Quit option display
		cmd = input(shell_displays.cmd_user(perm)) #Input comand
		user_comands.new_comand(userid, cmd) #Process new comand
		exit()


"""
Help option [./ -h]
This is for guest users
once, logged in the function used is user_help

"""
def is_help(cmd):
	#Check wether user entered q/Q
	if '-h' in cmd:
		print(shell_displays.help_option)
		exit()

#Help option [./ -h]
def user_help(userid, cmd):
	#Check wether user entered q/Q
	if '-h' in cmd:
		print(shell_displays.help_option)

		#Process comands futher
		cmd_v2 = cmd.split()

		#Permission
		perm = user_permission.check_permission(userid)

		if len(cmd_v2) >1:
			#Has extra options
			if len(cmd_v2) < 3:
				#Valid!
				#Import docs list
				from vendor.views.docs import docs

				#Import choices list
				from vendor.views.docs import choices as shell_choices

				#General comand docs
				j = docs.all_docs

				#Shell choices for each comand
				_j = shell_choices._choices

				#Shell Items docs
				__j = docs.item_docs

				keyw = cmd_v2[1]
				if keyw in j:
					#Keyword found!
					print(j[keyw])
					#Check if cmand has choices
					if keyw in _j:
						shell_displays._choices(keyw)

				elif keyw in __j:
					#Documentation for items
					print(__j[keyw])
					#Display item choices
					if keyw in _j:
						shell_displays._choices(keyw)
				
				#End printing docs
				else:
					#Docs not found!
					print("No documentation found for " + str(keyw) + "\n")

				#Process new user input	
				print(shell_displays.quit_option)
				cmd = input(shell_displays.cmd_user(perm))
				#Check comand
				user_comands.new_comand(userid, cmd)

			else:
				print("Invalid choice")
				print(shell_displays.quit_option)
				cmd = input(shell_displays.cmd_user(perm))
				#Check comand
				user_comands.new_comand(userid, cmd)

		else:

			#General help

			"""


			"""
			print(shell_displays._syntax) #Comand syntax

			shell_displays._items() #Print all available items

			print(shell_displays._keys) #Comand [-keys]

			from vendor.views.docs import docs
			j = docs.all_docs
			print("[~ COMANDS ~]")
			print("#" * 25)
			for i in j:
				print(j[i])
			print(shell_displays.quit_option)
			cmd = input(shell_displays.cmd_user(perm))
			#Check comand
			user_comands.new_comand(userid, cmd)

		#Quit processing further
		exit()
