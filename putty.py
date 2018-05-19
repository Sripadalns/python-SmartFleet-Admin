import ssh
import paramiko
import datetime
ssh = paramiko.SSHClient()
hostname = "159.89.170.250"
username="root"
password="$38205_38205$"
command ="df -h"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
x= ssh.connect(hostname,22,username,password)
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command (command)
x= stdout.read()
print stdout.read()
print x

text_file = open("Output.txt", "a")
datex = str(datetime.date.today())
text_file.write(datex)
text_file.write("\n")
timex=str(datetime.datetime.now().time())
text_file.write(timex)
text_file.write("\n")
text_file.write(x)
text_file.write("***********************\n")

text_file.close()
print x

