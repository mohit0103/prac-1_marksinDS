scoreinDS=[]

noofstudents=int(input("Enter no of Students : ")) 
for i in range(noofstudents):
   marks=int(input(f"Enter the score of student "+str(i+1)+" : "))
   scoreinDS.append(marks)

#avg
def average(listofmarks):  
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-1:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("Total Marks : ", sum)
    print("Average Marks : {:.2f}".format(avg))
average(scoreinDS)

#maximum 
def maximum(listofmarks):
  Max = listofmarks[0]
  for i in range(len(listofmarks)):
    if listofmarks[i]>Max:
      Max = listofmarks[i]
  return (Max)
print("Highest score in the class is : ", maximum(scoreinDS))

#Minimum
def minimum(listofmarks):
  Min = listofmarks[0]
  for i in range(len(listofmarks)):
    if listofmarks[i]<Min:
      Min = listofmarks[i]
  return (Min)
print("Lowest score in the class is : ", minimum(scoreinDS))

#absent 
def absentCnt(listofmarks):
    cnt=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-999:
            cnt+= 1
    return (cnt)
print("Count of students who were absent for the test is: ", absentCnt(scoreinDS))

#frequency 
def maxFrequency(listofmarks):
    i = 0
    Max = 0
    print("Marks ----> frequency count ")
    for j in listofmarks:
        if listofmarks.index(j) == i:
            print(j, "---->", listofmarks.count(j))
            if listofmarks.count(j) > Max:
                Max = listofmarks.count(j)
                mark = j
        i += 1
    return (mark, Max)
mark, count = maxFrequency(scoreinDS)
print("Highest frequency of marks {0} is {1} ".format(mark, count))
