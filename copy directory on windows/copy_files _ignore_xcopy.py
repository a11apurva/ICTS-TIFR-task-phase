import os
import sys
import time

start_time = time.time()

folders=["3.1.5"]

f=open("copied_files.txt","w")

excludelist="exclude.txt"

for foldername in folders:
    try:
        dir_src = os.path.join(r"Z:\copied_folder",foldername)
        dir_dst = os.path.join(r"C:\Projects\TestLogs\copied_folder",foldername)


        #os.system('xcopy "%s" "%s" /i/c/s/q/y/j' % (dir_src, dir_dst))
        #os.system('xcopy /exclude:"%s" "%s" "%s"' % (excludelist,dir_src, dir_dst))
        os.system('xcopy /exclude:%s %s %s /i/c/s/y/j/q' % (excludelist,dir_src, dir_dst))
        
        print "copied folder : "+foldername
        f.write(str(foldername)+"\n")
        
    except Exception as e:
        print(e)
        f.write(str(e)+"\n")
        continue

f.close()
print "\n***Done Copying***\n"
print("--- %s seconds ---" % (time.time() - start_time))
