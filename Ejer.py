
#creación de listas vacias 
lista_emp= []
lista_emp2= []
comparacion = []

def name_emp():
    arch = estab_archivo("Escritorio/empleados.txt", "a")
    empl = input("Ingrese Porfavor Su Nombre: ")   
    dia1 =input("Dia 1:") 
    dia2 =input("Dia 2:")
    dia3 =input("Dia 3:")
    dia4 =input("Dia 4:")
    dia5 =input("Dia 5:")
    lista_emp.append(empl), lista_emp.append(dia1), lista_emp.append(dia2), lista_emp.append(dia3), lista_emp.append(dia4), lista_emp.append(dia5)
    #print(lista_emp, "lista 1 ")
    arch.write( str(empl)+ '\n' ) 
    arch.close()

def name_emp2():
    arch = estab_archivo("Escritorio/empleados.txt", "a")
    print("Ingrese los Datos del Siguiente Empleado")
    empl2 = input("Ingrese Porfavor Su Nombre: ") 
    print("Ingrese Sus Horarios de la semana ej: MO10: 00-12: 00:")  
    dia1 =input("Dia 1:") 
    dia2 =input("Dia 2:")
    dia3 =input("Dia 3:")
    dia4 =input("Dia 4:")
    dia5 =input("Dia 5:")
    lista_emp2.append(empl2), lista_emp2.append(dia1), lista_emp2.append(dia2), lista_emp2.append(dia3), lista_emp2.append(dia4), lista_emp2.append(dia5)
    #print(lista_emp2, "lista 2")
    arch.write( str(empl2)+ '\n' ) 
    arch.close()


def comparar_horario():
    con = 0
    for i in lista_emp:
        if i in lista_emp2:
            con = con + 1
            comparacion.append(i)
    if len(comparacion) > 0:
        for i in comparacion: print( '%s' % i)    
        print ('Los dias en comun son:', lista_emp[0],'-', lista_emp2[0],':', con)
    else:
        print ('No existe ningun elemento igual en las listas')


def estab_archivo(ruta, permiso):
    archivo = open(ruta,permiso)
    return archivo

def sol_num_entero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Intruduzca la opción que desee: "))
            correcto=True
        except ValueError:
            print('Error, ingrese una opción correcta')
    return num

salir = False
opcion = 0

while not salir:

    print ("1. Ingreso de Empleado y Horario")
    print ("2. Comparación de Horario")
    print ("3. Salir")
    print ("Elige una opcion")
    opcion = sol_num_entero()
    if opcion == 1:

        name_emp()
        name_emp2()


    elif opcion == 2:
        comparar_horario()
        
        
    elif opcion == 3:
        salir = True
        
    else:
        print ("Introduce un numero entre 1 y 2 o 3 para Salir")   
    print ("Fin")
