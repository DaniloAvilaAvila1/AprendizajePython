#Primera parte del curso de Python
# Variables
my_string_variable= "My string variable"
print(my_string_variable)

my_int_variable=5
print(my_int_variable)

#transformacion de una variable entera a una cadena de texto.
my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
#########

my_bool_variable=False
print(my_bool_variable)

#Concatenacion de variables en un print.
print(my_string_variable,my_int_variable,my_bool_variable)
############

#Funciones del sistema
print(len(my_int_to_str_variable)) #Cuenta los caracteres de la variable.

#Variables en una sola linea. ¡No abusar de este tipo de sintaxis!
name,surname,alias,age= "Danilo","Avila","Conejo",20
print("Me llamo:",name,surname,"Mi edad es:",age,"Y mi alias es:",alias)

#¿¿Forzamos el tipo de dato??
address:str= "Mi direccion"
address=32
print(type(address))

#Operadores
#Operadores Aritmeticos
print(3+4)
print(10%3)
print(10//3) #Nos da un numero entero de la division, asi sea aproximado.
print(2**3) #Es una potencia

print("Hola"+"Python")
print("Hola"+str(5))
print("Hola" * 5)

my_float=2.5*2
print("Hola"*int(my_float))

#Operadores Comparativos
print(3>4)
print(3<4)

print("Hola">"Python") #Compara en ordenacion alfabetica, tiene en cuenta las mayusculas y minusculas.
print("Hola"<"Python")

#Operadores logicos
print(3>4 and "Hola">"Python")
print(3<4 or "Hola"<"Python")
print(3<4 or ("Hola"<"Python" and 4==4))
print(not(3>4))

#Strings
my_string= "mi string"
my_other_string="mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string+" "+my_other_string)

my_new_line_string="Este es un string\ncon salto de linea" #\n Lo que hace es ponerlo en parrafos diferentes.
print(my_new_line_string)
#Si queremos desaparecer los saltos de linea o tabulacion, ponemos \\ de esta manera \\t
#Asi ya no tiene efecto.
my_tab_string="\tEste es un string con tabulacion"
print(my_tab_string)

#Formateo
name,surname,age="Danilo","Avila",20

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age)) #Con el %d hacemos mas seguro nuestro codigo, ya que si ingresamos un dato que no sea un numero, bota error.

print(f"Mi nombre es {name} {surname} y mi edad es {age}") #La f formatea e infiere el valor de las variables entre los corchetes.

#Desempaqueado de caracteres
language= "Python"
a,b,c,d,e,f=language
print(a)
print(b)

#Division
language_slice=language[1:3]
print(language_slice)

language_slice=language[-2]
print(language_slice)

#Reverse
reversed_language=language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize()) #Pone en mayuscula la primera letra
print(language.upper()) #Pone todo en mayusculas
print(language.count("t")) #Cuenta la letra que queremos
print(language.isnumeric()) #Evalua si es un numero
print(language.lower()) #Toda la palabra en minusculas
#Si queremos comprobar que esten en minusculas o mayusculas, ponemos un is como prefijo
#Ejm: isupper o islower.
print(language.startswith("py")) #Nos dice si es verdadero o falso con que empieza la palabra
#Diferenciando las mayusculas con las minusculas.

