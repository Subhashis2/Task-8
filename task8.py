from os import system
import random
import string
import getpass
from time import sleep
import webbrowser
import subprocess as sp

def clear():
	system("clear") #you can directly change it here...'cls' for windows and 'clear' for linux

def run(cmd):
	clear()
	system("tput setaf 2")
	system(cmd)
	system("tput setaf 7")
	sleep(3)
	clear()

def title():
	system("tput bold")
	system("tput setaf 1")
	print("""
				__   __        __     ___  ______ _________ __ __      _____
				| |  \\ \\      / /    / _ \\ | --- ||__   __|| | | |    |  _  |
				| |   \\ \\    / / __ | /_\\ || ____|   | |   | |_| | __ | |_| |
				| |___ \\ \\/\\/ / |__|| |_| || |\\ \\    | |   |  _  ||__||  _  |
				|_____| \\_/\\_/      |_| |_||_| \\_\\   |_|   |_| |_|    | |_| |
				                                                      |_____|
									_____ __ ____ _  _     __
									  |  /__\\|___ |__/ __ |__|
									  |  |  | ___||  \\    |__|""")
	system("tput setaf 7")

def menu():
	username = "Subha"
	password = "subha"
	captcha = ''
	Captcha = ''
	typeUsername = ''
	typePassword = ''
	typeCaptcha = ''
	clear()
	title()
	for i in range(2):
		if (i == 1):
			captcha = captcha + ' '
		numbers = random.randint(0,9)
		letters = random.choice(string.ascii_letters)
		captcha = captcha + letters + ' ' + str(numbers)
		Captcha = Captcha + letters + str(numbers)

	typeUsername = str(input("""
				||-----------------------------------||
				||                                   ||
				     USERNAME:  """))

	typePassword = str(getpass.getpass("""
				||                                   ||
				     PASSWORD:  """))
	print("""
				||                                   ||
				     CAPTCHA:    {0}             ||""".format(captcha))
	typeCaptcha = str(input("""
				||                                   ||
				     TYPE HERE:  """))
	print("""
				||                                   ||
				||-----------------------------------||""")
	if((typeCaptcha != Captcha) and (typeUsername != username) and (typePassword != password)):
		return 0
	else:
		return 1

def loading():
	lst_1 = list(range(20,30))
	lst_2 = list(range(80,85))
	lst_3 = list(filter(lambda x: x%5 == 0, range(1,101)))
	l = 0
	for i in range(1,101):
		clear()
		print("""\n\n\n
						Login Successfull !!!
						  Loading.....({0}%)\n""".format(i))
		j = int(i / 2)
		if(j in lst_3):
			for k in range(j):
				print(" _", end = '', flush = True)
			print()
			for k in range(j):
				print("|_", end = '', flush = True)	
			if(j in lst_1 or j in lst_2):
				sleep(1)
			else:
				sleep(0.1)
			l = j
		else:
			for k in range(l):
				print(" _", end = '', flush = True)
			print()
			for k in range(l):
				print("|_", end = '', flush = True)
			sleep(0.1)
		print("|")
	
	MainProgram()	#Calling main program here....

def IntroPagePrint(front):
	l = len(front)
	system("tput setaf 6")
	print("			__________________________________________________________________________",end = '\n', flush = False)
	print("			||-----------------------------------------------------------------------||",end = '\n', flush = False)
	for i in range(l):
		print("			||",end = '',flush = True)
		system("tput setaf 2")
		print("	{}.".format(i),end = '',flush = True)
		system("tput setaf 7")
		print("	Press (",end = '',flush = True)
		system("tput setaf 1")
		print("{}".format(i),end = '',flush = True)
		system("tput setaf 7")
		if(i < 10):
			print(")  to ",end = '',flush = True)
		else:
			print(") to ",end = '',flush = True)
		system("tput setaf 3")
		print("{}".format(front[i]),end = '',flush = True)
		system("tput setaf 6")
		print("||",end = '\n',flush = False)
	print("			||-----------------------------------------------------------------------||")
	print("			___________________________________________________________________________",end = '\n', flush = False)
	system("tput setaf 7")
	print("\n\n")


