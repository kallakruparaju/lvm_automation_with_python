import os
os.system("tput setaf 6")
os.system("echo welcome to My LVM Menu| figlet -f shadow -d ./font/")
os.system("sleep 2")
while(True):
	os.system("tput setaf 2")
	print("""
	\n
	\t\tpress 1 :To Display Harddisks
	\t\tpress 2 :To create Physical volume
	\t\tpress 3 :To display Physical volume
	\t\tpress 4 :To create volume group
	\t\tpress 5 :To display volume group
	\t\tpress 6 :To create logic volume
	\t\tpress 7 :To display logic volume
	\t\tpress 8 :To Format logic volume
	\t\tpress 9 :To extend  volume
	\t\tpress 10:To resize  volume
	
	
	""")
	os.system("tput setaf 6")
	choice=int(input("Enter your choice  : "))
	os.system("tput setaf 7")
	if (choice==1):
		os.system("tput setaf 120")
		os.system("echo Displaying Harddisks| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		os.system("fdisk -l")
		os.system("sleep 5")
	elif (choice==2):
		os.system("tput setaf 11")
		os.system("echo Creating Physical Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")		
		device=input("Enter device name : ")
		os.system("pvcreate {}".format(device))
	elif (choice==3):
		os.system("tput setaf 3")
		os.system("echo Displaying Physical Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")		
		device=input("Enter device name : ")
		os.system("pvdisplay {}".format(device))
		os.system("sleep 5")
	elif (choice==4):
		os.system("tput setaf 7")
		os.system("echo Creating Volume Group| figlet -f shadow -d ./font/")
		os.system("sleep 2")	
		volumegroup=input("Enter volume group name : ")	
		a=input("Enter first device name : ")
		b=input("Enter first device name : ")
		os.system("vgcreate {} {} {}".format(volumegroup,a,b))
	elif (choice==5):
		os.system("tput setaf 120")
		os.system("echo Displaying Volume Group| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		volumegroup=input("Enter volume group name : ")
		os.system("vgdisplay {}".format(volumegroup))
		os.system("sleep 5")
	elif (choice==6):
		os.system("tput setaf 11")
		os.system("echo Creating Logic Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		volumegroup=input("Enter volume group name : ")
		logicvolume=input("Enter logic volume name : ")
		size=int(input("Enter size : "))
		os.system("lvcreate --size {}G --name {} {}".format(size,logicvolume,volumegroup))
	elif (choice==7):
		os.system("tput setaf 120")
		os.system("echo Displaying Logic Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		volumegroup=input("Enter volume group name : ")
		logicvolume=input("Enter logic volume name : ")
		os.system("lvdisplay {}/{}".format(volumegroup,logicvolume))
		os.system("sleep 5")
	elif (choice==8):
		os.system("tput setaf 120")
		os.system("echo Format Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		volumegroup=input("Enter volume group name : ")
		logicvolume=input("Enter logic volume name : ")
		os.system("mkfs.ext4 /dev/{}/{}".format(volumegroup,logicvolume))
	elif (choice==9):
		os.system("tput setaf 6")
		os.system("echo Extend  Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		size=input("Enter size : ")
		volumegroup=input("Enter volume group name : ")
		logicvolume=input("Enter logic volume name : ")
		os.system("lvextend --size +{}G /dev/{}/{}".format(size,volumegroup,logicvolume))
		
	elif (choice==10):
		os.system("tput setaf 2")
		os.system("echo Resize  Volume| figlet -f shadow -d ./font/")
		os.system("sleep 2")
		volumegroup=input("Enter volume group name : ")
		logicvolume=input("Enter logic volume name : ")
		os.system("resize2fs /dev/{}/{}".format(volumegroup,logicvolume))
	else:
		print("Wrong Input...pls try again")
		
	
