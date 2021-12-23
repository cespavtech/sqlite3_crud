"""



"""

_items = {
	"-u" : "Users",
	"-c" : "Courses",
	"-m" : "Modules",
	"-r" : "Rooms",
	"-s" : "Sessions"
}


"""
====================
Main Window Comands
====================
If match found, the value is parsed to method at 
build.core.kernel.process._call(userid, comand, item, cmd)


"""

_windows = {
	"show" : "disp",
	"create" : "new",
	"update" : "alt",
	"delete" : "del",
	"assign" : "ass",
	"report" : "rep",
	"remove" : "rem"
}



"""
====================
Main Comand Choices
====================
This has database table corresponding to choices
The hyphen (-) is ignored as from this point
It is removed from the user comand line later

It is assumed to create a module for each tabel with the same name for every comand

for users table there must be module in build.comands.show.users
and build.comands.create.users e.t.c

"""

items = {
	"u" : "users",
	"c" : "courses",
	"m" : "modules",
	"r" : "rooms",
	"s" : "sessions"
}


"""
==============
Item Fields
==============
This corresponds with the table field in the database
for selected item (e.g. users table identified by -u keyword)

User modules table field is processed by the responsible module
not configurable here...
"""

item_fields = {
#User table fields
	"u" : {
		"ui" : "id",
		"un" : "name",
		"ua" : "account",
		"ue" : "email",
		"up" : "password"
	},
#Courses table fields
	"c" : {
		"ci" : "id",
		"cn" : "name",
		"cs" : "slug"
	},
#Modules table fields
	"m" : {
		"mi" : "id",
		"mn" : "name",
		"ms" : "slug",
		"mc" : "course"
	},
#Rooms table fields
	"r" : {
		"ri" : "id",
		"rn" : "name",
		"rs" : "slug"
	},
#Sessions tabel fields
	"s" : {
		"si" : "id",
		"st" : "tutor",
		"sb" : "start",
		"se" : "end",
		"sd" : "day",
		"sr" : "room",
		"sm" : "module",
		"sc" : "cat",
		"ss" : "slug"
	}
}


"""
==============
Week Days
==============
These are used to convert user comands to full week day name
If the user choice for module day is not found here,
Item not found error is rendered and the process is halted

"""

week_days = {
	"mon" : "Monday",
	"tue" : "Tuesday",
	"wed" : "Wednusday",
	"thu" : "Thursday",
	"fri" : "Friday"
}


"""
====================
Event Categories
====================
We will use this to display the event category for sessions


"""

event_category = {
	"1" : "On Campus Workshop",
	"2" : "Off Campus Workshop"
}