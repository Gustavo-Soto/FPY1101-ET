from random import*
import csv
import os
import time
limpieza_pantalla = 'cls'

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldo = []
sueldo_total = []

def asignar_sueldos(sueldo):
    for asignar in sueldo:
        sueldo = 0
        sueldo = randint(1,100)
        print(asignar)
        return(asignar)
    
def clasificar():
    print(f'sueldo menores a',{},'total: ',{})
    print('Nombre empleado      sueldo')
    print(f'Juan perez',         {})
    print('Maria Garcia',        {})
    print('')
    print(f'Sueldo entre ',{},'y',{})
    print('')
    print(f'sueldos superiores a ',{})
    print(f'total: ',{})
    print('')
    print('Nombre empleado      sueldo')
    print(f'',{})
    print(f'total sueldos: $',{})
    
menu = 1
while menu <= 4:
    try:
        print('1.-Asignar sueldos')
        print('2.-Clasificar sueldos')
        print('3.-Ver estadisticas')
        print('4.-Reporte sueldos')
        print('5.-Salir del programa')
        
        seleccion = int(input('Seleccione su opcion'))
        os.system(limpieza_pantalla)
        time.sleep(2)
        
        if seleccion == 1:
            asignar_sueldos(sueldo)        
            sueldo = [sueldo]
            print(sueldo)
            
        elif seleccion == 2:
            clasificar()
            
        elif seleccion == 3:
            print('')
            
        elif seleccion == 4:
            print('')

        else:
            print('')
            break
    except ValueError:
        print('ingrese valor correcto')
        
print('finalizando programa...')
print('desarrollado por Gustavo SOto')
print('Rut: 18881469-7')
