"""
======================
Module View
======================

When showing module data,
we will use this view to render the data

@param module_data{} => module data
"""

#Error displays
from vendor.views.core import error_prompt as error_displays

#Modules configs
from configs import modules as module_configs


"""

"""

def rendor(module_data):

	#Display module name
	if module_data[0] == "name":
		print("""Module:				   """ + module_data[1])
		return


	#Display module category
	if module_data[0] == "category":
		category = module_data[1]
		module_category = module_configs.categories
		if category in module_category:
			category = module_category[category]
		print("""Event Category:				   """ + category)
		return

	#Display module name
	if module_data[0] == "slug":
		print("""Slug:				   """ + module_data[1])
		return

	#Display module profile name
	if module_data[0] == "profile_name":
		print("*" * 50)
		print("""Module:				   """ + module_data[1])
		print("*" * 50)
		return

	#Display module profile name
	if module_data[0] == "profile_name":
		print("*" * 50)
		print("""Module:				   """ + module_data[1])
		print("*" * 50)
		return