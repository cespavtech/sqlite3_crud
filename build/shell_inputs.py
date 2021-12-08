"""


"""

import build.windows as _win
import build._auth as auth
import build.tab_choice as choices

def choice_list():
	array_data = {
  "opt_1": "Staff",
  "opt_2": "Students",
  "opt_3": "Courses",
  "opt_4": "Rooms",
  "opt_5": "Modules"
	}
	return array_data

def choice_options():
	array_data = {
  "opt_1": "Staff",
  "opt_2": "Students",
  "opt_3": "Courses",
  "opt_4": "Rooms",
  "opt_5": "Modules"
	}
	return array_data

def is_quit(cmd):
	if cmd in ('q', 'Q'):
		return 1
	return 0
def select_account(cmd):
	if cmd in ('u', 'U'):
		return 1
	return 0
def quit_ok():
	print("Quit successful!")
def login_form(usr):
	if usr:
		print("Login with your account username/email")
	else:
		print("Enter your password to proceed")


class choice_data():
	def name(choice):
		choice_index = "opt_" + choice
		index_list = shell_inputs.choice_list(choice_index)
		if choice_index in index_list:
			choice_name = index_list[choice_index]
		else:
			choice_name = "Unknown"
		print("Loading information for " + choice_name)
def guess_window(tab, username):
	if tab == 0: #Tab one!
		_win.list() #Refer to windows module in [./build] directory
	elif tab == 1:
		_win.module_options(username)

def guess_list(tab):
	array_data = {
  "opt_1": "Staff",
  "opt_2": "Students",
  "opt_3": "Courses",
  "opt_4": "Rooms",
  "opt_5": "Modules"
	}
	return array_data
