import os
import subprocess
from datetime import datetime
import subprocess
import smtplib

directories=['file1','direc1/file1']

email_sender="albert.einstein@ligo.org"
email_receiver="richard.feynman@icts.res"
password="********"

remote_path="/path/remote/location"

curr_date = datetime.now().strftime ("%Y-%m-%d")
curr_date=datetime.strptime(curr_date, '%Y-%m-%d').date()


def days_between(d1):
    d1=datetime.strptime(d1, '%Y-%m-%d').date()
    return abs((curr_date - d1).days)



def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        SUBJECT = "BACKUP FALIURE"
        TEXT = "Backup Procedure failed on DATE: "+str(curr_date)+"\nPlease contact the system administrator.\nThank you."
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(email_sender, email_receiver, message)
        server.quit()
    except:
        print 'Network Error...'

def transfer_file(local_path):
    command="scp remote_user@remote_host:"+remote_path+" "+local_path
    cpu= subprocess.check_output(command, shell=True).strip()




if __name__ == '__main__': 
    try:
        command="mkdir -p backup"
        cpu= subprocess.check_output(command, shell=True).strip()

        file_name = "backup_"+str(curr_date)+".tar"

        command = "tar cf backup/"+file_name
        for direc in directories:
                command+=" "+direc

        cpu= subprocess.check_output(command, shell=True).strip()
            
        #transfer_file("backup/"+file_name)

        for file in os.listdir("backup"):
            file=os.path.join("backup", file)
            #print(file)
            command="stat -c %y "+file
            cpu= subprocess.check_output(command, shell=True).strip()
            print file+"\t"+cpu.split()[0]+"\t"+str(days_between(cpu.split()[0]))
            if (days_between(cpu.split()[0]) >= 7 ):
                command="rm "+file
                cpu= subprocess.check_output(command, shell=True).strip()
                print file+" deleted"

    except:
        print('error')
        send_email()
    
            
