"""


"""

all_docs = {
#Show comands
"show": """
*****************
 [~ show ~]
*****************

 Use this comand to display list of data

 [~ USAGE ~]
 show [item] [-key] [value]


 """,
#Create comand

"create": """
****************
 [~ create ~]
****************

 Use this comand to create a new data

 [~ USAGE ~]
 create [item] [-key] [value]

""",

#Update comand

"update": """
*****************
 [~ update ~]
*****************

 Use this comand to update data

 [~ USAGE ~]
 update [item] [-key] [value]

 *****
 NOTE:
 *****
 The first argument will be used to refer to the item

 [e.g.]
 update -u -ue example@mail.domain -un John Doe
 This will update data for user with email example@mail.domain

 """,
#Delete comand

 "delete": """
****************
 [~ delete ~]
****************

 Use this comand to delete data

 [~ USAGE ~]
 delete [item] [-key] [value]

 *****
 NOTE:
 *****
 The comand accepts only one argument

 [e.g.]
 delete -u -ui 2

 Will delete user with id 3

"""

 }


"""
======================
Items Documentations
======================
This is used to display documentations for each choice available under a comand

 """

item_docs = {
#User item
"-u" : """
****************
 [~ -u ~]
****************

 This item referes to users

 [~ USAGE ~]
 [comand] [-u] [-key] [value]

 ******
 NOTE:
 ******
 When creating new user accounts, use below options as account type;
 staff for staffs
 students for students
 admin for admins accounts

 [e.g.]
 delete -u -ui 2

 Will delete user with id 3
""",

#Course item
"-c" : """
****************
 [~ -c ~]
****************

 This item referes to courses

 [~ USAGE ~]
 [comand] [-c] [-key] [value]


 [e.g.]
 delete -c -ci 2

 Will delete course with id 3
 and also delete all modules under the course!
"""

 }


