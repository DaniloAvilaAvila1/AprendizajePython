#Lambdas
#Son como funciones, pero anonimas(no tienen nombre.)
#Sintaxis
sum_two_values=lambda first_value,second_value: first_value + second_value
print(sum_two_values(2,4))

multiply_values=lambda first_value,second_value:first_value*second_value-3
print(multiply_values(2,4))

#Lambda dentro de una funcion
def sum_three_values(value):
    return lambda first_value,second_value:first_value+second_value+value
print(sum_three_values(5)(2,4))

#Funciones de orden superior
#Son funciones que hacen cosas con funciones dentro
#Sintaxis
def sum_one(value):
    return value+1
def sum_five(value):
    return value+5
def sum_two_values_and_add_values(first_value,second_value,f_sum): #f_sum se entiende como una funcion.
    return f_sum(first_value+second_value)
print(sum_two_values_and_add_values(5,2,sum_one))
print(sum_two_values_and_add_values(5,2,sum_five))

#Closures
#Retorna una funcion
def sum_ten(original_value):
    def add(value):
        return value+10+original_value
    return add

add_closure=sum_ten(5)
print(add_closure(5))
print((sum_ten(5))(1))

#Funciones de orden superior que ya existen en el propio lenguaje(python.)
numbers=[2,5,10,21,3,30]
#Map
#Esta funcion predeterminada, recorre todos los valores y modifica su valor como querramos.
def multiply_two(number):
    return number*2

print(list(map(multiply_two,numbers)))
print(list(map(lambda number:number*2,numbers))) #Define una operacion de manera mas rapida y sencilla.

#Filter
#Esta funcion predeterminada, recorre todos los valores y verifica su veracidad o falsedad, mediante la condicion que se le da o que querramos.
def filter_greater_that_ten(number):
    if number>10:
        return True
    return False

print(list(filter(filter_greater_that_ten,numbers)))
print(list(filter(lambda number: number>10,numbers))) #Definida con lambdad de manera mas corta.

#Reduce
def sum_two_values(first_value,second_value):
    return first_value+second_value




