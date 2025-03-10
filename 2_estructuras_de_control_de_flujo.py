# -*- coding: utf-8 -*-
"""2_Estructuras_de_Control_de_Flujo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vy7lkPGuoSC9YtAdOvlhM-ytUVCiSeja

# Estructuras de Control de Flujo
Lo primero a decir de las estructuras de control de flujo es que el alcance de la estructura no está controlado por llaves  { } o por palabras reservadas sino por sangría.

La sangría en python es una forma de decirle a un intérprete de Python que el grupo de declaraciones pertenece a un bloque de código en particular.

## LA SENTENCIA CONDICIONAL IF
"""

edad = int(input("Ingrese su edad"))
if edad >= 18:
  print ("puede votar")

"""## CONDICIONALES DOBLES



"""

if condicion:
    codigo
    codigo
else:
    codigo
    codigo

"""Ejemplo condicional doble if-else:"""

edad = int(input("Ingrese su edad"))
if edad >= 18:
  print ("puede votar")
else:
  print("no puede votar")

"""De esta manera, todo lo que esté dentro del respectivo bloque se ejecutará o no de acuerdo con la evaluación de la condición.  Pero lo que esté por fuera al nivel del if, se ejecutará de todos modos."""

edad = int(input("INgrese du edad"))
if edad >= 18:
  print ("puede votar")
else:
  print("no puede votar")
print("fin del programa")

"""### CONDICIONALES MULTIPLES"""

if condicion:
    codigo
    codigo
elif condicion:
    codigo
    codigo
elif condicion:
    codigo
    codigo
else:
    codigo
    codigo

"""En este tipo de estructuras, al encontrarse una condición que se cumpla, las demás no serán evaluadas. El bloque else es opcional, pero de incluirse, siempre debe ser el último.

EJEMPLO DE CONDICIONALES MULTIPLES
"""

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede Votar")
elif edad >= 16:
    print("Puede votar con autorizacion")
else:
    print("No puede votar")

fruta = input("Ingrese una fruta: ")
if fruta == "manzana":
    print("La fruta es manzana")
elif fruta == "pera":
    print("La fruta es pera")
elif fruta == "naranja":
    print("La fruta es naranja")
elif fruta == "platano":
    print("La fruta es platano")
else:
    print("La fruta no es reconocida")

"""CONDICIONALES ANIDADAS

Las condiciones anidadas son condiciones al interior de otras. En este tipo de condiciones, la consistencia en la sangría es la que le permite al intérprete reconocer cuál condición y bloque se encuentra dentro de alguna otra condición o bloque

SINTAXIS **CONDICIONAL ANIDADO**
"""

if condicion:
    codigo
    codigo
    if condicion:
        codigo
        codigo
    else:
        codigo
        codigo

"""Las condiciones anidadas pueden llevar varios niveles de anidamiento y cada condición en si misma puede ser de tipo simple, doble o múltiple

Ejemplo condicional anidada
"""

