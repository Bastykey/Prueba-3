import csv 
from datetime import date
habitaciones=[]
pisos=[1,2,3,4]
def total_habitaciones():
   for i in pisos (0,10):
      print(f"Hay N°{i+1} en el piso{pisos[1]}")
      pisos=pisos+1
      

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
    
    



def ver_estado_habitacion():




#def ventas_diarias():



def guardar_informacion():

with open('habitaciones.csv', 'w') as archivo_csv:
   writer = csv.writer(archivo_csv)
   writer.writerows([[]])
#date.now().strftime()



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