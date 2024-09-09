#Captura de datos (Formulario) y definición de variables
nombre = input ("Cual es tu nombre: ")
apellidopat = input ("Y tu apellido paterno: ")
apellidomat = input ("Tu apellido materno: ")
edad = int(input ("Cual es tu edad: "))
peso = float(input("Cual es tu peso: "))
estatura = float(input("Cuanto mides en metros: "))

#Calculo de IMC
imc = float(peso / estatura**2)

# Impresión de datos
print ("Hola " + nombre + " " + apellidopat + " " + apellidomat )
print ("tienes " + str(edad) + " años")
print ("pesas " + str(peso) + " Kilogramos y mides " + str(estatura) + "metros" )
print ("tu indice de masa corporal es de: " + f"{imc:.2f}")