import os
import sys
import subprocess


filelist = []
gtfobinlist = []
matchesfound = False

print("USAGE: searchsuid.py {examplefile}")
print("python3 searchsuid.py #Takes local settings")
print("python3 searchsuid.py target-file.txt #Takes settings exported from 'find / -perm /4000 2>/dev/null' of remote server")

try:
    if sys.argv[1] != "":
        with open(sys.argv[1]) as suidfile:
            for line in suidfile:
                filelist.append(line)
    suidfile.close()

except:
    sudol = subprocess.run(['find', '/', '-perm', '/4000'], text=True, capture_output=True)
    print("Current find / -perm /4000 2>/dev/null")
    
    for line in sudol.stdout.split('\n'):
        print(line)
        filelist.append(line)



with open('gtfobinsuids') as gtfobinexploits:

    for i in (gtfobinexploits):
        gtfobinlist.append(i)
        #print("gtfo", i)


    print("TRYING TO FIND MATCHES:")
    for line in( filelist ):
        line = line.rstrip()

        line = line.split("/")
        #print(line)
        #print(line[-1])
        for gtfoline in gtfobinlist:
            gtfoline = gtfoline.rstrip()
            if line[-1] == gtfoline:
                print("gtfoline FOUND!", gtfoline)
                matchesfound = True
            else:
                pass
                #print("NOT FOUND", gtfoline, line[-1])
    if matchesfound == False:
        print("Sorry, No matches found")

