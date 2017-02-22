from csp import *
from KenKen import *
from inputReader import *
import sys
import time
import os


Results=[]
fileName = str(sys.argv[1])
args = ReadInput(fileName)


Possible_Values=""

for i in range(1,args[0]+1):
    Possible_Values+=str(i)

#ta domain 8a einai me thn idia seira gia olous tous algori8mous gia na einai dikaih h sugkrish
Domain=OrderedDict()

for i in range (0,args[0]):
    for j in range (0,args[0]):       
        Domain[str(i)+str(j)]=Possible_Values

k = KenKen(args,Domain,0)   
start_time = time.time()
print("Now executing BT")
start_time = time.time()
res = backtracking_search(k)
k.PrintGrid(res)
exTime=time.time() - start_time
print("Total assignments :",k.nassigns)
print("BT execution time    : %.3f secs" % (exTime))
Results.append([k.nassigns , round(exTime,3)])

k = KenKen(args,Domain,0) 
start_time = time.time()
print("Now executing BT+MRV")
start_time = time.time()
res = backtracking_search(k, select_unassigned_variable=k.mrv)
k.PrintGrid(res)
exTime=time.time() - start_time
print("Total assignments :",k.nassigns)
print("BT+MRV execution time    : %.3f secs" % (exTime))
Results.append([k.nassigns , round(exTime,3)])


k = KenKen(args,Domain,0) 
start_time = time.time()
print("Now executing FC")
start_time = time.time()
res = backtracking_search(k,inference=forward_checking)
k.PrintGrid(res)
exTime=time.time() - start_time
print("Total assignments :",k.nassigns)
print("FC execution time    : %.3f secs" % (exTime))
Results.append([k.nassigns , round(exTime,3)])

k = KenKen(args,Domain,0) 
start_time = time.time()
print("Now executing FC+MRV")
res = backtracking_search(k, select_unassigned_variable=k.mrv2, inference=forward_checking)
k.PrintGrid(res)
exTime=time.time() - start_time
print("Total assignments :",k.nassigns)
print("FC+MRV execution time    : %.3f secs" % (exTime))
Results.append([k.nassigns , round(exTime,3)])

k = KenKen(args,Domain,0) 
start_time = time.time()
print("Now executing MAC")
start_time = time.time()
res = backtracking_search(k,inference=mac)
k.PrintGrid(res)
exTime=time.time() - start_time
print("Total assignments :",k.nassigns)
print("MAC execution time    : %.3f secs" % (exTime))
Results.append([k.nassigns , round(exTime,3)])



spaceNum=[]
exTimeStr=[]

for res in Results:
    spaceNum.append(len(str(res[0])))
    spaceNum.append(len(str(res[1]))) 

spaces=""
for i in range(0,max(spaceNum)):
    spaces+=" "
spaces+="|"


line1 =" |                  |    BT  "+spaces+"  BT+MRV"+spaces+"    FC  "+spaces+"  FC+MRV"+spaces+"   MAC  "+spaces
line2 =""
for i in range(0,len(line1)):
    if(line1[i]=="|"):
        line2+="+"
    else:
        line2+="-"

print(line1)


assignmentsLine =" |Total Assignments |"
exTimeLine =" |Execution Time    |"

Assign_container=[]
Ex_container=[]
for i in range(0,5):
    w1="  "+str(Results[i][0])
    w2="  "+str(Results[i][1])
    for j in range(0,5+(len(spaces))-len(str(Results[i][0]))):
        w1+=" "
    w1+="|"

    for j in range(0,5+(len(spaces))-len(str(Results[i][1]))):
        w2+=" "
    w2+="|"
    

    Assign_container.append(w1)
    Ex_container.append(w2)

for i in range(0,5):
    assignmentsLine+=Assign_container[i]    
    exTimeLine+=Ex_container[i]


print(line2)
print(assignmentsLine)
print(line2)
print(exTimeLine)
print(line2)


k = KenKen(args,Domain,1)
start_time = time.time()
print("Now executing MIN_CONFLICTS")

start_time = time.time()
res=min_conflicts(k, max_steps=10000)

exTime=time.time() - start_time
if(res!=None):
    k.PrintGrid(res)
else:
    print("Could not find solution")

print("Total assignments :",k.nassigns)
print("MIN_CONFLICTS execution time    : %.3f secs" % (exTime))



