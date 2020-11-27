#Funcion suma
def suma():
    print("\n\t¡Muy bien, elegiste la suma!\n")
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))

    suma = num1 + num2

    print(f"\nEl resultado de la suma es: {suma}\n")
#--------------------------------------------------------------------

#Funcion resta
def resta ():
    print("\n\t¡Muy bien, elegiste la resta!\n")
    num3 = float(input("Introduce el primer numero: "))
    num4 = float(input("Introduce el segundo numero: "))
    
    resta = num3 - num4

    print(f"\nEl resultado de la resta es: {resta}\n")
#--------------------------------------------------------------------

#Funcion division
def division():
    print("\n\t¡Muy bien, elegiste la division!\n")
    num5 = float(input("Introduce el primer numero: "))
    num6 = float(input("Introduce el segundo numero (El numero debe ser diferente de cero): "))

    if (num6 != 0):
        division = num5/num6
        print(f"\nEl resultado de la division es: {division}\n")
    else:
        print("\nLo sentimos, un numero no es divisible entre cero\n""Si quieres volver a intentarlo vuelve a ejecutar el programa\n")
#--------------------------------------------------------------------

#Funcion multiplicacion
def multiplicacion():
    print("\n\t¡Muy bien, elegiste la multiplicacion!\n")
    num7 = float(input("Introduce el primer numero: "))
    num8 = float(input("Introduce el segundo numero: "))

    multiplicacion = num7 * num8

    print(f"\nEl resultado de la multiplicacion es: {multiplicacion}\n")
#--------------------------------------------------------------------

#Cuerpo del programa
print("--------------------------------------------------------------------")
print("\t\tBienvenido a este nuevo programa\n" "\tEn esta ocasion crearemos una calculadora simple")
print("--------------------------------------------------------------------")

print("\nDejame preguntar: ¿Que operacion deseas realizar?")
opcion = input("\nSuma\n""Resta\n""Division\n""Multiplicacion\n""\nelige: ")

if (opcion == "Suma" or opcion == "suma"):
    suma()
elif(opcion == "Resta" or opcion == "resta"):
    resta()
elif(opcion == "Multiplicacion" or opcion == "multiplicacion"):
    multiplicacion()
elif(opcion == "Division" or opcion == "division"):
    division()

print("--------------------------------------------------------------------")
print("\t\tGracias por usar nuestro programa")
print("--------------------------------------------------------------------")