import csv
import time

maxsel = 6

#svfile = open('ssn.csv', 'r', newline='')
with open('ssn.csv', 'r', newline="") as csvfile: #Abrir archivo csv
    data = list(csv.DictReader(csvfile))

print('Bienvenido a la base de datos de estudiantes')
print('1: Ver alumnos inscriptos')
print('2: Ver numero de Seguro Social')
print('3: Ver los resultados de los 3 examenes')
print('4: Ver el resultado del examen final')
print('5: Ver nota final')
print('6: Modificar lista de estudiantes')
print('0: Finalizar')

def restart():
    time.sleep(0.3)
    print()
    print('1: Ver alumnos inscriptos')
    print('2: Ver numero de Seguro Social')
    print('3: Ver los resultados de los 3 examenes')
    print('4: Ver el resultado del examen final')
    print('5: Ver nota final')
    print('0: Finalizar')
    print()
    selection()

def selection():


    selection = int(input('Ingresar un número: ')) #Preguntar un numero de la lista

    while selection > maxsel or selection < 0:
        selection = int(input('Ingresar un número válido: '))

    counter = 1
    if selection == 1:
        print()
        for i in data:
            print(str(counter)+'.',i['Last name'])
            counter += 1
        restart()

    elif selection == 2:

        print()
        print('Seleccionó 2')
        print()

        all_lines = list(data['num'])
        last_line = all_lines[-1]

        surname = int(input('Ingresar el número del estudiante: \n'))
        if surname > int(last_line):
            surname = int(input('Estudiante no encontrado, intentar nuevamente'))
        print(data[surname-1]['new_SSN'])
        restart()

    elif selection == 3:
        print()
        print('Seleccionó 3')
        print()
        surname = int(input('Ingresar el número del estudiante: \n'))
        print(data[surname-1]['Test1'], end=", ")
        print(data[surname-1]['Test2'], end=", ")
        print(data[surname-1]['Test3'])
        restart()

    elif selection == 4:
        print()
        print('Seleccionó 4')
        print()
        surname = int(input('Ingresar el número del estudiante: \n'))
        print(data[surname-1]['Final'])
        restart()

    elif selection == 5:
        print()
        print('Seleccionó 5')
        print()
        surname = int(input('Ingresar el número del estudiante: \n'))
        print(data[surname-1]['Grade'])
        restart()
    
    elif selection == 6:
        print()
        modd = str(input('Que Desea hacer?: \'AGREGAR\' o \'QUITAR\': '))
        if modd == 'QUITAR':
            pass
        elif modd == 'AGREGAR':
            new_surname = input('Ingrese el apellido del nuevo estudiante: ')
            new_name = input('Ingrese el nombre del nuevo estudiante: ')
            new_ssn = input('Ingrese el numero de seguro social (9 números) del nuevo estudiante: ')

            while len(new_ssn) != 9:
                new_ssn = input('Ingrese el numero de seguro social (9 números) del nuevo estudiante: ')
            new_ssn = (new_ssn[:3]+'-'+new_ssn[3:5]+'-'+new_ssn[5:])

            tup = (counter+1, new_surname, new_name, new_ssn)

            #writer_object = writer(csvfile)
            #writer_object.writerow(tup)
            
    elif selection == 0:
        print('Hasta luego')
        exit()

if __name__ == '__main__':
    selection()
