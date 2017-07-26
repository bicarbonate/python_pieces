[root@ ec2-user]# python
Python 2.6.9 (unknown, Oct 29 2013, 19:58:13)
[GCC 4.6.3 20120306 (Red Hat 4.6.3-2)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import paramiko
>>>
>>> ip = '1.1.1.16'
>>> username = 'testuser'
>>> password = 'password'
>>>
>>> remote_conn_pre=paramiko.SSHClient()
>>> remote_conn_pre
<paramiko.SSHClient object at 0x15f47d0>
>>>
>>> remote_conn_pre.set_missing_host_key_policy(
...   paramiko.AutoAddPolicy())
>>>
>>> remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
>>>

[root@ ec2-user]# netstat -an | grep 22
tcp
0
0
0.0.0.0:22	0.0.0.0:*	LISTEN
tcp
0
0
10.10.10.22:55566
1.1.1.16:22	ESTABLISHED


>>>
>>> remote_conn.send("show ip int brief\n")
18
>>> output = remote_conn.recv(5000)
>>> print output
show ip int brief
Interface	IP-Address	OK?	Method	Status	Protocol
FastEthernet0
unassigned
YES	unset	up	up
FastEthernet1	unassigned	YES	unset	up	up
FastEthernet2	unassigned	YES	unset	down	down
FastEthernet3	unassigned	YES	unset	up	up
FastEthernet4	1.1.1.16	YES	NVRAM	up	up
NVI0	1.1.1.16	YES	unset	up	up
Tunnel1	169.254.253.2	YES	NVRAM	up	down
Tunnel2	169.254.253.6	YES	NVRAM	up	down
Vlan1	unassigned	YES	NVRAM	down	down
Vlan10	10.2.8.1	YES	NVRAM	up	up
Vlan20	192.168.0.1	YES	NVRAM	down	down
--More--
