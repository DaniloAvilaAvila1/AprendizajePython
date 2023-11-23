#Tipos de error
#Primer tipo de error
#SyntaxError
#print "¡Hola comunidad!" #Descomentar para error
print("¡Hola comunidad!")

#Segundo tipo de error
#NameError
language="spanish" #Comentar para error
print(language)

#Tercer tipo de error
#IndexError
my_list=["Python","Swift","Kotlin","Dart","JavaScript"]
print(my_list[4]) #Si le pongo 5, da error

#Cuarto tipo de error
#ModuleNotFoundError
#import maths #Descomentar para que nos de error
import math

#Quinto tipo de error
#AttributeError
#print(math.PI) #Descomentar para que nos de error
print(math.pi)

#Sexto tipo de error
#KeyError
my_other_dict={"Nombre":"Danilo","Apellido":"Avila","Edad":35,1:"Python"}
print(my_other_dict["Edad"])
#print(my_other_dict["Apelido"]) #Descomentar para que nos de error
print(my_other_dict["Apellido"])

#Septimo tipo de error
#TypeError
#print(my_list["Nombre"]) #Descomentar para que nos de error
print(my_list[0])

#Octavo tipo de error
#ImportError
#from math import PI #Descomentar para que nos de error
from math import pi
print(pi)

#Noveno tipo de error
#ValueError
my_int=int("10")
#my_int=int("10 Años") #Descomentar para que nos de error
print(my_int)

#Decimo tipo de error
#ZeroDivisionError
print(4/2)
#print(4/0) #Descomentar para que nos de error