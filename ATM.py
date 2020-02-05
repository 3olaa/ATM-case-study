import numpy as np
import random

IAT = np.random.exponential(1,size = 10**6)   #exponential distribution #1 is mean
ST1 = np.random.randint(2, 4, size = 10**6)   #unifrom distribution service time of ATM1 #2 is min, 4 is max
ST2 = []
for j in range (10**6):
    x = random.triangular(2, 4, 3.3)          #a = 2 = side1 , b = 4 = side2 , c = 3.3 = height
    ST2.append(x)                           #triangular distribution service time of ATM2
            
ST3 = np.random.normal(3, 0.5, size = 10**6)  #normal distribution service time of ATM3 #3 is mean, 0.5 is standard deviation

ATM1 = []
ATM2 = []
ATM3 = []
SST = []           #start service time
timeInSystem = []  
waitingTime = []
completionTime = []
AT = [] #arrival time (in total System)

#SeviceTime of Customer = ST (ATM he went to)

for i in range (0,10**6):
    
    if(i == 0):
        AT.append(IAT[i])
        SST.append(AT[i])  #ATM was available, no wait time
        waitingTime.append(0)
        completionTime.append(SST[i]+ ST1[i])        #hattghayar fel else 3ala 7asab el three ATMs
        timeInSystem.append(completionTime[i]- AT[i])    #or WaitingTime + ServiceTime
        ATM1.append(completionTime[i])
        ATM2.append(0)
        ATM3.append(0)
        ST2[i]=0
        ST3[i]=0
    else:
        AT.append(AT[i-1] + IAT[i])
        SST.append(max(AT[i],min(ATM1[i-1],ATM2[i-1], ATM3[i-1])))
        waitingTime.append(SST[i] - AT[i])
        if min(ATM1[i-1],ATM2[i-1], ATM3[i-1])== ATM1[i-1]:
            completionTime.append(SST[i] + ST1[i])              #or WaitingTime + ServiceTime
            ATM1.append(completionTime[i])
            ATM2.append(ATM2[i-1])
            ATM3.append(ATM3[i-1])
            ST2[i]=0
            ST3[i]=0
        elif min(ATM1[i-1],ATM2[i-1], ATM3[i-1])== ATM2[i-1]:
            completionTime.append(SST[i] + ST2[i])  
            ATM2.append(completionTime[i])
            ATM3.append(ATM3[i-1])
            ATM1.append(ATM1[i-1])
            ST1[i]=0
            ST3[i]=0
        else:
            completionTime.append(SST[i] + ST3[i])
            ATM3.append(completionTime[i])
            ATM2.append(ATM2[i-1])
            ATM1.append(ATM1[i-1])
            ST1[i]=0
            ST2[i]=0
        timeInSystem.append(completionTime[i] - AT[i])
        
utilizationOfATM1 = sum(ST1)/max(ATM1)
utilizationOfATM2 = sum(ST2)/max(ATM2)
utilizationOfATM3 = sum(ST3)/max(ATM3)
maxWaitingTime = max(waitingTime)
averageWaiting = sum(waitingTime)/10**6
minuteWait = []
wait = []
for i in range (10**6):
    if waitingTime[i]>1:
        minuteWait.append(waitingTime[i])
    if waitingTime[i]>0:
        wait.append(waitingTime[i])
waitProbability = len(wait)/10**6         #people waiting        
minuteProbability = len(minuteWait)/10**6 #people waiting more than 1 minute

print("utilization of ATM1: ",utilizationOfATM1, "\n")
print("utilization of ATM2: ",utilizationOfATM2, "\n")
print("utilization of ATM3: ",utilizationOfATM3, "\n")
print("Average waiting time: ",averageWaiting,"\n")
print("Maximum waiting time: ",maxWaitingTime,"\n")
print("probability of waiting time: ",waitProbability,"\n")
print("probability of waiting more than 1 minute: ",minuteProbability,"\n")

        
