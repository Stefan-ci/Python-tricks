import psutil

def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d"%(hours, minutes, seconds)

battery = psutil.sensors_battery()
percent = battery.percent
time = convertTime(battery.secsleft)

print('Battery percentage: ', percent)
print('Power plugged in: ', battery.power_plugged)
print("Battery left: ", time)
