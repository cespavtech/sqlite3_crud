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
		print("Login with your account username")
	else:
		print("Enter your password to proceed")