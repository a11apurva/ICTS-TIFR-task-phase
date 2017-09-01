import subprocess

f=open('users.csv')


command="mkdir -p /archive/home"
subprocess.check_output(command, shell=True).strip()

command="mkdir -p /scratch"
print subprocess.check_output(command, shell=True).strip()


for line in f:
    line=line.strip().split(',')
    u_name=line[0]
    f_name=line[1]
    email=line[2]
    group=line[3]

    try:

        command="getent group "+group+" || sudo groupadd "+group	# create a new roup if not already exists
        print subprocess.check_output(command, shell=True).strip()
        
        command = "useradd -m "+u_name+" -N -G "+group+" -d /archive/home/"+u_name+" -c \""+f_name+","+email+"\""	# Add a new user with necessary details
        print subprocess.check_output(command, shell=True).strip()

	command="mkdir -p /scratch/"+u_name				# create a new usr folder under /scratch
	print subprocess.check_output(command, shell=True).strip()

	command="chgrp "+group+" /scratch/"+u_name			# assign the folder to the users's group
	print subprocess.check_output(command, shell=True).strip()

	command="chmod g+r-x /scratch/"+u_name				# grant read and execute permission
	print subprocess.check_output(command, shell=True).strip()

	command="chgrp "+group+" /archive/home/"+u_name			# assign the folder to the users's group
	print subprocess.check_output(command, shell=True).strip()

	command="chmod g+r-x /archive/home/"+u_name			# grant read and execute permission
	print subprocess.check_output(command, shell=True).strip()


	command="setfacl -m u:"+u_name+":rwx /archive/home/"+u_name	# grant read, write and execute permission to the user
	print subprocess.check_output(command, shell=True).strip()

	command="setfacl -m u:"+u_name+":rwx /scratch/"+u_name		# grant read, write and execute permission to the user
	print subprocess.check_output(command, shell=True).strip()

	command="chown "+u_name+":"+group+" /scratch/"+u_name		# grant ownership of the folder under /scratch to the user
	print subprocess.check_output(command, shell=True).strip()

    except Exception, e: print e


f.close()


