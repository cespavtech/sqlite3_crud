"""
===================
Sessions Views
===================


"""

#Item table fields

from build.core.inputs import items

def rendor(session_data):
	#Display session profile

	#Print session week day
	if session_data[0] == "day":
		print("""Day:			            """ + str(items.week_days[session_data[1]]))
		return

	#Print session start time
	if session_data[0] == "start_time":
		print("""Start Time:			            """ + str(session_data[1]))
		return

	#Print session end time
	if session_data[0] == "end_time":
		print("""End Time:			            """ + str(session_data[1]))
		return


	#Print session duration
	if session_data[0] == "duration":
		start = int(session_data[1][0]) + int(session_data[1][1])
		end = int(session_data[2][0]) + int(session_data[2][1])

		#Convert them to 24 hour clock if neccessary
		if end <= 12:
			end = end + 12

		if start <= 12:
			start = start + 12
		duration = (end - start)
		print("""Duration:			            """ + str(duration) + " hour(s)")
		return


	#Print session room
	if session_data[0] == "room":
		print("""Room:			            """ + str(session_data[1]))
		return

	#Print session tutor
	if session_data[0] == "tutor":
		print("""Tutor:			            """ + str(session_data[1]))
		return
		

