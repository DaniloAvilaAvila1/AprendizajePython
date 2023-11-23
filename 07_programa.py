#Datos
#Consiste en la fecha y hora
from datetime import datetime
#Creando una fecha
now=datetime.now() #Nos va a inicianilizar un objeto de tipo datetime.

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
#Nos da la representacion unica de un tiempo.
timestamp=now.timestamp()

print(timestamp)

#Creando fecha y hora
#Lo minimo que se necesita es el año, el mes y el dia, ya que si no, nos da error.
year_2023=datetime(2023,1,1) #La hora, minuto y segundo se nos define como cero, ya que no la ponemos.

print_date(year_2023)
#Time nos permite trabajar con diferentes funciones en base al tiempo.
#Time es un objeto que no tiene nada a diferencia de lo anterior(timestamp).
#Agrupa solo horas, minutos y segundos.
from datetime import time

currente_time=time(21,6,0)
print(currente_time.hour)
print(currente_time.minute)
print(currente_time.second)

#Agrupa solo fechas
from datetime import date 

current_date=date.today() #Asi puedo definirlo todo de hoy (fechas).
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date=date(2023,10,6) #Aqui definimos uno por uno.
print(current_date.year)
print(current_date.month)
print(current_date.day)

#Modificando fechas
current_date=date(current_date.year,current_date.month + 1,current_date.day)

print(current_date.month)
#now es el momento de ahora (nos da la fecha y hora actual o en el moneto en que se ejecuta.)
diff=year_2023-now
print(diff)
diff=year_2023.date()-current_date
print(diff)
print(year_2023.time())

#Trabajando con el timedelta
from datetime import timedelta
#Esto es para trabajar con franjas de fechas
start_timedelta=timedelta(200,100,100,weeks=10)
end_timedelta=timedelta(300,100,100,weeks=13)
print(end_timedelta-start_timedelta)
print(end_timedelta+start_timedelta)

#Listas de comprension
my_original_list=[0,1,2,3,4,5,6,7]
print(my_original_list)

my_list=[i +1 for i in range(8)] #Transformando la lista en otra lista
print(my_list)

my_range=range(8)
print(list(my_range))

#Probamos con funciones
def sum_five(number):
    return number +5

my_list=[sum_five(i) for i in range(8)]
print(my_list)