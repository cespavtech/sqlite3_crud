"""

"""

prompt = {
	"user" : {
		"name" : "Enter User Names",
		"email" : "Enter User Email address",
		"password" : "Enter User Password",
		"account" : "Select Account type  [ -h -u for help ]"
	},

	"course" : {
		"name" : "Enter Course Name",
		"slug" : "Enter Course Slug"
	},

	"module" : {
		"name" : "Enter Module Name",
		"slug" : "Enter Module Slug",
		"course" : "Enter Module Course [ course slug or id ]",
		"room" : "Enter Module Room [ room slug or id ]",
		"cat" : "Category [ -h -m for help ]",
		"tutor" : "Module Tutor [staff id or email]",
		"start" : "Module Start Time [e.g. 10:00]",
		"end" : "Module Finish Time [e.g. 12:00]",
		"day" : "Module Week Day [e.g. mon]"
	},

	"room" : {
		"name" : "Enter Room Name",
		"slug" : "Enter Room Slug"
	}
}