menuPrintList = ["run some linux basics commands             ","run some docker commands                   ","do some partitions                         ","communicate with AWS                       ","create a hadoop cluster easily             ","go to ansible                              ","exit                                       ","shutdown the OS                            "]

def MainProgram():
	clear()
	while True:
		clear()
		IntroPagePrint(menuPrintList)
		ch = int(input("Enter your choice: "))
		if(ch == 0):
			rhelCommands()
		elif(ch == 1):
			docker()
		elif(ch == 2):
			partition()
		elif(ch == 3):
			aws()
		elif(ch == 4):
			hadoop()
		elif(ch == 5):
			ansible()
		elif(ch == 6):
			exit()
		elif(ch == 7):
			system("init 0")		
		else:
			print("not supported")
			input("\npls continue...")	

def ansible():
	clear()
	ansibleCmdList = ["",["echo '[dvd1]' >> /root/yum.repo","echo 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/' >> /root/yum.repo","echo 'gpgcheck=0' >> /root/yum.repo","echo '' >> /root/yum.repo","echo '[dvd2]' >> /root/yum.repo","echo 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS/' >> /root/yum.repo","echo 'gpgcheck=0' >> /root/yum.repo","cp /root/yum.repo /etc/yum.repos.d/ ","yum repolist"],"dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm","yum install sshpass","pip3 install ansible","","ansible --version",["mkdir /etc/ansible","echo '[defaults]' >> /etc/ansible/ansible.cfg","echo 'inventory=/root/ip.txt' >> /etc/ansible/ansible.cfg"],"ansible all --list-hosts","ansible all -m package -a 'name=httpd state=present'","ansible all -m copy -a 'src=web.html dest=/var/www/html'","ansible all -m service -a 'name=httpd state=started'"]

	while(True):
		system("tput setaf 3")
		print("""
		                                  |--->CONFIGURE YUM (PRESS 1):
		                                  |
		                                  |--->CONFIGURE EPEL (PRESS 2):
		                                  |
		           |-> INSTALL ANSIBLE--->|--->INSTALL SSHPASS (PRESS 3):
		           |                      |
		ANSIBLE--->|                      |--->INSTALL ANSIBLE (PRESS 4):
		           |                      |
		           |                      |--->INSTALL ANSIBLE DIRECTLY (PRESS 5):
		           |
		           |-> CHEAK ANSIBLE VERSION (PRESS 6):
		           |
		           |-> CREATE INVENTORY (PRESS 7):
		           |
		           |-> CHECK THE LIST OF HOSTS IN INVENTORY (PRESS 8):
		           |
		           |                        |--->INSTALL SOFTWARE[HTTPD] (PRESS 9):
		           |                        |
		           |-> CONFIGURE APACHE --->|--->COPY A HTML TO
		                  WEB SERVER        |    /var/www/html DIRECTORY (PRESS 10): 
		                      |             |
		                      |             |--->EXECUTE HTTPD SERVICE (PRESS 11):
		                      |             |
		                      |             |--->DIRECTLY CONFIGURE APACHE
		                      |                             WEB SERVER  (PRESS 12):
		                      |
		                      |--->CHECK HTTPD STATUS MANUALLY(PRESS 13):
		                      |
		                      |--->OPEN THE HTML PAGE IN BROWSER (PRESS 14):
		                      |
		                      |--->GO TO MAIN MENU (PRESS 15)\n\n""")
		system("tput setaf 7")

		choice = int(input("Enter your choice:   "))
		choiceManualList = [1,5,7,12,13,14] 
		if(choice in choiceManualList):
			if(choice == 1):
				for i in range(9):
					system(ansibleCmdList[1][i])
			elif(choice == 5):
				for i in range(9):
					system(ansibleCmdList[1][i])
				for i in range(2,5):
					system(ansibleCmdList[i])
			elif(choice == 7):
				count = int(input("How many hosts you want to enter:  "))
				for i in range(count):
					ip = input("Enter the target ip:  ")
					usr = input("Enter the username:  ")
					passwd = getpass.getpass("Enter the password:  ")
					system("echo '{0} ansible_user={1} ansible_ssh_pass={2} ansible_connection=ssh' >> /root/ip.txt".format(ip,usr,passwd))
				for i in range(3):
					system(ansibleCmdList[7][i])
			elif(choice == 12):
				for i in range(9,12):
					system(ansibleCmdList[i])
			elif(choice == 13):
				iP = input("Enter the ip to check httpd status:  ")
				system("ssh root@{0} systemctl status httpd".format(iP))
			elif(choice == 14):
				iP = input("Enter the ip to open the web page in browser:  ")
				webbrowser.open("https://{}/web.html".format(iP))
			else:
				print("			Program Error !!!")
				sleep(3)
				exit()
			sleep(5)
		elif(choice == 15):
			MainProgram()
		else:
			system(ansibleCmdList[choice])
			sleep(5)

	sleep(10)

