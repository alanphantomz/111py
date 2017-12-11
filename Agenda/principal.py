#My First program in python "An agenda"
#My libreries
import modules

#-----------START PROGRAM----------------
print("wellcame to your electronic agenda!!")
respuesta = "-5"

while respuesta != "5":
    modules.ini()
    respuesta=input(">")    
    if respuesta=="1":
        modules.insertPeople()
    elif respuesta == "2":
        modules.listContacts()
    elif respuesta == "3":
        modules.deleteContact()
    elif respuesta =="4":
        modules.createAgenda()
    elif respuesta == "5":
        print("Good bye!!")
    else :
        print("opcion no  valida")
        respuesta="-5"
