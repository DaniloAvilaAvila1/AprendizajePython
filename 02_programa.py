#Segunda parte del curso de Python
#Listas
#Sintaxis
my_list=list()
my_other_list=[]

print(len(my_list))

my_list=[35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))
print(my_list[0]) #Selecciona un objeto de la lista.

#En una lista, se puede poner cualquier tipo de dato.

my_other_list=[35,1.77,"Danilo","Avila"]
print(type(my_other_list))
print(my_other_list.count(35)) #El count nos ayuda a contar elementos de la propia lista.

#Desembalaje de elementos de una lista
list = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = list

print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']


countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *rest, es = countries #Podemos definirlo de la siguiente manera tambien
print(gr)
print(fr)
print(bg)
print(sw)
print(rest)
print(es)

#Concatenamos las listas
print(my_list+my_other_list+countries)

#Cortar elementos de una lista
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] #Se puede escribir de ambas maneras por eso se les deja el mismo nombre de variables.
all_fruits= fruits[0:] 
orange_and_mango = fruits[1:3] 
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]
print(orange_and_lemon)

#Comprobacion de elementos de una lista
does_exist = 'banana' in fruits
print(does_exist) 
does_exist = 'lime' in fruits
print(does_exist)  

#Agregar elementos de una lista
#Sintaxis
#list=list()
#list.append(item)
#solo para agregar elementos al final de una lista.
fruits.append('apple')
print(fruits)           
fruits.append('lime') 
print(fruits) 

#Insertamos elementos a la lista en el orden que querramos.
fruits.insert(1,"apple")
print(fruits)
fruits.insert(2,"lime")
print(fruits)

#Eliminar elementos de una lista
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits.reverse() #le da vuelta a la lista
print(fruits)
del fruits[0]
print(fruits)       
del fruits[1]
print(fruits)      
del fruits[1:3]     
print(fruits)
#El elemento pop elimina lo ultimo de la lista si no se especifica.       
fruits.pop()
print(fruits)      
fruits.pop(0)
print(fruits)   

my_list.sort()
print(my_list) #Ordena la lista de menor a mayor en caso de numeros 
#Y en orden alfabetico en caso de palabras
print(my_list[1:4]) #Nos da el elemento que tenemos entre esos numeros

#Borrar por completo los elementos de una lista
fruits.clear()
print(fruits)
#Copiamos la lista
my_new_list=fruits.copy()
print(my_new_list)

#Tuplas
#A diferencia de las listas, no son modificables.
#Sintaxis
my_tuple=tuple()
my_other_tuple=()

my_tuple=(35,1.77,"Avila","Danilo")
print(my_tuple)
print(type(my_tuple))

print(my_tuple.count("Avila"))
print(my_tuple.index("Avila")) #Nos dice cual es el orden de la variable que se selecciona.

#Dividimos una tupla
fruits = ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[1:3] #No incluye el item o elemento 3.
orange_to_the_rest = fruits[1:]
print(orange_mango)









