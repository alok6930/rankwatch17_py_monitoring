import os, psutil                   #import os and psutil
from time import time, sleep

start=time()
while True:
	disk_usage=[]		    #Create array for disk,cpu and ram usage
	my_cpu_usage=[]
	my_ram_usage=[]
	sleep(1)
	if int(time()-start)%5==0:
		disk=psutil.disk_usage('/').used
		cpu=psutil.cpu_percent()
		ram=psutil.virtual_memory().used
		#Displaying No. of cpu core,ram usage,disk usage,cpu usage
		print "CPU Core :", psutil.cpu_count(), "RAM Usage", ram, "Disk Usage", disk, "CPU Usage", cpu
		disk_usage.append(disk)
		my_cpu_usage.append(cpu)
		my_ram_usage.append(ram)
	if int(time()-start)%30==0 or int(time()-start)%60==0 or int(time()-start)%300==0:
		#Displaying Avg ram usage,disk usage,cpu usage after 30 sec,1 min, 5 min
		print "Average Disk :", sum(disk_usage)/len(disk_usage), "Average CPU :", sum(my_cpu_usage)/len(my_cpu_usage), "Average RAM :", sum(my_ram_usage)/len(my_ram_usage)
	
