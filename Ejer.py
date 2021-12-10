
#creation of lists for Employees and Schedules 
lista_emp= []
lista_emp2= []
comparacion = []

def name_emp():
    arch = estab_archivo("empleados.txt", 'a')
    print("New Employee: ")
    empl = input("Input a New Employee: ")   
    dia1 =input("Day 1:") 
    dia2 =input("Day 2:")
    dia3 =input("Day 3:")
    dia4 =input("Day 4:")
    dia5 =input("Day 5:")
    lista_emp.append(empl), lista_emp.append(dia1), lista_emp.append(dia2), lista_emp.append(dia3), lista_emp.append(dia4), lista_emp.append(dia5)
    #print(lista_emp, "lista 1 ")
    arch.write( str(lista_emp)+ '\n' ) 
    arch.close()

def name_emp2():
    arch = estab_archivo("empleados.txt", 'a')
    print("New Employee: ")
    empl2 = input("Input Your Name: ") 
    print("Input your schedule of work, indicating the time and hours  ej: MO10: 00-12: 00:")  
    dia1 =input("Day 1:") 
    dia2 =input("Day 2:")
    dia3 =input("Day 3:")
    dia4 =input("Day 4:")
    dia5 =input("Day 5:")
    lista_emp2.append(empl2), lista_emp2.append(dia1), lista_emp2.append(dia2), lista_emp2.append(dia3), lista_emp2.append(dia4), lista_emp2.append(dia5)
    #print(lista_emp2, "lista 2")
    arch.write( str(lista_emp2)+ '\n' ) 
    arch.close()

#This method compares two lists of employees and shows us the days that the workers have in common.
def comparar_horario():
    arch = estab_archivo("empleados.txt", 'a')
    con = 0
    for i in lista_emp:
        if i in lista_emp2:
            con = con + 1
            comparacion.append(i)
    if len(comparacion) > 0:
        for i in comparacion: print( 'Days in Common ' '%s' % i)    
        print ('Employees:', lista_emp[0],'-', lista_emp2[0],':','Days in common:', con)
    else:
        print ('No exist Days in common ')
    arch.write('Employees:' + str(lista_emp[0])+'-'+ str(lista_emp2[0])+':'+'Days in common:'+ str(con) + '\n' ) 
    arch.close()


def estab_archivo(ruta, permiso):
    archivo = open(ruta,permiso)
    return archivo


#Verify that only numbers and not letters are entered
def sol_num_entero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Choose an Option between 1 and 2 or 3 to Exit: "))
            correcto=True
        except ValueError:
            print('Error, Enter a correct Option')
    return num

#Menu Creation 
salir = False
opcion = 0

while not salir:

    print ("1. Input a New Employee and schedule of work")
    print ("2. Comparison of schedule of work")
    print ("3. Exit")
    print ("Choose an Option")
    opcion = sol_num_entero()
    if opcion == 1:
        name_emp()
        name_emp2()
    elif opcion == 2:
        comparar_horario()  
    elif opcion == 3:
        salir = True     
    else:
        print ("Enter a number between 1 and 2 or 3 to Exit")   
    print ("End")
