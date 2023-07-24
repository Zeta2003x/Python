def make_readable(seconds): #Human Readable Time
	time = []
	hours = str(int(seconds/3600))
	if len(hours) == 1:
		hours = f"0{hours}"
	time.append(hours)
	minutes = str(int((seconds%3600)/60))
	if len(minutes) == 1:
		minutes = f"0{minutes}"
	time.append(minutes)
	seconds = str(int((seconds%3600)%60))
	if len(seconds) == 1:
		seconds = f"0{seconds}"
	time.append(seconds)
	return ":".join(time)

def format_duration(s): #Human Readable Duration Format
	time = []
	if s < 0: return "Past"
	if s == 0: return "now"
	years = s // 31536000
	if years == 1: time.append(str(years) + " year")
	elif years > 1: time.append(str(years) + " years")
	days = (s%31536000)//86400
	if days == 1: time.append(str(days) + " day")
	elif days > 1: time.append(str(days) + " days")
	hours = (s%86400)//3600
	if hours == 1: time.append(str(hours) + " hour")
	elif hours > 1: time.append(str(hours) + " hours")
	minutes = (s%3600)//60
	if minutes == 1: time.append(str(minutes) + " minute")
	elif minutes > 1: time.append(str(minutes) + " minutes")
	seconds = s%60
	if seconds == 1: time.append(str(seconds) + " second")
	elif seconds > 1: time.append(str(seconds) + " seconds")
	return ", ".join(time[:-1]) + f" and {time[-1]}" if len(time) > 1 else time[0]

print(format_duration(120001))