"""



"""

_items = {
	"-u" : "Users",
	"-c" : "Courses",
	"-m" : "Modules",
	"-r" : "Rooms"
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
	"delete" : "del"
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
	"r" : "rooms"
}


"""
==============
Item Fields
==============
This corresponds with the table field in the database
for selected item (e.g. users table identified by -u keyword)

"""

item_fields = {
#User table fields
	"u" : {
		"ui" : "id",
		"ue" : "email",
		"un" : "name",
		"ua" : "account"
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
		"mc" : "course",
		"mr" : "room",
		"ec" : "category"
	},
#Rooms table fields
	"r" : {
		"ri" : "id",
		"rn" : "name",
		"rs" : "slug"
	}
}

