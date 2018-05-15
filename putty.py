import ssh
import paramiko
ssh = paramiko.SSHClient()
hostname = "159.89.170.250"
username="root"
password="$38205_38205$"
command ="df -h"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
x= ssh.connect(hostname,22,username,password)
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command (command)
print stdout.read()

print x

