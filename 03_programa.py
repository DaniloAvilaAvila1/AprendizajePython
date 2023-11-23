#Cambiar tuplas a listas
#Tambien puede ser en viceversa.
#Sintaxis
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)    
fruits = tuple(fruits)
print(fruits)   
print(type(fruits)) 
print(fruits[0])

#Sets 
#sintaxis
my_set=set()
my_other_set={}

print(type(my_set))
print(type(my_other_set)) #Nos dice que inicialmente es un diccionario.

my_other_set={"Danilo","Avila",20}
print(type(my_other_set))

#Añadimos un elemento al set
#El set no es una estructura ordenada
#El set no permite elementos repetidos
my_other_set.add("Conejo")
print(my_other_set)

print("Avila" in my_other_set)
print("Avilaa" in my_other_set)

my_other_set.remove("Avila")
print(my_other_set)

#Unimos los sets
my_set={1,2,3,4}
my_new_set=my_other_set.union(my_set)
print(my_new_set)
my_new_set=my_other_set.union({"Aprendo","Python"}) #Unimos de manera directa.
print(my_new_set)

#Convertimos el set a lista
my_list=list(my_new_set)
print(my_list[0]) #A diferencia del set, en la lista se puede verificar en que posicion se encuentran sus elementos.
print(type(my_list))
#Convertimos la lista a set
my_new2_set=set(my_list)
print(type(my_new2_set))

print(my_new_set.difference(my_other_set))

#Diccionarios:
#Sintaxis
my_dict=dict()
my_other_dict={}

my_other_dict={"Nombre":"Danilo","Apellido":"Avila","Edad":35,1:"Python"}
print(my_other_dict)
print(type(my_other_dict))

my_dict={"Nombre":"Danilo",
         "Apellido":"Avila",
         "Edad":35,
         "Lenguajes":{"Python","Swift","Kotlin"},
          1:1.77
        }
print(my_dict) #Imprimimos un diccionario con un set dentro.
print(my_other_dict)

#Agregamos un elemento al diccionario
print(my_dict["Nombre"]) #Invocamos un elemento del diccionario
my_dict["Nombre"]="DAAAA" #Reemplazamos el nombre anterior, por el escrito en esta linea de codigo.
print(my_dict["Nombre"])

#Agregamos un nuevo campo al diccionario
my_dict["Carrera_Universitaria"]="Ing.Electronica_y_Telecomunicaciones"
print(my_dict)
del my_dict["Carrera_Universitaria"] #De esta menra utilizamos el del para eliminar un elemento especificado
#ya que si no especifico, elimina toda la variable como tal.
print(my_dict)

#Comprobamos si esta la variable en el diccionario
print("Avila" in my_dict) #Nos da falso ya que verifica lo que es la premisa mas no el resultado.
print("Nombre" in my_dict)

#Jugando con las funciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list=["Nombre",1,"Piso"]

my_new_dict=dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict=dict.fromkeys(("Nombre",1)) #Creamos diccionarios nuevos sin valores.
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict,("Danilo","Avila")) #Repite todos los valores en las claves que son las premisas.
print(my_new_dict) #Con la funcion fromkeys no se puede asignar valores a cada uno de las claves, simplemente los repite.

#Convirtiendo el diccionario en.......
my_values=my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))







