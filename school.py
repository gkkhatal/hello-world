import subprocess
import time

 

def callf(i):
	command='curl -I https://www.theorchidschool.org/Circular/article/1470'
	emailcommand = 'curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "gkkhatal@gmail.com" --mail-rcpt "trigger@recipe.ifttt.com" --upload-file mail.txt --user "gkkhatal@gmail.com:Ghp0tters" --insecure'
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	outstr=out.decode("utf-8")
	print("out=>",outstr)
	print("err=>",err)
	cnt=0
	if "HTTP/1.1 200" in outstr:
		q=subprocess.Popen(emailcommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(i," Success")
	else:
		print(i," Failure")
	#for line in out
		#the real code does filtering here
	#	print(i+" test:", line)
	
i = 0
while i > -1:
	i=i+1
	#print(i);	
	callf(i)
	time.sleep(10)
	
