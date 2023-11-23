#Condicionales
#Ejecución condicional: se ejecutará un bloque de una o más declaraciones si una determinada expresión es verdadera
#Ejecución repetitiva: un bloque de una o más declaraciones se ejecutará repetitivamente siempre que una determinada expresión sea verdadera. En esta sección, cubriremos las declaraciones if , else y elif . Los operadores lógicos
#Y de comparación que aprendimos en las secciones anteriores serán útiles aquí.

#Sintaxis
#La condicion tiene que ser verdadera, si es falsa el print no se ejecuta.
my_condition=False

if my_condition: # Es lo mismo que if my_condition==True.
    print("Se ejecuta la condicion del if")

print("La ejecucion continua")

my_condition=5*2

if my_condition==10:
    print("Se ejecuta la condicion del segundo if")

print("La ejecucion continua")

if my_condition>=10:
    print("Se ejecuta la condicion del tercer if")

print("La ejecucion continua")

#Ahora utilizamos el else
#Agregamos una condicion mas
if my_condition>10 and my_condition<20:
    print("Es mayor que 10 y menor que 20")     
else: #Sino
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

#Ahora utilizamos el elif
if my_condition==10:
    print("Se ejecuta la condicion del segundo if")
if my_condition>10 and my_condition<20:
    print("Es mayor que 10 y menor que 20")
elif my_condition==25:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto que 25")

print("La ejecucion continua")

my_string=""

if not my_string:
    print("My cadena de texto es vacia")

if my_string=="Mi cadena de textoooooooooo":
    print("Estas cadenas de texto coinciden")

print("La ejecucion continua")

#Bucles/Loops/Ciclos.
#Sintaxis
my_condition_1=0

while my_condition_1<10:
    print(my_condition_1)
    my_condition_1 +=2 # Sin esta instruccion, el bucle seria infinito.
else: #Es opcional.
    print("Mi condicion es mayor o igual que 10")


print("La ejecucion continua")  


while my_condition_1<20:
    my_condition_1 +=1
    if my_condition_1==15:
       print("Mi condicion es 15")
       break #Con esto paramos el bucle en el valor que querramos.
    print(my_condition_1)

print("La ejecucion continua")

#For
#Un bucle for nos sirve para integrar, un listado de elementos.
my_list=[35,24,62,52,30,30,17]
for element in my_list:
    print(element)



