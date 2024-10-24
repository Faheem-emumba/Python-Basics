#Data Validation 
import re

def validateInput(value,dataType):

    if dataType=="integer":
        try:
            int(value)
            return True
        except ValueError as e:
            print("Invalid data type \nError:",e )
            return False

    elif dataType=="float":

        try:
            float(value)
            return True
        except ValueError as e:
            print("Invalid data type \nError:",e )
            return False
        
    elif dataType=="email":

        # email_regex = r'^(?=.*\bemail\b).+@.+\..+$'
    
        # if re.match(email_regex, value):
        #     return True
        # else:
        #     print("Invalid email address.")
        #     return False

        return "email" in value
    
    else:
        print("Entered Invalid data type")
        return


value = "[email address removed]"
data_type = "email"

print(validateInput(value,data_type))

