#fo=open("foo.txt","r+")
##print("Name of the file:",fo.name)
##print("Closed: ",fo.closed)
##print("Opening mode: ",fo.mode)
##string=fo.read()
##print("Read String is: ",string)
##fo.close()
import os
#os.rename("foo.txt","archivo.txt")
#os.remove("archivo.txt")
#os.mkdir("palabras_favoritas")
#os.chdir("palabras_favoritas")#cambia de directorio actual mientras se ejecuta el script
os.chdir(r"c:\\")#cambiamos al directorio "c"
#os.mkdir("recontraputa")
os.rmdir("recontraputa")
print(os.getcwd())#despliega el directorio de trabajo actual