linuxCommandList = ["cat /proc/version","whoami","date","cal","free -m","df -h","echo ","ls -lh","date +%r","man ","espeak-ng ","rpm -q ","which ","rpm -i ","rpm -e ","jobs","fg","ifconfig","ifconfig ","nslookup ","ping -c 10 ",["systemctl start firewalld","systemctl stop firewalld","systemctl enable firewalld","systemctl disable firewalld"],"lscpu","uptime","echo 3 > /proc/sys/vm/drop_caches","pgrep ","fdisk -l",["echo '[dvd1]' >> /root/yum.repo","echo 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/' >> /root/yum.repo","echo 'gpgcheck=0' >> /root/yum.repo","echo '' >> /root/yum.repo","echo '[dvd2]' >> /root/yum.repo","echo 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS/' >> /root/yum.repo","echo 'gpgcheck=0' >> /root/yum.repo","cp /root/yum.repo /etc/yum.repos.d/ ","yum repolist"],"ps -aux","netstat -tnlp","top"]

introPagePrintList = ["check your OS version details              ","check who am I?                            ","check date                                 ","check cal                                  ","check RAM                                  ","check hardisk details                      ","print any text on the console              ","check current directory details            ","show only time                             ","check any manual of any command            ","speak any text by system                   ","check software details by 'rpm' command    ","check the location of the command          ","install any package                        ","uninstall any package                      ","check running processes                    ","check foreground running processes         ","show your ip                               ","show your ip of enp0s3 N/W card            ","check any website's ip                     ","ping someone                               ","start/stop/enable/disable your firewall    ","check how much CPU you have                ","see last boot details                      ","clear cache of your RAM                    ","check process id of any software           ","check partition details                    ","configure 'yum'                            ","show all running processes and their PID   ","check running port details                 ","check all running processes using 'top' cmd"]