edad = int (input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad puede votar")

else:
    if edad >= 16:
        print("Usted es adolescente puede votar con autorizacion")
    else:
        print("Usted es menor de edad no puede votar")

"""###Operadores Lógicos

![logicos.png](data:image/png;base64,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)

Puedes identificar qué pasa en el siguiente código con una persona
* a) soltera, linda de 20 años y no buena persona?
* b) buena persona, no linda, soltera y de 45 años?
* c) soltera de 31 años, no buena persona y linda?
* d) casada, de 25 años, linda y buena persona?
"""

estado_civil = input("Digite seu estado civil (Soltero, Casado,): ")
edad = int(input("Digite su edad: "))
buena_persona =  input("Digite si es buena persona (Si, No): ")
linda = input("Digite si es linda (Si, No): ")

if estado_civil == "Casado":
    print("No me caso ni me comprometo")
elif edad <= 30 and linda == "Si":
    print("si Me caso y me comprometo")
else:
    print("SOlo me Comprometo")

"""## Apropiación [Ejercicios Condicionales]

1. En un sistema de automatización industrial, un motor puede estar encendido o apagado. Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente. Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.
"""

motor = input("Pulse 1 para encender el motro: ")

if motor == "0":
    print("Motor Apagado")
elif motor == "1":
    motor_temp = int(input("Digite la temperatura del motor:"))
    print("MOTOR ENCENDIDO")
    if motor_temp >= 80:
        print("Excele la temperatura\n" +"Apagando motor")

"""2.  Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad. Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la matrícula. Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. Si el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o mas, el descuento será del 5%.

Escribir el precio que deberá pagar un estudiante por su matrícula y el valor del descuento.

3. En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para determinar si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe marcar como rechazada y enviar una alerta al operador. Si la pieza cumple con los estándares de calidad, se debe marcar como aprobada y continuar con la producción.  

Realice un programa que lea una entrada binaria en la que los 1s significan estándares de calidad cumplidos y los 0s significan estándares de calidad No cumplidos.  El programa debe rechazar la pieza ante cualquier estándar no cumplido.
"""

numero_de_piezas = int(input("Ingrese el numero de piezas:"))

for p in range (numero_de_piezas):

    pieza = input("Ingrese los estandares de calidad:")
    if len (pieza ) == pieza.count("0") +  pieza.count("1"):
        defectuosos = pieza.count("0")
        print(defectuosos)

        if defectuosos > 0:
            print ("La pieza debe ser recahzada")
        else:
            print ("Pieza Aceptada")
            break

    else:
        print ("Error en la pieza")

"""# LOS CICLOS

## EL CICLO WHILE

El ciclo while es muy sencillo, solo ponemos la condición a evaluar y en su interior el código que se ejecuta mientras la condición se cumpla; manteniendo las reglas de sangría ya conocidas

**sintaxis**
"""

while condicion:
    codigo
    codigo

x = 1
while x <= 5:
    print(x)
    x += 1

color = "rojo"

while color != "verde":
    color = input("Adivina el color: ")
    print ("el color seleccionado fue: ", color )
    break

"""## EL CICLO FOR

**sintaxis**

for **nombre_variable** in iterable_
"""

for varibale in iterable:
    codigo
    codigo

cad = [1,23,5,22,80, "casa", 2.4, "sena", 21]

for x in cad:
    print(x)
    print(type(x))

for x in range(5): #0,1,2,3,4
    print("hola", x+1) # hola 1, hola 2, hola 3, hola 4

"""Es común usar la función range() para generar el iterable deseado, en caso de querer ejecutar el ciclo for un número determinado de veces.

La función range() tiene los siguientes parámetros: range(start, stop, step).

start: (opcional) valor inicial, por defecto 0

stop: (obligatorio) posición final, detiene el ciclo antes de llegar a ella

step: (opcional) incremento en cada paso, por defecto 1

**Ejemplo**
"""

for x in range (1, 11, 2):
    print(x)



for x in range(0,5,1):
    print("hola", x)

for x in range (2,12,2):
    print(x)

for x in range(10):
    print(x)

for x in range(9,0,-1):
    print(x)

for x in range(3,100,3):
    print(x)

nombre = input("Ingrese su nombre: ")
for x in range(1, len(nombre), 2):
    print(x)

"""# break continue

**¿Qué mostraría el siguiente programa?**
"""

print("La instrucción break:")
for i in range(1, 6): #[1,2,3,4,5]
    if i == 3:
        break

    print("Dentro del bucle.", i)

print("Fuera del bucle.")

print("\nLa instrucción continue:")
for i in range(1, 6):#[1,2,3,4,5]
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

"""## Apropiación [Ejercicios Cíclicos]

1. Leer un número y presentar la tabla de multiplicar de ese número entre 1 y 10. Utilizar el siguiente formato de ejemplo:
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
```
"""

def tabla_multiplicar(numero):
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
numero = int(input("Introduce un número: "))
tabla_multiplicar(numero)

"""2. En un partido de fútbol, se ofrece un descuento a los aficionados que depende del estrato y la edad.  Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la boleta.   Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%.  Si  el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o más, el descuento será del 5%.  Determinar el total del dinero recaudado y descontado por las últimas N personas que ingresan al partido."""

total_recaudado = 0
for
   total_recaudado = total_recaudado + pago

def calcular_descuento(estrato, edad, precio_boleta):
  """Calcula el descuento según el estrato y la edad."""
  if estrato == 1:
    if edad < 18:
      descuento = precio_boleta * 0.20
    else:
      descuento = precio_boleta * 0.15
  elif estrato == 2:
    if edad < 18:
      descuento = precio_boleta * 0.10
    else:
      descuento = precio_boleta * 0.05
  else:
    descuento = 0
  return descuento


precio_boleta = float(input("Ingrese el precio de la boleta: "))
N = int(input("Ingrese el número de personas que ingresaron al partido: "))


total_recaudado = 0
total_descontado = 0

for i in range(N):
  estrato = int(input(f"Ingrese el estrato de la persona {i+1}: "))
  edad = int(input(f"Ingrese la edad de la persona {i+1}: "))

  descuento = calcular_descuento(estrato, edad, precio_boleta)

  total_recaudado += precio_boleta
  total_descontado += descuento

print(f"Total recaudado: {total_recaudado:.2f}")
print(f"Total descuento: {total_descontado:.2f}")

"""3.  Leer un password de ingreso a un programa y mostrar el mensaje de bienvenida si es correcto. Mientras no lo sea, debe mostrar el mensaje de Password incorrecto. El programa debe terminar automáticamente al quinto intento fallido."""

password = input("Coloque su contraseña")
password_correcto = " ",password
intentos = 0

while intentos < 5:
  password_ingresado = input("Ingrese su contraseña: ")
  if password_ingresado == password_correcto:
    print("¡Bienvenido!")
    break
  else:
    print("Contraseña incorrecta. Intente de nuevo.")
    intentos += 1
 


 
if intentos == 5:
  print("Demasiados intentos fallidos. Acces denegado.")