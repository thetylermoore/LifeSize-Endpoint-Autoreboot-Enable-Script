import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#paramiko black magic

codec_list = [
	['1.1.1.1', 'Mock Store'],
	['1.1.1.2', 'Center Circle Conference Room'],
	['1.1.1.3', 'DC Footwear M&D'],
	['1.1.1.4', 'DC Great Wall'],
	['1.1.1.5', 'Exec Conf Room'],
	['1.1.1.6', 'Healy Office'],
	['1.1.1.7', 'IT Operations Room'],
	['1.1.1.8', 'IT War Room'],
	['1.1.1.9', 'Legal Tax Meeting Room'],
	['1.1.1.9', 'Mock Store'],
	['1.1.1.10', 'OT Office'],
	['1.1.1.11', 'QS Footwear M&D'],
	['1.1.1.12', 'QS M&D Pit'],
	['1.1.1.13', 'Roxy War Room'],
	['1.1.1.14', 'Center Circle Visitor Office'],
	]
#add additional locations in the same format

for row in codec_list:

	try:
		ssh.connect(row[0], username='auto', password='lifesize')
	#default password for express 220 and team 220 units, make sure SSH is enabled on units from GUI
	except paramiko.SSHException:
		print ("Connection Failed")
		quit()

	stdin,stdout,stderr = ssh.exec_command("set system autoreboot on")
	#this command will enable autoreboot for the unit at 4am if asleep
	
	for line in stdout.readlines():
		print row[1] + " autoreboot status " + line.strip()
		#cofirmation of autoreboot status

	stdin,stdout,stderr = ssh.exec_command("get system date")
	#this command will verify system time, important because of the 4am time above

	for line in stdout.readlines():
		print row[1] + " date verification " + line.strip()

	ssh.close()
