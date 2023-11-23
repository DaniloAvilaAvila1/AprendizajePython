#Expresiones Regulares
import re
#Match
#Busca desde el principio de la cadena de texto que hemos designado a las o la variables.
my_string="Esta es la leccion numero 7:La leccion de Expresiones Regulares"
my_other_string="Esta no es la leccion numero 6: Manejo de Richeros"

match=re.match("Esta es la leccion",my_string,re.I)
print(match)
start,end=match.span()
print(my_string[start:end]) #Span es el rango en que se encuentra el texto que se quiere o se ha seleccionado.


match=re.match("Esta no es la leccion",my_other_string)
# if not(match==None): #Otra forma de comprobar el None
if match is not None: #Otra forma de comprobar el None
    print(match)
    start,end=match.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares",my_string))

#Search
#Puede buscar en cualquier parte del texto, no necesariamente desde el principio como el match.
search=re.search("leccion",my_string,re.I)
print(search)
start,end=search.span()
print(my_string[start:end]) #Nos imprime la palabra directo.

#Findall
#Hace un listado dependiendo de las repeticiones de las palabras en las cadena de textos("leccion","leccion".)
findall=re.findall("leccion",my_string,re.I) #La I hace que no diferencia las mayusculas de las minusculas, le da igual.
print(findall)

#Splint
#Separa el texto en el formato que querramos, pero tambien tenemos que colocarlo en la cadena de texto.
print(re.split(":",my_string))

#Sub
#Es para sustituir algunas palabras de la cadena de texto que hemos escrito o seleccionado.
print(re.sub("Expresiones Regulares","Reglas",my_string)) #Aqui ya no se utiiliza el re.I
print(re.sub("leccion|leccion","LECCION",my_string))
print(re.sub("[L|L]eccion","leccion",my_string)) #Otra forma mas simplificada.

#Patrones de Expresiones Regulares
#Sintaxis
pattern=r"[lL]eccion" #Busca leccion con mayuscula o minuscula.
print(re.findall(pattern,my_string))

pattern=r"[lL]eccion|Expresiones"
print(re.findall(pattern,my_string))

pattern=r"[0-9]" #Busca que numeros hay o tiene el texto o cadena de texto.
print(re.findall(pattern,my_string))
print(re.search(pattern,my_string))

pattern=r"\D" #Nos da un listado de todas las letras que se encuentran en la cadena de texto.
print(re.findall(pattern,my_string))

pattern=r"[l].*"
print(re.findall(pattern,my_string))

email="daniloavila@daniloavila.com"
pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9+]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))