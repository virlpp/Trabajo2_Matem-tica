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
print("Bienvenido al programa de análisis de años de nacimiento.")

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
                print("Saliendo del programa...")
                opcion = False
            else:
                print("Continuando con el programa...")
                opcion = True #Se mantiene la ejecución del programa