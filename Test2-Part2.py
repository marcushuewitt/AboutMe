#Marcus Huewitt

#For my part 2 of the exam, I looked up reg expressions. Also being that my previous teacher spoke about it in her prior class, I decided to 
#do a program that takes in your information such as first name, last name, city, state, zip code,and street address and place it against my
#reg expression formula. It mixes in try and except as well.


import re

def main():
    try:
        firstName=""
        lastName=""
        street=""
        city=""
        zipCode=""
        state=""
        firstName=input("Please enter your first name: ")
        lastName=input("Please enter your last name: ")
        street=input("Please enter your street: ")
        city=input("Please enter your city: ")
        zipCode=input("Please zip code: ")
        state=input("Please enter a state: ")
        verifyInput(firstName,lastName,street,city,zipCode,state)
    except:
        print("You made an error!")
        
def verifyInput(firstName,lastName,street,city,zipCode,state):
    try:
        if(verifyfirstName(firstName)):
            print("First Name is: " + str(firstName))
        else: 
            print("There is an error with your First Name: ")
    except:
        print("Error!!!")
    try:
        if(verifylastName(lastName)):
            print("Last Name is: " + str(lastName))
        else:
            print("There is an error with your Last Name: ")
    except:
        print("Error!!!")
    try:
        if(verifystreet(street)):
            print("Street is: " + str(street))
        else: 
            print("There is an error with your Street: ")
    except:
        print("Error!!!")
    try:
        if(verifycity(city)):
            print("City is: " + str(city))
        else:
            print("There is an error with your City: ")
    except:
        print("Error!!!")
    try:
        if(verifyzipCode(zipCode)):
            print("Zip Code is: " + str(zipCode))
        else:
            print("There is an error with your Zip Code: ")
    except:
        print("Error!!!")
    try:
        if(verifystate(state)):
            print("State is: " + str(state))                    
        else:
            print("There is an error with State: ")                       
    except:
        print("Error!!!")
                            
                            
def verifyfirstName(firstName):
    try:
        isVeried = False
        regFirstName=re.compile("^[a-zA-Z]{1}[a-zA-Z]{0,17}{0,1}[a-zA-Z]{0,}[a-zA-Z]{1}$")
        if regFirstName.match(firstName):
            isVeried = True
        return isVeried
    except:
        print("You made an error!")
        
def verifylastName(lastName):
    try:
        isVeried = False
        regLastName=re.compile("^[a-zA-Z]{1}[a-zA-Z]{0,}{0,1}[a-zA-Z]{0,17}[a-zA-Z]{1}$")
        if regLastName.match(lastName):
            isVeried = True
        return isVeried
    except:
        print ("You made an error!")
        
def verifystreet(street):
    try:
        isVeried = False
        regStreet=re.compile("^[a-zA-Z0-9]{1,}[a-zA-Z0-9]{0,58}[a-zA-Z0-9]{1}$")
        if regStreet.match(street):
            isVeried = True
        return isVeried
    except:
        print ("You made an error!")
        
def verifycity(city):
    try:
        isVeried = False
        regCity=re.compile("^[a-zA-Z]{1}[a-zA-Z]{0,18}[a-zA-Z]{1}$")
        if regCity.match(city):
            isVeried = True
        return isVeried
    except:
        print ("You made an error!")
        
def verifyzipCode(zipCode):
    try:
        isVeried = False
        regZipCode=re.compile("[0-9]{5}$")
        if regZipCode.match(zipCode):
            isVeried = True
        return isVeried
    except:
        print ("You made an error!")
            
def verifystate(state):
    try:
        isVeried = False
        regState=re.compile("[A-Z]{2}$")
        if regState.match(state):
            isVeried = True
        return isVeried
    except:
        print ("You made an error!")
        
main()