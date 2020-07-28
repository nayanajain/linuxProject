import os
os.system("tput setaf 5")
print("       *************************")
os.system("tput setaf 1")
print("       HEY GENIUS! Welcome to my project")
os.system("tput setaf 3")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
os.system("tput setaf 6")
print("\tHere I am building a simple menu using linux o.s. and python integration. Well, you may be thinking why I have chosen python with Linux ??")

os.system("tput setaf 2")
print("Though many other great platforms available and this is the era of AUTOMATION. To enhance automation, we have Integrated python with Linux.") 
os.system("tput setaf 3")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
os.system("tput setaf 5")
key=input("press any key to continue")
os.system("clear")
os.system("tput setaf 5")
ch='y'

while(ch=='y') :
  os.system("tput setaf 2")
  print("how would you like to execute-- local or remote",end="")
  os.system("tput setaf 4")
  location=input()

  if(location=='local') :

    print(""" BASIC COMMANDS
    press 0 to see ip configuration of your system.
    press 1 to show date
    press 2 for calender
    press 3 if you want to run multiple program
    press 4 for adding new user
    press 5 to create file
    press 6 to see manual of any software
    press 7 to print output in a file
    press 8 if you want to know to create alias
    press 9 for searching particular word from file
    press 10 to see how much RAM is used by system.
    press 11 to install any software (using RedHat Package Management)
    press 12 if you want to install any software through yum 
    press 13 if you want to see port number and inode table of any program.
    press 14 if you want to copy any file from one folder to another
    press 16 to delete a foldername
    press 17 if you want to see number of partitions
    press 18 to see name of kernel.
    press 19 to see RAM.   
    press 20 to see graphical representation of process.
    press 21 if you want to create a user 
    press 22 if you want to see details of all the user
    press 23 if you want to create a group
    press 24 if you want to create a new user as well as add user into the group    press 25 if you want to add existing user into the group
   
    PYTHON COMMANDS BASIC
    press 26 wanna know about getpass command
           
    
     
    """)
     
    os.system("tput setaf 5")
    ch=input()

    if(int(ch)==0):
      os.system("ifconfig")
    elif(int(ch)==1):
      os.system("date")
    elif(int(ch)==2):
      os.system("cal")
    elif(int(ch)==3):
      name1=input("enter name of 1st  program you want to run(here only 2")
      name2=input("enter name of 2nd  program you want to run")
      os.system("{};{}".format(name1,name2))
    elif ch=='4':
      user=input("enter name of new user")
      os.system("useradd {}".format(user))
    elif(int(ch)==5) :
      name=input("enter name of file")
      os.system("touch {}.txt".format(name))
      print("file created")
    elif ch=='6':
      name=input("enter name of program you want to see manual")
      os.system("man {}".format(name))
    elif ch=='7':
      name=input("enter name of program you want to see")
      files=input("enter the name of file for displaying output") 
      os.system("{} &> {}".format(name,files))
      print("output stored in file")
    elif ch=='8':
      print("alias creation format: alias (var name)=(command name)")
    elif ch=='9':
      name=input("enter name of the file")
      w=input("enter word you want to search")
      os.system("grep {} {}".format(w,name))
    elif ch=='10':
      os.system("free -m")  
    elif ch=='11':
      name=input("enter name of software")
      os.system("rpm -i {}".format(name))
    elif ch=='12':
      ch=input("want to know why yum is better then RPM")
      if(ch=='y'):
        print("......................")
      n=input("enter name of program you want to install")
      os.system("yum install {}".format(name))
    
    elif ch=='13':
      os.system("netstat -n")

    elif ch=='14' :
      n1=input("enter the name of the file")
      n2=input("enter new file name")
      os.system("cp {} {}".format(n1,n2))
      print("file copied")
    elif ch=='16':
      n=input("enter the name of the folder")
      ch=input("are you sure???(y/n)")
      if(ch=='y'):
        os.system("rm -r {}".format(n1))
        print("folder deleted")    
      print("folder not deleted")
    elif ch=='17' :
      os.system("fdisk -l")
      os.system("partprobe /dev/sda")
    elif ch=='18':
      os.system("uname -r")
    elif ch=='20' :
      os.system("pstree")
    elif ch=='21' :
      os.system("useradd {}".format(user))
    elif ch=='22' :
      os.system("cat /etc/passwd")
    elif ch=='23' :
      name=input("enter the name of the group")
      os.system("groupadd {}".format(name)) 
    elif ch=='24' :
      name=input("enter name of the user")
      name2=input("enter name of the group")
      os.system("useradd -g {} {}".format(name2,name))
    elif ch=='25' :
      name=input("enter the name of the existing user you want to add in group")
      name2=input("enter name of the group")
      os.system("usermod -g {} {}".format(name2,name))
    elif ch=='26' :
      import getpass
      a=getpass.getpass()
      print("have you understood difference between getpass and input command")
      os.system("tput setaf 1")
      print("getpass is a command used for taking secure input like password")
      print("Whereas input command is used for taking general input")
    else :
      print("wrong choice")

  elif(location=='remote'):
    remoteIP=input("enter remote ip address")
    print(""" press 1 to show date
              press 2 for calender
              press 3 for adding new user
              
        """)
    ch=input()
    if(int(ch)==1) :
      os.system("ssh {} date".format(remoteIP))
    elif(int(ch)==2) :
      os.system("cal")
    elif ch=='3':
      user=input("enter name of new user")
      os.system("ssh {} useradd {}".format(remoteIP,user))


    else:
      print("wrong choice")
  else:
     print("wrong location! no such ip address")

  print("want to enter more")
  ch=input()


    

     
