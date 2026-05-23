
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor

#procedimiento que borre pantalla

def borrar_Pantalla():
   import os
   os.system("cls")
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
   borrar_Pantalla()
   nombre = input("Ingresa tu nombre: ").strip().upper()
   apellidos = input("Ingresa tus apellidos: ").strip().upper()
   print(f"Hola {nombre} {apellidos} bienvenido a la clase de Python")
   
 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre, apellidos):
   borrar_Pantalla()
   print(f"Hola {nombre} {apellidos} bienvenido a la clase de Python")

#funcion3("JOHN", "DOE")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   borrar_Pantalla()
   nombre = input("Ingresa tu nombre: ").strip().upper()
   apellidos = input("Ingresa tus apellidos: ").strip().upper()
   return 
   f"Hola {nombre} {apellidos} bienvenido a la clase de Python"
#resultado = funcion2()
#print(resultado)
 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nombre, apellidos):
   borrar_Pantalla()
   return
   f"Hola {nombre} {apellidos} bienvenido a la clase de Python"

resultado = funcion4("JOHN", "DOE")
print(resultado)

funcion1()
nombre=input("nombres: ").strip().upper()
apellidos= input("apellidos: ").strip().upper()
funcion3(nombre, apellidos)
 
nombre,apellidos=funcion2()



