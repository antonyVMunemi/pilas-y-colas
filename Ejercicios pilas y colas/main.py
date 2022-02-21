from Pila_cola_lista import *
import os

c1 = True
while c1:
    opc = input('1.PILAS 2.COLAS. 3.LISTAS 4.SALIR: ')
    os.system('cls')
    if opc == '1':
        print('Bienvenido a pilas'.center(30,'-'))
        tamaño = int(input('\nIngrese el tamaño de la pila: '))
        pilas = Stack(tamaño)
        c = True
        while c:
            opc = input('\n1.PUSH 2.POP 3.LONGITUD 4.SHOW 5.BUSCAR 6.SALIR: ')
            if opc == '1':
                pilas.push()
            else:
                if opc == '2':
                    pilas.pop()
                else:
                    if opc == '3':
                        pilas.longitud()
                    else:
                        if opc == '4':
                            pilas.show()
                        else:
                            if opc == '5':
                                pilas.buscar()
                            else:
                                if opc == '6':
                                    c = False
                                    c1 = True
                                    os.system('cls')
    else:
        if opc == '2':
            print('Bienvenido a colas'.center(30,'-'))
            tamaño = int(input('\nIngrese el tamaño de la cola: '))
            colas = Cola(tamaño)
            c = True
            while c:
                opc = input('\n1.PUSH 2.POP 3.LONGITUD 4.SHOW 5.BUSCAR 6.SALIR: ')
                if opc == '1':
                    colas.push()
                else:
                    if opc == '2':
                        colas.pop()
                    else:
                        if opc == '3':
                            colas.longitud()
                        else:
                            if opc == '4':
                                colas.show()
                            else:
                                if opc == '5':
                                    colas.buscar()
                                else:
                                    if opc == '6':
                                        c = False
                                        c1 = True
                                        os.system('cls')
        else:

            if opc == '3':
                print('Bienvenido a listas'.center(30,'-'))
                tamaño = int(input('\nIngrese el tamaño de la lista: '))
                listas = Lista(tamaño)
                c = True
                while c:
                    opc = input('\n1.PUSH 2.POP 3.SHOW 4.ELIMINAR ELEMENTO 5.INSERTAR ELEMENTO 6.BUSCAR 7.SALIR: ')
                    if opc == '1':
                        listas.push()
                    else:
                        if opc == '2':
                            listas.pop()
                        else:
                            if opc == '3':
                                listas.show()
                            else:
                                if opc == '4':
                                    listas.eliminarElemento()
                                else:
                                    if opc == '5':
                                        listas.insertarElemento()
                                    else:
                                        if opc == '6':
                                            listas.buscar()
                                        else:
                                            if opc == '7':
                                                c = False
                                                c1 = True
                                                os.system('cls')
            else:
                if opc == '4':
                    print('Gracias por usar el programa')
                    c1 = False

