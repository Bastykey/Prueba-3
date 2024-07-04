import csv 
from datetime import date


habitaciones=[]
def total_habitaciones(habitaciones):
   for i in range (1,40):
      print(f"Hay N°{i+1} en el hotel")
    
      

def reservar_habitacion(documentos_personas):
    try:    
        nombres=input("Ingrese el Nombre  y el apellido de la persona responsable:")
    except   ValueError:
        print("Error: Recuerde ingresar correctamente los datos")
        rut=int(input("Ingrese el rut :"))
    try:    
        fecha=int(input("Ingrese fecha de salida: "))
        hora=int(input("Ingrese hora salida: "))
    except ValueError:
        print("Error: Recuerde ingresar correctamente los datos")
        print("Hola ")
        datos_usuario={
        "NOMBRE":nombres,
        "RUT": rut,
        "FECHA" : fecha,
        "HORA": hora
    }
    documentos_personas.append(datos_usuario)
    if  not documentos_personas:
        print("¡No hay datos ingresados!")
print("Agregado con exito :)")

def buscar_habitacion():
 if  not documentos_personas:
    print("¡No hay datos ingresados!")


def guardar_informacion(documentos_personas):
    with open('habitaciones.csv','w') as archivo_csv:
        writer = csv.writer(archivo_csv)
    writer.writerows([[]])


documentos_personas=[]
while True:
    print("**********************************")
    print("*GESTION DE HABITACIONES DEL HOTEL*")
    print("1. Reservar Habitacion ")
    print("2. Buscar Habitacion")
    print("3. Ver estado de Habitacion ")
    print("4. Ventas diarias")
    print("5. Guardar informacion ")
    print("**********************************")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("¿Que habitacion desea elegir? \n 1) Habitacion estandar $30.000 \n 2) Habitacion Regular $60.0000 \n 3)Habitacion premium $100.000\n **Recuerde que cada valor corresponde al valor diario de la habitacion** \n")   
        seleccion=int(input(""))
        if seleccion == 1:
            print("¡Ha elegido una habitacion estandar!")
            print("Ingrese sus datos para reservar la habitacion")
            reservar_habitacion()
            
            print("Estas son las habitaciones disponinbles")
            total_habitaciones()
            s=int(input("¿cual desea reservar?"))
            
        if seleccion == 2:
            print("¡Ha elegido una habitacion regular!")
        if seleccion == 3:
            print("¡Ha elegido una habitacion premium!")
    else:
        print("opcion invalida")


    if opcion == 2:
        total_habitaciones()
        
        

    if opcion==3:
       buscar_habitacion()