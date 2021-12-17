"""
*****************************************************

********************LOGIN MODULE*********************

"""

#Database configs
import config

#Login display messages
from vendor.views.login import login_prompt as login_displays

#Shell error messages
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Homa Page header after user login successfully
from vendor.views.headers import tabs as tab_headers

#Shell clobal options [e.g. q/Q for quit]
from build.core import shell_options as shell_choice

#Process user comands
from build.core.kernel import kernel as user_comands

#Get user id to process comands
from build.users.profile import profile as user_profile

#User Permissions
from build.users.security import permissions as user_permission

#Password handling
from passlib.hash import bcrypt
import getpass  # for password prompt

def new_login():

	"""


	"""

	#Start new session
	print(shell_displays.quit_option)
	print (login_displays.request_username)
	username = input()

	#Check wether is quit!
	shell_choice.is_quit(username)

	print(shell_displays.quit_option)
	print(login_displays.request_password)
	password = getpass.getpass()

	#Check wether is quit!
	shell_choice.is_quit(password)

	login_status = proces_login(username, password)
	if login_status == "acct":
		#Wrong username/password
		print(error_displays.wrong_login_combination)
		new_login()
	elif login_status == "den":
		#Account login denied!
		print(error_displays.login_denied)
		new_login()
	elif login_status == True:

		print(tab_headers.welcome_user) #welcome_user is homepage tab header!


		#Get user id and start processinf comands
		userid = user_profile.user_id(username)

		#User previleges
		perm = user_permission.check_permission(userid)

		#Process comands

		cmd = input(shell_displays.cmd_user(perm))

		#Check comand
		user_comands.new_comand(userid, cmd)



def proces_login(username, password):
	"""


	"""

	#Set password hasher
	hasher = bcrypt.using(rounds=13)  # Make it slower

	#Start processing login
	print("Processing login...")

	combination = "acct"

	denied = "den"

	success = True

	#Check wether user found 
	"""SQL"""

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Check user availability!

	sql = "SELECT password FROM users WHERE email=?"

	cur.execute(sql, [username])

	user_row = cur.fetchall()

	#Check wether any account found!

	if len(user_row) < 1:
		#No account found!
		return combination

	#Run password verification
	hashed_password = user_row[0][0]
	login_success = hasher.verify(password, hashed_password)

	if login_success:
		#Passwords matched!
		return success

	#Passwords did not match!
	return combination

