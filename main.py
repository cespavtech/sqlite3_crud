"""
************************** SQLITE CRUD **********************
****************** BLA BLA BLA *****************************
============================================================
Depends on the following packages
passlib (pip install passlib)
"""

intro_msg = '''Hello! To get started please login '''
intro_login = '''Enter q/Q to quit
Enter u/U to select another username
'''
#Database connections!
import sqlite3
con = sqlite3.connect('database/crud_sqlite.db')

#Import libs
#from passlib.hash import sha256_crypt .///// for password hashing
import build.messages as messages
import getpass  # for password prompt
import build.shell_inputs as shell_inputs
import admin.options as admin_options
import build._auth as auth


#Process user logins
def login_user(username, password):
	if shell_inputs.select_account(password):
		print("Please select user account")
		process_cmd(input('[ USERNAME ]\n'), 1)
		exit()
	if shell_inputs.is_quit(password):
		shell_inputs.quit_ok()
		exit()
	print("*" * 20)
	print("Logging you in as [ " + username + " ]")
	cur = con.cursor()
	cur.execute("SELECT * FROM users WHERE user_name=?", (username,))
	user_row = cur.fetchall()
	if len(user_row) < 1: # >0
	# auth.authenticate(username, password)
		messages.login_ok()
		messages.select_option()
		admin_options.list()
		input()
	else:
		messages.login_message()
		print(intro_login)
		shell_inputs.login_form(0)
		login_user(username, getpass.getpass())


#Process user cli comands

def process_cmd(cmd, auth):
	if shell_inputs.is_quit(cmd):
		shell_inputs.quit_ok()
		exit()
	if auth == 1:
		#Login request!
		shell_inputs.login_form(0)
		print(intro_login)
		login_user(cmd, getpass.getpass())
	else:
		print("Try again")





#Init load
print("*" * 15)
print(intro_msg)
print(intro_login)
shell_inputs.login_form(1)
process_cmd(input('[ USERNAME ]\n'), 1)