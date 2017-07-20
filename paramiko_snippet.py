import sys, paramiko

#Requests user input for a target IP address
#print = "Enter the target IP"
#hostname = input('Enter the target IP address')

#Sets env variables
user = 'skeer'
password = 'Oplsai386'
hosts = 'sputnik'

print( #Greeting Messges.
    "\n"
    "1 Enter your Username"
    "\n2 Enter your password"
    "\n3 Enter the hostname")


#Calling the paramiko ssh function
ssh = paramiko.SSHClient()
print('calling paramiko')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn = ssh.connect("hosts", username="user", password="password")
print('trying to connect')
cmd = 'uptime'
print('')
print(cmd)
(stdin, stdout, stderr) = ssh.exec_command(cmd)
z = stdout.read()
print(z)
#ssh.close()
