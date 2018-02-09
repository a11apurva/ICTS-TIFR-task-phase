import myshutil
from myshutil import copytree, ignore_patterns
import os


folders=["3.2.1"]

f=open("copied_files.txt","w")

for foldername in folders:
    try:
        dir_src = os.path.join(r"Z:",foldername)
        dir_dst = os.path.join(r"C:\Projects\TestLogs\copied_folder",foldername)

        copytree(dir_src, dir_dst, ignore=ignore_patterns('*.ko', '*dump*','vm*'))

        print "copied folder : "+foldername
        f.write(str(foldername)+"\n")
        
    except Exception as e:
        print(e)
        f.write(str(e)+"\n")
        continue

f.close()
print "\n***Done Copying***\n"
