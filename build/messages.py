"""=============================================================
===================Messages Module========================

**************************************************************

All messages displayed by the shell for users are defined here

**************************************************************
@param intro_login = Displayed all the time for guest users
@param intro_user = Displayed all the time for logged in users
@param intro_msg = Displayed at the shell start
================================================================
"""
intro_msg = '''Hello! To get started please login '''
intro_login = '''Enter q/Q to quit
Enter u/U to select another username
'''
intro_user = '''Enter q/Q to quit
'''

intro_user_more = '''Enter 0 to go back
Enter 00 for home window
'''
cmd_prompt = "[ CHOICE ]\n"
def login_message():
	print('Wrong username/password combinations! ')
def login_ok():
	print('You are now logged in! ')

def select_option(username):
	print("Select an option to continue")
	print("Logged in as " + username)
def select_choice():
	print("Select an option below;")
	if username != 0:
		print("Logged in as " + username)
def invalid_comand(cmd):
	print("*" * 30)
	print("INVALID COMAND [=> " + cmd + " <=]\n")
	print("*" * 30)