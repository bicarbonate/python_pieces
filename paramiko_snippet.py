import sys, paramiko, getpass


user = raw_input("Username:") #Prompts for username
passwd = getpass.getpass("Password for " + user + ":") #Prompts for password
name = raw_input("Target Hostname:") #Prompt for target hostname



#Calling the paramiko ssh function
ssh = paramiko.SSHClient()
print('calling paramiko')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn = ssh.connect("name", username="user", password="passwd")
print('trying to connect')

z = stdout.read()
print(z)
#ssh.close()
