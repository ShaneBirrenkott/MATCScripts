#!/usr/bin/env python3
#Shane Birrenkott, SBirrenkott@MadisonCollege.edu

import subprocess

#subprocess.run() synch
#subprocess.popen() asynch
#subprocess.call() true/false if the command worked

def main():
    myProc = subprocess.run(['ps','-axco','command'], stdout=subprocess.PIPE)

    myProcString = myProc.stdout.decode("utf-8")

    myProcList = myProcString.split('\n')

    for out in myProcList[1:]:
        print(out)

    print(len(myProcList[1:]))

if __name__=='__main__':
    main()