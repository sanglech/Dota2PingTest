import subprocess
import time
class Testing(object):
    def hello_world(self):
        print ("Hello World")
    def run_this(self,_textfile):
        proc=subprocess.Popen("ping 208.78.164.1 -n 100",stdout=_textfile)
        while proc.poll() is None:
            time.sleep(0.5)

def ping_check():
    something=Testing()
    with open("PingResults.txt", "w") as textfile:
        something.run_this(textfile)
    with open ("PingResults.txt", "r") as textfile:
        for line in textfile:
            if "Average = " in line:
                check=line.split()
    return(check[-1])


ready=input("Time to play dota? Y/N")
yes=["yes","Y","y","Yes"]
quit=["quit","Q","q","Quit","N","n","No","no"]
while ready not in quit:
    if (ready in yes):
        print("Checking ping to dota2 USEast servers")
        avg_ping=ping_check()
        print("Your Average ping to USEast is %s. Please see log for further details\n "%avg_ping)
        print("Finished checking ping to Dota USEast Servers")
    else:
        ready=input("Quit?")
    ready=input("Test again or quit? Y/N")
#something=Testing()
#something.hello_world()
