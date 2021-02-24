import sys, datetime, subprocess
	
print("System started!")

sys_max_hour = 1 #set maximum hours
sys_start_time = datetime.datetime.now()
delta = datetime.timedelta(hours = sys_max_hour)
sys_shutdown_time = sys_start_time + delta

def shutdown():
	subprocess.call(["shutdown", "/s", "/f", "/t", "120", 
	"/c", "Còn 2 phút trước khi tắt máy. Sao lưu dữ liệu!"])
	sys.exit()

while True:
	cur_time = datetime.datetime.now()
	if(cur_time >= sys_shutdown_time):
		shutdown()