def rhelCommands():
	while True:
		clear()
		IntroPagePrint(introPagePrintList)
		oddCommandList = [6,9,10,11,12,13,14,18,19,20,21,25,27]
		choice = int(input("		Enter your choice: "))
		if(choice in oddCommandList):
			if(choice == 6):
				inpt = input("Enter your text to print on console: ")
				cmd = "{0}{1}".format(linuxCommandList[6],inpt)		
				run(cmd)			
			elif(choice == 9):
				inpt = input("Enter the command to check manual: ")
				cmd = "{0}{1}".format(linuxCommandList[9],inpt)		
				run(cmd)
			elif(choice == 10):
				inpt = input("Enter your text to speak by system: ")
				cmd = "{0}'{1}'".format(linuxCommandList[10],inpt)		
				run(cmd)
			elif(choice == 11):
				inpt = input("Enter the software name to check details: ")
				cmd = "{0}{1}".format(linuxCommandList[11],inpt)		
				run(cmd)
			elif(choice == 12):
				inpt = input("Enter the command name to check location: ")
				cmd = "{0}{1}".format(linuxCommandList[12],inpt)		
				run(cmd)
			elif(choice == 13):
				inpt = input("Enter the package name to install: ")
				cmd = "{0}{1}".format(linuxCommandList[13],inpt)		
				run(cmd)
			elif(choice == 14):
				inpt = input("Enter the package name to uninstall: ")
				cmd = "{0}{1}".format(linuxCommandList[14],inpt)		
				run(cmd)
			elif(choice == 18):
				inpt = input("Enter your Network card name: ")
				cmd = "{0}{1}".format(linuxCommandList[18],inpt)		
				run(cmd)
			elif(choice == 19):
				inpt = input("Enter the website: ")
				cmd = "{0}{1}".format(linuxCommandList[19],inpt)		
				run(cmd)
			elif(choice == 20):
				inpt = input("Enter target ip to ping: ")
				cmd = "{0}{1}".format(linuxCommandList[20],inpt)		
				run(cmd)
			elif(choice == 21):
				print("""
					0. Press (0) to start firewall
					1. Press (1) to stop firewall
					2. Press (2) to enable firewall
					3. Press (3) to disable firewall""")
				inpt = int(input("Enter your choice: "))
				cmd = "{0}".format(linuxCommandList[21][inpt])		
				run(cmd)
			elif(choice == 25):
				inpt = input("Enter the software name to check PID: ")
				cmd = "{0}{1}".format(linuxCommandList[25],inpt)		
				run(cmd)
			elif(choice == 27):
				clear()
				check = system("ls /etc/yum.repos.d/yum.repo")
				if(check == 0):
					print("yum is already configured !!!\n")
				else:
					lengthOfList = len(linuxCommandList[27])
					for i in range(lengthOfList):
						system(linuxCommandList[27][i])
				sleep(3)
			else:
				print("			Wrong Choice !!!")
		else:
			if(choice == -1):
				MainProgram()
			else:
				run(linuxCommandList[choice])

dockerCommandList = [["echo '[docker]' >> /root/docker.repo","echo 'baseurl=https://download.docker.com/linux/centos/7/x86_64/stable' >> /root/docker.repo","echo 'gpgcheck=0' >> /root/docker.repo","cp /root/docker.repo /etc/yum.repos.d/"],"yum install docker-ce --nobest",["systemctl start docker","systemctl stop docker","systemctl enable docker","systemctl disable docker"],"docker info","docker images","docker ps -a","docker pull ","docker run -it --name ",["docker start ","docker stop "],"docker stop `docker ps -a -q`","docker rm `docker ps -a -q`","docker attach ","docker rm ","docker rmi ",[["docker exec "," yum install net-tools"],["docker exec "," ifconfig"],["docker exec "," yum install httpd"],["docker exec "," systemctl status httpd"]],"docker logs "]

menuPageList = ["Create docker repo                         ","Install docker on the top of base OS       ","Start/Stop/Enable/Disable docker service   ","Check docker info                          ","Check docker images                        ","Show docker running history                ","Download docker images                     ","Launch new docker container                ","Start/Stop docker running container        ","Stop all running containers                ","Remove all running containers              ","Attach docker container                    ","Remove docker container                    ","Delete docker images                       ","Configure web server in docker container   ","see what exactly going on this OS          "]

