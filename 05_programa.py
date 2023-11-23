#Funciones
#Una funcion va intentar resolver un problema muy concreto que nosotros vamos a indicar.
#Sintaxis
def my_function():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

#Recibe la funcion parametros
def sum_two_values(first_value:int,second_value): #No se puede forzar el tipado
    print(first_value+second_value)

sum_two_values(5,7)
sum_two_values(54754,71231)

#Asi como recibe la funcion parametros, tambien los puede retornar.
def sum_two_values_with_return(first_value,second_value):
    return(first_value+second_value)

my_result=sum_two_values_with_return(10,5) #El return lo almacena en esta variable.
print(my_result)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name(surname="Avila",name="Danilo")

def print_name_with_default(name,surname,alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Danilo","Avila","Conejo")

def print_upper_texts(*texts): #Con el asterisco, nos permite poner un elemento, ya que al principio le decimos "Texts", osea mas de uno, con uno nos bota error.
    for text in texts:
      print(text.upper())

print_upper_texts("Hola","Python","Danilo")

#Clases
#Nos sirve para dozar un objeto de principio a fin.
#Sintaxis
class MyEmptyPerson: #Preferible el nombre de las clases escribirlas asi.
    pass #Nos evita solamente el error. y se deja cuando el codigo no tiene nada.

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self,name,surname): #init y self, nos define que es un constructor de la clase(para establecer un parametro) mas no una funcion.
       self.name=name
       self.surname=surname

my_person=Person("Danilo","Avila")
print(f"{my_person.name} {my_person.surname}")

#Tambien se puede definir de la siguiente manera
class Person:
    def __init__(self,name,surname,alias="Sin alias"): 
        self.full_name=f"{name} {surname} ({alias})"    
    def walk(self): #Para darle acciones u operaciones.
        print(f"{self.full_name} esta caminando")

       
my_person=Person("Danilo","Avila")
print(my_person.full_name)
my_person.walk()
my_other_person=Person("Danilo","Avila","Conejo")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name="Hector el father" #Aqui ya no tiene parametros establecidos de la clase y se puede modifcar como se requiera o querramos.
print(my_other_person.full_name)
my_other_person.walk() #La accion de caminar(Walk) se agrega despues del print.

#Como hacerlo de manera privada
class Person:
    def __init__(self,name,surname,alias="Sin alias"): 
        self.full_name=f"{name} {surname} ({alias})" #Propiedad publica (sin __)
        self.__name=name #Propiedad privada (__)

    def get_name(self): #Esto nos permite acceder al nombre o variable que querramos, mas no modificarlo.
        return self.__name
    
    def walk(self): #Para darle acciones u operaciones.
        print(f"{self.full_name} esta caminando")

my_person=Person("Danilo","Avila","Conejo")

print(my_person.get_name())
my_person.walk()

