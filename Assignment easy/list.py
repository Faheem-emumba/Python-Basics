#List Operations

# calculating the sum of the list elements
def calculateSum( inputList ):
    
    if len(inputList) == 0:
        print("The list is empty")
        return
    
    sum=0
    for number in inputList:
        sum+=number
    print(sum) 
    
# calculating the average of the list of elements
def calculateAverage( inputList ):
    
    lengthOfList=len(inputList)
    
    if lengthOfList == 0:
        print("The list is empty")
        return
    
    sum=0
    for number in inputList:
        sum+=number
    print(sum/lengthOfList)  
    
# finding the max number in the list 
def findMax(inputList):
    
    listLength=len(inputList)
    
    if listLength == 0:
        print("The list is empty")
        return
    
    max= inputList[0]
    i=1
    
    while i<listLength:
        if max< inputList[i]:
            max=inputList[i]
        i=i+1    
        
    print(max)       
    
# reversing a list
def reverseList(inputList):
    listLength=len(inputList)
    
    if listLength == 0:
        print("The list is empty")
        return
    start=0
    end=listLength-1
    
    while start < end :
        temp=inputList[start]
        inputList[start]=inputList[end]
        inputList[end]=temp
        
        start+=1
        end-=1
    
    print(inputList)
    

#code execution

numbers = [1, 5, 3, 8, 2]

calculateSum(numbers)
calculateAverage(numbers)
findMax(numbers)

my_list = ['a', 'b', 'c']
reverseList(my_list)