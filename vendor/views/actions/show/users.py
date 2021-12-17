"""
======================
User Profile View
======================

When showing user profile data,
we will use this view to render the profile data

@param user_data{} => user profile data
"""

#We will use this to display user profile data
from configs.display import user_data

def rendor(user_data, user_modules = {}):
	#Display user profile
	print("-" * 50)
	guess_name(user_data['account'], user_data['name'])

	#Print all user modules
	guess_modules(user_modules)

	#Last line to indicate user profile display end!
	print("-" * 50)



"""
This method is for displaying user name
We will guess the user type and display appropriate account title
"""

def guess_name(account, name):
	#Check account type
	account_title = "Uknown"
	name_titles = user_data.user_name

	#Check wether defined
	if account in name_titles:
		#Found!
		account_title = name_titles[account]

	#Rendor name view
	print(account_title + """:				""" + str(name))


"""
This method is for displaying user modules
We will guess the user account type to display the data in appropriate way

"""

def guess_modules(user_modules):
	#Print modules list if any!
	if len(user_modules) < 1:
		#No modules!
		print("No Modules found for this user....")
		return

	#Load modules data...
