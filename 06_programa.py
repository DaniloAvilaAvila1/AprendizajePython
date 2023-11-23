#Manejo de errores
#Estos pueden producir que el programa se detenga o la aplicacion muera, por eso es importante saber como manejarlos o solucionarlo.
numberOne=5
numberTwo=1
numberTwo="1"
try:
  print(numberOne+numberTwo)
  print("No se ha producido error")
except:
  print("Se ha producido un error")
else: #Opcional
  #Esto no se ejecuta si se produce una excepcion.
  print("La ejecucion continua correctamente")
finally: #Opcional
  #Se ejecuta siempre
  print("La ejecucion continua")


#Excepciones por type
#Aqui podemos verificar que tipo de error se produce.
try:
  print(numberOne+numberTwo)
  print("No se ha producido error")
except ValueError:
  print("Se ha producido un ValueError")
except TypeError:
  print("Se ha producido un TypeError")

#Captura de la informacion de la excepcion(Error)
try:
  print(numberOne+numberTwo)
  print("No se ha producido error")
except ValueError as error: #Este error escrito, es un nombre de variable que le damos, a la variable que tiene la informacion del verdadero error como tal.
  print(error)
except Exception as exception: 
  #Controla el error en general, si no es tipo ValueError.
  print(exception)

#Modulos
#Esto es como una libreria
#Sintaxis
#La nomenclatura de los modulos python no la acepta con numeros (02_programa).
#Tambien tenemos establecidos modulos por defecto de python con ciertas funciones cada uno de ellos.
import module

module.sum(5,3,1)

#Importamos de manera directa y asignamos cualquier nombre a nuestra variable o valor requerido.
from math import pi as PI_VALUE

print(PI_VALUE)