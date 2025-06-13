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


