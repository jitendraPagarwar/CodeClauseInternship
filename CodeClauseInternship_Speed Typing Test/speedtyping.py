from time import* 
import random



def mistake(partest,usertest):
    error=0
    for i in range(len([partest])):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except:
             error=error+1
    return error    
def speedtime(time_start,time_end,userinput):
    time_delay=time_end-time_start
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)


jp=["my name is jitendra","python programming languages is important",
    " It is important for intervie"
    " very complicated ",
"create many big  project"]

jp1=random.choice(jp)
print("****Typing Speed****")
print(jp1)
time1=time()
jpinput=input("Enter:")
time2=time()

print('speed:',speedtime(time1,time2,jpinput),"w/sec")
print("error:",mistake(jp1,jpinput))