def docker():
	while True:
		clear()
		IntroPagePrint(menuPageList)
		oddCommandList = [0,2,6,7,8,11,12,13,14,15]
		choice = int(input("		Enter your choice: "))
		if(choice in oddCommandList):
			if(choice == 0):
				clear()
				check = system("ls /etc/yum.repos.d/docker.repo")
				if(check == 0):
					system("tput setaf 1")
					print("\ndocker repo is already configured !!!\n")
				else:
					system("tput setaf 2")
					lengthOfList = len(dockerCommandList[0])
					for i in range(lengthOfList):
						system(dockerCommandList[0][i])
				system("tput setaf 7")
				sleep(3)
			elif(choice == 2):
				print("""
					0. Press (0) to start docker service
					1. Press (1) to stop docker service
					2. Press (2) to enable service
					3. Press (3) to disable service""")
				inpt = int(input("Enter your choice: "))
				cmd = "{0}".format(dockerCommandList[2][inpt])		
				run(cmd)
			elif(choice == 6):
				img = input("Enter the image name: ")
				ver = input("Enter the version: ")
				cmd = "{0}{1}:{2}".format(dockerCommandList[6],img,ver)		
				run(cmd)
			elif(choice == 7):
				img = input("Enter the image name: ")
				ver = input("Enter the version: ")
				osTagName = input("Enter the OS-tag name: ")
				cmd = "{0}{1} {2}:{3}".format(dockerCommandList[7],osTagName,img,ver)		
				run(cmd)
			elif(choice == 8):
				print("""
					0. Press (0) to start docker container
					1. Press (1) to stop docker container""")
				inpt = int(input("Enter your choice: "))
				osTagName = input("Enter the OS-tag name: ")
				cmd = "{0}{1}".format(dockerCommandList[8][inpt],osTagName)
				run(cmd)
			elif(choice == 11):
				osTagName = input("Enter the OS-tag name to attach: ")
				cmd = "{0}{1}".format(dockerCommandList[11],osTagName)
				run(cmd)
			elif(choice == 12):
				osTagName = input("Enter the OS-tag name to remove: ")
				cmd = "{0}{1}".format(dockerCommandList[12],osTagName)
				run(cmd)
			elif(choice == 13):
				img = input("Enter the Image name to delete: ")
				cmd = "{0}{1} --force".format(dockerCommandList[13],img)
				run(cmd)
			elif(choice == 14):
				osTagName = input("Enter the OS-tag name: ")
				lengthOfList = len(dockerCommandList[14])
				for i in range(lengthOfList):
					cmd = "{0}{1}{2}".format(dockerCommandList[14][i][0],osTagName,dockerCommandList[14][i][1])
					run(cmd)
			elif(choice == 15):
				osTagName = input("Enter the OS-tag name: ")
				cmd = "{0}{1}".format(dockerCommandList[15],osTagName)		
				run(cmd)
			else:
				print("			Wrong Choice !!!")
		else:
			if(choice == -1):
				MainProgram()
			else:
				run(dockerCommandList[choice])

