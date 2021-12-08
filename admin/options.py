
import build.messages as messages
import admin.options as admin_options
import build.shell_inputs as options
import build.windows as _win
def loop(cmd, tab = 0):
	if tab == 0:
		index_list = options.guess_list(tab)
	else:
		index_list = options.choice_list()
	username = cmd[2]
	auth = cmd[1]
	cmd_raw = str(cmd[0])
	if options.is_quit(cmd_raw):
		options.quit_ok()
		exit()
	cmd_index = "opt_" + cmd_raw
	if cmd_index in index_list:
		cmd_name = index_list[cmd_index]
		messages.select_option(username)
		print(messages.intro_user)
		print("[ " + cmd_name + "~]: Select")
		options.guess_window(tab, username)
		admin_options.loop([input(messages.cmd_prompt), auth, username], tab)
	else:
		messages.invalid_comand(cmd_raw)
		messages.select_option(username)
		print(messages.intro_user_more)
		options.guess_window(tab, username)
		admin_options.loop([input(messages.cmd_prompt), auth, username], tab)