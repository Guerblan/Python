import math
#Constantes
'''
PRECIO = 45
print(PRECIO)
PRECIO=12
print(PRECIO)

#----------------------------------------Tipos de datos----------------------------------------------

#1. Pedir por teclado el nombre y la edad de una persona y mostrar en pantalla un mensaje
#similar a: “Te llamas _____ y tienes ___ años.”
#2. Ampliar el ejercicio anterior pidiendo la altura de la persona.
#3. Pedir por teclado el radio de un cÌrculo y mostrar su longitud y su area


name=input('Dime tu nombre')
#siempre tengo que cambiar el tipo en función de lo que me pida ya que input genéricamente es un string
edad=int(input('Dime tu edad'))
print('Te llamas ' + name + ' y tienes ' + edad + ' años')
altura=float(input('Dime tu altura'))
print('tu altura es '+ altura)
radio=float(input('Dime el radio de un círculo'))
#Requiere importar math
longitud= 2*math.pi*radio
area=math.pi*radio**2
#Necesitamos poner la f al principio para que la variable dentro de {} de el valor
print(f'El radio del cículo es {radio} ,su longitud es {longitud} y su area {area}')

#-------------------------------ENTEROS------------------------------------------------


# Realiza el c·lculo 23 entre 10 y muestra el cociente y el resto. Verifica el resultado. 

cociente,resto = divmod(23,10)
print(cociente,resto)

#Pide dos n˙meros por teclado y muestra el cociente y resto. Muestra tambiÈn la divisiÛn
#entera. 
num1 = int(input('Introduce un primer número'))
num2 = int(input('Introduce un segundo número'))
cociente,resto=divmod(num1,num2)
print(cociente,resto)
#Aqui´bastaría con haber reutilizado cociente ya que YA es una división entera
div_entera=num1//num2
print(div_entera)


#-----------------------------REALES------------------------------------------------

#• Realiza un producto entre un n˙mero entero y otro decimal. Visualiza el resultado. øSe
#puede?
num_entero=3
num_decimal=0.2
print(num_entero*num_decimal)

#• Realiza las operaciones anteriores y muestra su contenido.
x = 0.1 + 0.2 # 0.30000000000000004
print(x)
x = 2e-3
print(x)

#• Muestra el resultado de la operaciÛn 2.3 + 1.1.
resultado=2.3 + 1.1
print(resultado)
#• Muestra el resultado de la operaciÛn anterior usando round. FÌjate en los diferentes
#resultados.
print(round(resultado))

#• Muestra el resultado de la operaciÛn 2.5 + 1.1.
resultado_nuevo=2.5 + 1.1
print(resultado_nuevo)
#• Muestra el resultado de la operaciÛn anterior usando round. FÌjate en los diferentes
#resultados.
print(round(resultado_nuevo))
#• FÌjate en los redondeos obtenidos y analiza cÛmo funcionan. 
#Aquí lo que me quiere decir es que Round redondea al más cercano,pero si acaba en .5 redondea
#redondea al  par más cercano!!!Por ej 3,5 redondearía a 4 y 2,5 a 2

#---------------------------BOOLEAN------------------------------------------
# ¿Es posible imprimir un valor booleano?
bool = 1
print(bool)

# Pide dos números enteros por teclado. Muestra en pantalla True si el primer número es
# mayor que el segundo y false en caso contrario. No se puede usar la sentencia if. 
num1=int(input('Dame un primer número'))
num2=int(input('Dame un segundo número'))
#Aqí comprobamos que una condición devuelve un booleano
resultado=(num1>num2)
print(resultado)

#-----------------------------------CADENAS-----------------------------------------
#1. Pide una cadena por teclado y muestra su longitud.
cadena = input('Escribe una cadena')
print(len(cadena))
#2. Pide una cadena por teclado y concaténala con si misma mostrando el resultado.
cadena = input("Introduce una cadena: ")
print(cadena + cadena)

#3. Pide una cadena por teclado y determina si tiene la subcadena hoy
cadena = input("Introduce una cadena: ")
print(cadena.find("hoy") != -1)

#4. Pide una cadena por teclado y reemplaza todas las apariciones de la letra z por c
cadena = input("Introduce una cadena: ")
print(cadena.replace('z','c'))

#5. Pide una cadena por teclado y determina cuántas vocales tiene.
cadena = input("Introduce una cadena: ")
print(cadena.count('a'))
print(cadena.count('e'))
print(cadena.count('i'))
print(cadena.count('o'))
print(cadena.count('u'))

#6. Pide una cadena por teclado y determina cuántas veces aparece la a y cuántas veces
#aparece la i
cadena = input("Introduce una cadena: ")
print(cadena.count('a'))
print(cadena.count('i'))

#7. Pide una cadena por teclado y muéstrala con todas las letras en mayúsculas.
cadena = input("Introduce una cadena: ")
print(cadena.upper())

#8. Pide una cadena por teclado y muéstrala con todas las letras en minúsculas.
cadena = input("Introduce una cadena: ")
print(cadena.lower())

#9. Pide una cadena por teclado y muéstrala en rojo y negrita.
cadena = input("Introduce una cadena: ")

print("\033[31m\033[1m" + cadena + "\033[0m")

#10. En la cadena “Seremos capaces de ir muy lejos” muestra la posición y la última de la letra s
cadena = "Seremos capaces de ir muy lejos"

print(cadena.find('s'))
print(cadena.rfind('s'))

#11. Pide una cadena por teclado y muéstrala al revés. 
cadena = input("Introduce una cadena: ")
print(cadena[::-1])

#---------------------------------------------OPERADORES-------------------------------------------------
#-----------------------------------------CONVERSIÓN DE TIPOS----------------------------------------
#Pide por teclado la edad de una persona.
edad = input('Dime tue edad')
edad = int(edad)
# Muestra la edad leída sumándole 3.
print(edad + 3)
# ¿Has obtenido un error? ¿A qué se debe? ¿Cómo se soluciona?
#No lo he obtenido porque previamente había cambiado el tipop
# Pide el nombre de una persona, su edad, su estatura y muestra un mensaje en pantalla con
#toda esa información. Debes mostrar la información con un formato “agradable”.
# Pide un número decimal (float) por teclado y muéstralo en pantalla.
# Pide un número decimal (float) por teclado transfórmalo en entero y muéstralo por pantalla.

#Ejecuta el programa dos veces, la primera introduce 12.3 y la segunda 12.7. ¿La
#transformación a entero trunca o redondea? 
'''
#--------------------------------FUNCIONES INTEGRADAS----------------------------------------------------
numeros = [44, 8, 15, 6, 23, 43]
#Haz una tabla con la utilidad de cada una de las funciones.
#2. Muestra el menor valor de la lista.
print(min(numeros))
#3. Muestra el mayor valor de la lista.
print(max(numeros))
#4. Muestra la suma de todos los números de la lista.
print(sum(numeros))
#5. Muestra cuántos elementos tiene la lista.
print(len(numeros))
#6. Calcula la media de todos los elementos de la lista.
print(sum(numeros)/len(numeros))
#7. Calcula la media de todos los elementos de la lista y muestra el resultado solo con dos
#decimales.
media=sum(numeros)/len(numeros)
print(round(media,2))
#8. Muestra los elementos de la lista ordenados ascendentemente. La lista inicial no debe
#cambiar.
print(sorted(numeros))
#9. Ordena los elementos de la lista y muéstralos.
numeros.sort
#10. ¿Qué diferencia hay entre los dos ejercicios anteriores?
#sorted sirve para ordenar para algo puntual,una impresió por ej.sotr() sirve para esditar la lista original.Cambia.
#11. Crea una lista de 5 números con range y muéstrala.
lista = list(range(5))
print(lista)
#12. Crea una lista de los 10 primeros números pares usando range y muéstrala.
lista_par = list(range(0,20,2))
print(lista_par)
#13. Crea una lista con los siguientes animales: zorro, elefante, gallina
lista_animales=["zorro","elefante","gallina"]
#14. Ordena alfabéticamente la lista.
print(sorted(lista_animales))
#15. Redondea el número 7.856 a dos decimales. 
num = 7.856
print(round(num,2))