def partition():
	r=input("Where you  want  to configure ? (local/remote) :")
	while True:
		clear()
		print("""
	    	                      [ LOGICAL VOLUME MANAGER ]
	    _____________________________________|_____________________________________
	    |       |              |                           |                      |
	CREATE LVM  |  CHECK VOLUME GROUP DETAILS      CHECK LVM DETAILS     EXTEND LOGICAL VOLUME  
	(PRESS 1)   |         (PRESS 2)                     (PRESS 3)             (PRESS 4)
		    | 
	DISPLAY PHYSICAL VOLUME STATUS
			(PRESS 5)\n\n""")

		if(r == "local"):
			choice = int(input("Enter your choice:  "))
			if choice==1:
			        system("pvcreate /dev/sdc")
			        system("pvcreate /dev/sdb")
			        inpt = input("Enter volume group name[default task8]: ")
			        if inpt == "":
			        	defaultVgName = "task8"
			        else:
			        	defaultVgName = inpt
			        system("vgcreate {} /dev/sdc /dev/sdb".format(defaultVgName))
			        inpt = input("Enter Logical volume name[default task8]: ")
			        if inpt == "":
			        	defaultLvName = "lv1"
			        else:
			        	defaultLvName = inpt
			        system("lvcreate --size 20G --name {0} {1}".format(defaultLvName,defaultVgName))
			        system("mkfs.ext4 /dev/{0}/{1}".format(defaultVgName,defaultLvName))
			        dirName = input("Enter the directory name that you want to attach with Logical Volume: ")
			        system("mkdir {}".format(dirName))
			        system("mount /dev/{0}/{1} /{2}".format(defaultVgName,defaultLvName,dirName))
			elif choice==2:
				system("vgdisplay")
			elif choice==3:
				system("lvdisplay")
			elif choice==4:
				inpt = input("Enter volume group name[default task8]: ")
				if(inpt == ""): defaultVgName = "task8"
				else: defaultVgName = inpt
				inpt = input("Enter Logical volume name[default task8]: ")
				if inpt == "": defaultLvName = "lv1"
				else: defaultLvName = inpt
				extendVolSize = int(input("How much amount volume you want to increase[enter in GiB]:  "))
				system("lvextend --size +{0}G /dev/{1}/{2}".format(extendVolSize,defaultVgName,defaultLvName))
			elif choice==5:
				system("pvdisplay")
			else:
				print("not supported")
				MainProgram()
		elif r== "remote":
			ip=input("Enter the remote ip :")
			choice = int(input("Enter your choice:  "))
			if choice==1:
				system("ssh root@{} pvcreate /dev/sdc")
				system("ssh root@{} pvcreate /dev/sdb")
				inpt = input("Enter volume group name[default task8]: ")
				if inpt == "":
					defaultVgName = "task8"
				else:
					defaultVgName = inpt
				system("ssh root@{0} vgcreate {1} /dev/sdc /dev/sdb".format(ip,defaultVgName))
				inpt = input("Enter Logical volume name[default task8]: ")
				if inpt == "":
					defaultLvName = "lv1"
				else:
					defaultLvName = inpt
				system("ssh root@{0} lvcreate --size 20G --name {1} {2}".format(ip,defaultLvName,defaultVgName))
				system("ssh root@{0} mkfs.ext4 /dev/{1}/{2}".format(ip,defaultVgName,defaultLvName))
				dirName = input("Enter the directory name that you want to attach with Logical Volume: ")
				system("ssh root@{0} mkdir {1}".format(ip,dirName))
				system("ssh root@{0} mount /dev/{1}/{2} /{3}".format(ip,defaultVgName,defaultLvName,dirName))
			elif choice==2:
				system("ssh root@{} vgdisplay".format(ip))
			elif choice==3:
				system("ssh root@{} lvdisplay".format(ip))
			elif choice==4:
				inpt = input("Enter volume group name[default task8]: ")
				if inpt == "":
					defaultVgName = "task8"
				else:
					defaultVgName = inpt
				inpt = input("Enter Logical volume name[default task8]: ")
				if inpt == "":
					defaultLvName = "lv1"
				else:
					defaultLvName = inpt
				extendVolSize = int(input("How much amount volume you want to increase[enter in GiB]:  "))
				system("ssh root@{0} lvextend --size +{1}G /dev/{2}/{3}".format(ip,extendVolSize,defaultVgName,defaultLvName))
			elif choice==5:
				system("ssh root@{} pvdisplay".format(ip))
			else:
				print("not supported")
				MainProgram()				
def callProcess(cmd):
	out = sp.getstatusoutput(cmd)
	return out[1]
#split the output and convert into a list
def convert(lst):
	return (lst.split())

#searing the number of instances or volumes 
def searching(lst,word):
	cnt = 0
	for item in lst:
		if(word in item):
			cnt += 1
	return cnt-1

#finding volumeid or instanceid
def findId(lst,word):
	cnt = 0
	for item in lst:
		cnt += 1
		if(item == word):
			instancdIdd = lst[cnt+1]
			break
	return instancdIdd

