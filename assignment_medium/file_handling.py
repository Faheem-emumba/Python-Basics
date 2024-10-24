import csv

def calculateAverageGrade():
    with open('choclate.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        
        for row in reader:
            name = row["Name"]
            math = float(row['Math'])
            science = float(row['Science'])
            english = float(row['English'])

            print(name, ":", (math + science + english) / 3)


def writeData():

    with open('new_file.csv','a',newline='') as f:

        fieldnames = ["Name", "Phone"]  
        dictWriter = csv.DictWriter(f, fieldnames=fieldnames,delimiter=',')

        #dictWriter.writeheader() #run only first time
        
        print("Add data in Address book")
        name=input("Enter name: ")
        phnNumber=input("Enter Phone Number: ")

        data={"Name":name,"Phone":phnNumber}

        dictWriter.writerow(data)
      
def readData():
        with open('new_file.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')

            print("want to search for data in Address book")
            name=input('Enter Name for retieving data: ')

            for row in reader:
                 if row["Name"].lower()== name.lower():
                      print("Name : ",name, " Phone Number : " ,row['Phone'])
                      return
                 
            print("No data found for ", name) 




#writeData()
readData()
#calculateAverageGrade()

