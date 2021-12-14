"""
*****************************************************

********************USER PERMISSIONS MODULE*********************

@param userid > Current user ID in users table

"""
from build.users.profile import profile as user_profile




"""

"""
def allowed(perm):
	#Check wether current user can perform this action
	perm_list = prevs

	#Check wether current user role is present
	if perm in perm_list:
		#Found!
		current_perm = perm_list[perm]
		if current_perm['disp']['all'] == 1:
			return 1




"""
#New user permission check
@param admin 
@param student
@param staff
"""
def check_permission(userid):
	admin = "admin"
	student = "student"
	staff = "staff"

	#Return new permission
	return admin


"""
=======================
User Permissions List
=======================
We configure what actions we would allow users to perform
based on their account type

Each comand covers the all items
If a user can use the comand disp/show they can access all
If the all attribute is set to true/1, the rest will be ignored
if set to False/0 each item will be accessed to see if the user can perform the selected action

To allow a user to perform a certain action on items, simply add the items in the list after all
Make sure to set all to False/0 to allow specific item actions only!
"""

prevs = {
#For admins
	"admin" : {
	#Which data can the admin display
		"disp" : {
			"all" : 1
		},
	#Data to allow admin create
		"new" : {
			"all" : 1
		},
	#Data to allow admin modify
		"alt" : {
			"all" : 1
		},
	#Data to allow admin delete
		"del" : {
			"all" : 1
		}
	},

#For staffs
	"staff" : {
	#Which data allow staffs to display
		"disp" : {
			"all" : 1
		},
	#Data to allow staffs create
		"new" : {
			"all" : 0
		},
	#Data to allow staffs modify
		"alt" : {
			"all" : 0
		},
	#Data to allow staffs delete
		"del" : {
			"all" : 0
		}
	},

#For students
	"student" : {
	#Which data allow students to display
		"disp" : {
			"all" : 0,
			"self" : {
				"c" : 1,
				"m" : 1
			}
		},
	#Data to allow students create
		"new" : {
			"all" : 0
		},
	#Data to allow students modify
		"alt" : {
			"all" : 0
		},
	#Data to allow students delete
		"del" : {
			"all" : 0
		}
	}

}

