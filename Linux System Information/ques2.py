import subprocess


def cpu_info():
        print '\nCPU Details:'
        print "------------"

        command = "cat /proc/cpuinfo"
        cpu= subprocess.check_output(command, shell=True).strip()
        cpu=cpu.split('\n')

        cpu_count=0
        logical_cpu_count=0


        for line in cpu:
                if 'physical id' in line:
                        cpu_count=int(line.split('\t')[-1].split()[-1])
                if 'processor' in line:
                        logical_cpu_count+=1
                if 'model name' in line:
                        model=line.split('\t')[-1][1:]

        cpu_count+=1

        print "CPU model:"+model
        print "Number of Physical CPUs:\t"+str(cpu_count)
        print "Number of Logical CPUs:\t\t"+str(logical_cpu_count)



def memory_info():
        print '\nMemory Details:'
        print "---------------"

        command = "cat /proc/meminfo | grep MemTotal"
        memory= subprocess.check_output(command, shell=True).strip()
        print 'Total RAM: '+str(round((float(memory.split()[-2])/(1024*1024)),2))+' GB'

        command = "cat /proc/meminfo | grep SwapTotal"
        memory= subprocess.check_output(command, shell=True).strip()
        print 'SWAP Area: '+str(round((float(memory.split()[-2])/(1024*1024)),2))+' GB'

def os_info():
        print '\nOperating System Details:'
        print "-------------------------"

        command = "uname -a"
        os= subprocess.check_output(command, shell=True).strip()
        os=os.split(' ')

        print 'Kernel Name:\t\t' +str(os[0])
        print 'Kernel Release:\t\t' +str(os[2])
        print 'Kernel Version:\t\t' +str(os[3])
        print 'Operating System:\t' +str(os[-1])



def disk_info():
        print '\nDisk Space Details:'
        print "-------------------"

        command = "df -h --total"
        disk= subprocess.check_output(command, shell=True).strip()
        disk=disk.split('\n')[-1].split()

        print 'Total Size:\t' +str(disk[1])+" GB"
        print 'Used:\t\t' +str(disk[2])+" GB"
        print 'Availabe:\t' +str(disk[3])+" GB"




def avg_load():
        print '\nLoad Average:'
        print "---------------"

        command = "uptime"
        load= subprocess.check_output(command, shell=True).strip()

        print "Load Average over last 15 mins: "+load.split()[-1]






def user_info():
        print '\nLogged in users:'
        print "----------------"

        command = "who -q"
        user= subprocess.check_output(command, shell=True).strip()
        user=user.split('\n')[0].split(' ')

        for u in user:
                print u

        



if __name__ == '__main__':
        cpu_info()
        memory_info()
        os_info()
        disk_info()
        avg_load()
        user_info()
        print '\n'

