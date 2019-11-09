import subprocess
import time

 

def callf(i):
	command='curl -I https://www.theorchidschool.org/Circular/article/1470'
	command2="curl https://www.theorchidschool.org/Admissions/Online | grep '<a ' |wc -l"
	emailcommand = 'curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "gkkhatal@gmail.com" --mail-rcpt "trigger@recipe.ifttt.com" --upload-file mail.txt --user "gkkhatal@gmail.com:Ghp0tters" --insecure'
	p = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	outstr=out.decode("utf-8")
	#print("out=>",outstr)
	#print("err=>",err)
	cnt=0
	linksno=int(outstr)
	print(linksno)
	if (linksno > 143) :
		f=open("mail.txt" , "w")
		f.write("From: \"Ganesh Khatal\" <gkkhatal@gmail.com>\nTo: \"Triggers\" <trigger@recipe.ifttt.com>\nSubject: ("+str(i)+")Link is added-"+str(linksno)+"\n\n The link is added!!!")
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