awsIntroPrintList = ["Check AWS version                          ","Show instances list                        ","Check how many instances I have?           ","Launch a instance                          ","See recently created instance ID           ","Check instance status                      ","Stop recently created instance             ","Create a ebs volume of 1 GB                ","See recently created volume ID             ","Attach volume with my instance             ","Check volume status                        ","Detach the volume                          ","Delete the volume                          "]

def aws():
	count = 0
	while True:
		clear()
		IntroPagePrint(awsIntroPrintList)
		global splitedListInstance
		global splitedListVolume
		global outputIdInstance
		global outputIdVolume
		choice = int(input("		Enter your choice: "))
		if(choice == 0):
			output = callProcess("/usr/local/bin/aws --version")
			run(output)
		elif(choice == 1):
			output = callProcess("/usr/local/bin/aws ec2 describe-instances --filters Name=tag-key,Values=Name --query Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']} --output table")
			run(output)
		elif(choice == 2):
			output = callProcess("/usr/local/bin/aws ec2 describe-instances --filters Name=tag-key,Values=Name --query Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']}")
			output = convert(output)
			count = searching(output,"Instance")
			run("You have {0} instances....".format(count))
		elif(choice == 3):
			output = callProcess("/usr/local/bin/aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --subnet-id subnet-a96861c1 --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=CLI_Rhel_Instance}] --security-group-ids sg-0f70d19c8e241fceb --key-name KeyHadoop --output table")
			run(output)
			splitedListInstance = convert(output)
			outputIdInstance = findId(splitedListInstance,'InstanceId')
		elif(choice == 4):
			outputIdInstance = findId(splitedListInstance,'InstanceId')
			run("You just created this Instance Id: {}".format(outputIdInstance))
		elif(choice == 5):
			run("You have to wait for 10 seconds Boss....because you have just launched the instance...\nit will take some time to run successfully....")
			sleep(12)
			cmdd = "/usr/local/bin/aws ec2 describe-instance-status --instance-ids {0} --output table".format(outputIdInstance)
			output = callProcess(cmdd)
			run(output)
		elif(choice == 6):
			output = callProcess("/usr/local/bin/aws ec2 stop-instances --instance-ids {}".format(outputIdInstance))
			run(output)
		elif(choice == 7):
			run("Okay boss...I am creating 1GB volume for you...")
			output = callProcess("/usr/local/bin/aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size 1 --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=MyPendrive2}] --output table")
			run(output)
			splitedListVolume = convert(output)
			outputIdVolume = findId(splitedListVolume,'VolumeId')
		elif(choice == 8):
			outputIdVolume = findId(splitedListVolume,'VolumeId')
			run("You just created this Volume Id: " + outputIdVolume)
		elif(choice == 9):
			run("Attaching the volume.....")
			speak("Attaching the volume.....")
			cmdd = "/usr/local/bin/aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdh --output table".format(outputIdVolume,outputIdInstance)
			output = callProcess(cmdd)
			run(output)
		elif(choice == 10):
			run("You have to wait for 10 seconds Boss....because you have just attached the volume with instance...\nit will take some time to run successfully....")
			sleep(12)
			cmdd = "/usr/local/bin/aws ec2 describe-volume-status --volume-ids {0} --output table".format(outputIdVolume)
			output = callProcess(cmdd)
			run(output)
		elif(choice == 11):
			output = callProcess("/usr/local/bin/aws ec2 detach-volume --volume-id {}".format(outputIdVolume))
			run(output)
		elif(choice == 12):
			output = callProcess("/usr/local/bin/aws ec2 delete-volume --volume-id {}".format(outputIdVolume))
			run(output)
		else:
			print("			Wrong Choice !!!")
			sleep(3)
			MainProgram()


rc = 0
while(rc != 1):
	rc = menu()
	clear()
	if(rc == 1):
		loading()
	else:
		print("\n\n\n\t\tUnuccessfull !!!, Invalid inputs....")
		sleep(2)
