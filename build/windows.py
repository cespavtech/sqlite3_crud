"""
============================================================
=====================Windows Module=========================

************************************************************

All the windows displayed to users are defined here

************************************************************

@param list_[win] = Window page (e.g list_two for second window)
Any feature to claa before displaying pages can be added here
Before the actual print function, add other function if necessary
Remember to import the module hosting your function before calling the it

After the user selects an item (student, module, rooms etc)
more options are loaded from module tab_choice.py in ./build folder
============================================================

"""
#Window one
def list():
	print('''
1 -> Staff
2 -> Students
3 -> Courses
4 -> Rooms
5 -> Modules
		''')
#Window two
def module_options(is_admin = 0):
	if is_admin:
		#Current user is admin, display all options
		print('''
		1 -> List All
		2 -> Search
		3 -> Create
		''')
	else:
		print('''
		1 -> List All
		2 -> Search
		''')
		
