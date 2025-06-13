# Desarrollaremos un programa donde se pida ingresar el DNI (Documento Nacional de Identidad) de una persona y se harán operaciones con ellos.

# Mensahje de bienvenida
print(" ")
print("-------------------------------------------------------------")
print("Bienvenido al programa de operaciones con DNIs.")
print("A continuación se les solicitará ingresar dos DNIs diferentes.")
print("-------------------------------------------------------------")
print(" ")


#Se solicita un primer DNI al usuario y se valida que tenga 8 dígitos numéricos.
# y el conjunto de dígitos del 0 al 9
DNI = input("Ingrese un DNI: ")
while not DNI.isdigit() or len(DNI) != 8:
    print("El DNI debe tener 8 dígitos numéricos.")
    DNI = input("Ingrese su DNI: ")

#Se solicita un segundo DNI al usuario y se valida que tenga 8 dígitos numéricos.
DNI2 = input("Ingrese otro DNI: ")
while not DNI2.isdigit() or len(DNI2) != 8:
    print("El segundo DNI debe tener 8 dígitos numéricos.")
    DNI2 = input("Ingrese otro DNI: ")

# Se valida que el segundo DNI sea diferente al primero
if DNI2 != DNI:
     
     print(" ")
     print("-------------------------------------------------------------")  
     print("Operaciones con los DNIs ingresados:")
     print("-------------------------------------------------------------")   

    #Generación automática de los conjuntos de dígitos únicos
     conjunto_digitos = set(DNI) # Convertimos el DNI en un conjunto de dígitos únicos
     print(f"Conjunto de dígitos únicos: {conjunto_digitos}")

    #Calculo de la unión de los conjuntos de dígitos de ambos DNIs
     conjunto_digitos2 = set(DNI2)  # Convertimos el segundo DNI en un conjunto de dígitos únicos
     union_digitos = conjunto_digitos.union(conjunto_digitos2)  # Unión de los conjuntos
     print(f"Unión de los conjuntos de dígitos: {union_digitos}")    


    # Calculo de la intersección de los conjuntos de dígitos
     interseccion_digitos = conjunto_digitos.intersection(conjunto_digitos2)  # Intersección de los conjuntos
     print(f"Intersección de los conjuntos de dígitos: {interseccion_digitos}")


    # Calculo de la diferencia de los conjuntos de dígitos

     diferencia_digitos = conjunto_digitos.difference(conjunto_digitos2)  # Diferencia de los conjuntos
     print(f"Diferencia de los conjuntos de dígitos: {diferencia_digitos}")


    # Calculo de la diferencia simétrica de los conjuntos de dígitos

     diferencia_simetrica_digitos = conjunto_digitos.symmetric_difference(conjunto_digitos2)  # Diferencia simétrica de los conjuntos
     print(f"Diferencia simétrica de los conjuntos de dígitos: {diferencia_simetrica_digitos}")

     print(" ")
     print("-------------------------------------------------------------")  
     print("Frecuencia de dígitos:")
     print("-------------------------------------------------------------")   


    # Conteo de frecuencia de cada dígito en el primer DNI
     frecuencia_digitos = {digito: DNI.count(digito) for digito in conjunto_digitos}  # Conteo de frecuencia
     print("Frecuencia de cada dígito en el primer DNI:")
     print(" ")
     for digito, frecuencia in frecuencia_digitos.items():
        print(f"Dígito {digito}: {frecuencia} veces")


    # Conteo de frecuencia de cada dígito en el segundo DNI
     print(" ")
     frecuencia_digitos2 = {digito: DNI2.count(digito) for digito in conjunto_digitos2}  # Conteo de frecuencia
     print("Frecuencia de cada dígito en el segundo DNI:")
     print(" ")
     for digito, frecuencia in frecuencia_digitos2.items():
        print(f"Dígito {digito}: {frecuencia} veces")
     print(" ")


     print("-------------------------------------------------------------")  
     print("Suma de dígitos:")
     print("-------------------------------------------------------------")   

    # Suma total de los dígitos del primer DNI
     
     suma_digitos = sum(int(digito) for digito in DNI)  # Suma de los dígitos
     print(f"Suma total de los dígitos del primer DNI: {suma_digitos}")


    # Suma total de los dígitos del segundo DNI
     print(" ")
     suma_digitos2 = sum(int(digito) for digito in DNI2)  # Suma de los dígitos
     print(f"Suma total de los dígitos del segundo DNI: {suma_digitos2}")
     print("-------------------------------------------------------------")
     print("Operaciones finalizadas.")
     print(" ")
     print("////////////////////////////////////////////////////////////////")

else:
    print("Los DNIs ingresados son iguales. Por favor, ingrese dos DNIs diferentes.")


