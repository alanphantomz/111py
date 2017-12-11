def ini():    
    print("1. INSERT NEW")
    print("2. LIST CONTACTS")
    print("3. DELETE  ALL CONTACTS")
    print("4. CREATE AGENDA")
    print("5. SALIR")

def listContacts():
    file=open("contacts.csv",'r')
    print("Your Contacts:")
    print("Name\tNumber")
    print((file.read()).replace(",","\t"))
    
def createAgenda():
    file=open("contacts.csv",'x')
    file.close()

def insertPeople():
    file=open("contacts.csv",'a')
    print("Input Name: ")
    name=input(">")
    print ("Input Number: ")
    number=input(">")
    print ("Your Data:")
    print ("Name: %s Number %s" %(name,number))
    file.write(name+","+number+"\n")
    file.close()
    print ("Your contact has been saved!!")

def deleteContact():
    file=open("contacts.csv",'w')
    file.truncate()
    file.close()
