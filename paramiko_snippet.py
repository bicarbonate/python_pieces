import sys, paramiko, getpass


user = input("Username:") #Prompts for username
#passwd = getpass.getpass("Password for " + user + ":") #Prompts for password
key_file = input("Public key full path:") #Prompts for full path to key file
name = input("Target Hostname:") #Prompt for target hostname
command = input("Enter target command:") #Prompt for remote command


#Calling the paramiko ssh function
ssh = paramiko.SSHClient() #Define value 'ssh' as calling the paramiko.sshclient
print('calling paramiko')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Must come before connect line to add hosts to known_hosts
#ssh.connect("name", username="user", password="passwd")
ssh.connect(hostname = name, username = user, key_filename = key_file) # key_filename means to specify, pkey on the
#other hand means to actually paste in the key text itself
print('trying to connect')
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command (command)
print(stdout.read())
#ssh.close()