#Funciones


# Esta función recibe cuatro años de nacimiento y cuenta cuántos son impares.
def anio_impar(anios):
     return sum(1 for anio in anios if anio % 2 != 0)


# Esta función recibe cuatro años de nacimiento y cuenta cuántos son pares.
def anio_par(anios):
    return sum(1 for anio in anios if anio % 2 == 0)


# Esta función recibe cuatro años de nacimiento y verifica si alguno de ellos es bisiesto.
def es_bisiesto(anios):
    bisiestos = [anio for anio in anios if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)]
    if bisiestos:
        return f"De los años ingresados, tenemos uno o más años especiales: {bisiestos}. \nComo se ha ingresado un año bisiesto, se finaliza el programa."
    return None

# Esta función finaliza el programa si se ha ingresado un año bisiesto.
def fin_programa(es_bisiesto):
     print("Saliendo del programa...")
     exit()

# Esta función recibe un año de nacimiento y determina a qué grupo generacional pertenece.
def clasificar_generacion(anio_nacimiento):
    if anio_nacimiento >= 2013:
        return "Generación Alfa"
    elif anio_nacimiento >= 1997:
        return "Grupo Z"
    elif anio_nacimiento >= 1981:
        return "Grupo Y (Millennials)"
    elif anio_nacimiento >= 1965:
        return "Grupo X"
    elif anio_nacimiento >= 1946:
        return "Baby Boomers"
    elif anio_nacimiento >= 1928:
        return "Generación Silenciosa"
    else:
        return "Año de nacimiento no válido o anterior a 1928"
        
# Esta función verifica si el año ingresado tiene 4 dígitos.
def longitud_anio(anio):
   return len(str(anio)) == 4  

# Esta función calcula la edad actual de cada año de nacimiento ingresado.
def edad_actual(anios):
    from datetime import datetime
    return [datetime.now().year - anio for anio in anios]  # Calcula la edad actual restando el año de nacimiento al año actual



#------------------ Programa principal ------------------
# Mensahje de bienvenida
print(" ")
print("-------------------------------------------------------------")
print("Bienvenido al programa de análisis de años de nacimiento.")
print("-------------------------------------------------------------")
print(" ")

# Solicitar al usuario los años de nacimiento
opcion = True

while opcion:
    valido = False  # Bandera para verificar si los años son válidos
    while not valido:
        try:
            anio_1 = int(input("Ingrese su año de nacimiento: "))
            anio_2 = int(input("Ingrese el año de nacimiento de un compañero: "))
            anio_3 = int(input("Ingrese el año de nacimiento de otro compañero: "))
            anio_4 = int(input("Ingrese el año de nacimiento de otro compañero: "))
            if all(longitud_anio(anio) for anio in (anio_1, anio_2, anio_3, anio_4)):
                valido = True  # Si todos se ingresan bien, cambiamos la bandera
            else:
                print("Todos los años deben tener 4 dígitos. Por favor, intente nuevamente.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")

        # Validación de los años de nacimiento
        print(" ")
        anios = [anio_1, anio_2, anio_3, anio_4]
        print(f"Nacidos en años impares: {anio_impar(anios)} \nNacidos en años pares: {anio_par(anios)}")

        #Se clasifica cada año
        generacion1 = clasificar_generacion(anio_1)
        generacion2 = clasificar_generacion(anio_2)
        generacion3 = clasificar_generacion(anio_3)
        generacion4 = clasificar_generacion(anio_4)

        #Se verifica si todos pertenecen a la misma generación
        if generacion1 == generacion2 == generacion3 == generacion4:
            print(" ")
            print(f"Todos pertenecen a la misma generación: {generacion1}")
        else:
            print(" ")
            print(f"Las generaciones son diferentes: \nPersona 1: {generacion1}, \nPersona 2: {generacion2}, \nPersona 3: {generacion3}, \nPersona 4: {generacion4}")

        #Mostrar producto cartesiano de los años
        edades = edad_actual(anios)

        producto_cartesiano = [(anio, edad) for anio, edad in zip(anios, edades)]
        print(" ")
        print("Producto cartesiano entre los conjuntos año_nacimiento y edad_actual:")
        for par in producto_cartesiano:
            print(par)

        # Verificar si alguno de los años es bisiesto
        if es_bisiesto(anios):
            print(" ")
            print(es_bisiesto(anios))
            fin_programa(True)
        else: # Si no hay años bisiestos, continuamos con el programa
            opcion = input("Deseas salir del programa? (si/no): ").strip().lower()
            if opcion == 'si':
                print("-------------------------------------------------------------")

                print("Saliendo del programa...")
                opcion = False
            else:
                print("Continuando con el programa...")
                opcion = True #Se mantiene la ejecución del programa
