class Stack:
    def __init__(self, tamano):
        self.pila = []
        self.tope = 0
        self.size = tamano

    def push(self):
        while self.size > self.tope:
            dato = input('Ingrese un elemento a la pila: ')
            self.pila.append(dato)
            self.tope += 1
        else:
            print('La pila esta llena\n')

    def pop(self):
        if len(self.pila) != 0:
            self.pila.pop()
            self.tope -= 1
            print(self.pila)
        else:
            print('La pila esta vacia\n')

    def longitud(self):
        print(f'La longitud de la pila es: {len(self.pila)}\n')

    def show(self):
        if len(self.pila) != 0:
            print(self.pila)
        else:
            print('La pila esta vacia\n')

    def buscar(self):
        if len(self.pila) != 0:
            pos = input('Ingrese un elemento para retornar una posicion: ')
            if pos in self.pila:
                print(f'Posicion: {self.pila.index(pos)}')
            else:
                print(f'Imprimiendo Elemento de la posicion -1: {self.pila[-1]}\n')
        else:
            print('La pila esta vacia\n')
            
class Cola:
    def __init__(self, tamano):
        self.cola = []
        self.tope = 0
        self.size = tamano

    def push(self):
        while self.size > self.tope:
            dato = input('Ingrese un elemento a la cola: ')
            self.cola.append(dato)
            self.tope += 1
        else:
            print('La cola esta llena\n')

    def pop(self):
        if len(self.cola) != 0:
            self.cola.pop(0)
            self.tope -= 1
            print(self.cola)
        else:
            print('La cola esta vacia\n')

    def longitud(self):
        print(f'La longitud de la Cola es: {len(self.cola)}\n')

    def show(self):
        if len(self.cola) != 0:
            print(self.cola)
        else:
            print('La cola esta vacia\n')

    def buscar(self):
        if len(self.cola) != 0:
            pos = input('Ingrese un elemento para retornar una posicion: ')
            if pos in self.cola:
                print(f'Posicion: {self.cola.index(pos)}')
            else:
                print(f'Imprimiendo Elemento de la posicion -1: {self.cola[-1]}\n')
        else:
            print('La cola esta vacia\n')

class Lista:
    def __init__(self, tamano):
        self.lista = []
        self.size = tamano
        self.tope = 0

    def push(self):
        while self.size > self.tope:
            dato = input('Inserte el nuevo elemento: ')
            self.lista.append(dato)
            self.tope +=1
        else:
            print('La lista esta Llena\n')

    def pop(self):
        if len(self.lista) != 0:
            self.lista.pop()
            self.tope -=1
            print(f'Mostrando lista: {self.lista}')
        else:
            print('La lista esta vacia\n')

    def show(self):
        if len(self.lista) != 0:
            print(f'Mostrando lista: {self.lista}\n')
        else:
            print('La lista esta vacia\n')

    def eliminarElemento(self):
        if len(self.lista) == 0:
            print('La lista esta vacia\n')
        else:
            opc = int(input('Ingrese la posicion que desea borrar: '))
            while opc > (len(self.lista)- 1):
                opc = int(input('Posicion inexistente, vuelva a ingresar posicion: '))
            else:
                print(f'Elemento borrado: {self.lista.pop(opc)}')


    def insertarElemento(self):
        if len(self.lista) == 0:
            print('La lista esta vacia\n')
        else:
            opc = input('Ingrese el nuevo elemento: ')
            opc1 = int(input('Ingrese la posicion en la que desea insertar el nuevo dato: '))
            while opc1 > (len(self.lista) - 1):
                opc1 = int(input('Posicion inexistente, vuelva a ingresar posicion: '))
            else:
                self.lista.insert(opc1, opc)
                print(f'Elemento insertado en la posicion {opc1}: {opc}')


    def buscar(self):
        if len(self.lista) != 0:
            pos = input('Ingrese el valor para retornar una posicion: ')
            if pos in self.lista:
                print(f'Posicion: {self.lista.index(pos)}\n')
            else:
                print(f'Imprimiendo Elemento de la posicion -1: {self.lista[-1]}\n')
        else:
            print('La lista esta vacia\n')