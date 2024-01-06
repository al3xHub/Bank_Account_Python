'''
- crear clase persona:
  - con nombre y apellido como atributos
- clase cliente:
  - que hereda de persona.
  - Atributos propios "numero_cuenta y balance".
  - métodos
       - imprimir datos cliente
       - Depositar
       - Retirar (Hay que tener en cuenta que el cliente no debe retirar más dinero del que tiene.)
- Preguntar usuario que quiero hacer al iniciar el programa (Depositar, retirar o salir), cada vez que se realize
    una operación mostrar balance.
- El cliente puede hacer tantas operaciones como quiera hasta elegir salir.
-Crear funciones:
  - Crear cliente pidiendo todos los datos (atributos). Devolviendo (return) un objeto ya creado.
  - Crear inicio llamando a la función crear_cliente() y después preguntar al usuario que operaciones realizar.
'''

import random


class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class Cliente(Persona):
    def __init__(self, nombre, apellidos, numero_cuenta, balance):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_datos_cliente(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellidos: {self.apellidos}')
        print(f'Nº de Cuenta: {self.numero_cuenta}')
        print(f'Balance: {self.balance}')

    def depositar(self, dinero):
        self.balance += dinero
        print(f'Se ha depositado {dinero} euros.')
        print(f'Balance: {self.balance}')

    def retirar(self, dinero):
        if dinero > self.balance:
            print('Lo siento el dinero que desea retirar supera los fondos de la cuenta bancaria.')
        else:
            self.balance -= dinero
            print(f'Se ha retirado {dinero} euros.')
            print(f'Balance: {self.balance}')


def crear_cliente():
    print('Crear Nuevo Cliente:')
    nombre_cliente = input('Por favor, escribe tu nombre.')
    apellidos_cliente = input('Por favor, escribe tus apellidos.')
    numero_cuenta = random.randint(1000, 9999)
    balance = 0
    nuevo_cliente = Cliente(nombre_cliente, apellidos_cliente, numero_cuenta, balance)

    print(nuevo_cliente)
    return nuevo_cliente


def inicio():
    cliente = crear_cliente()
    cliente.imprimir_datos_cliente()

    opciones = 'x'

    while opciones != '3':
        print(f'Bienvenido a tu banco favorito.')
        opciones = input('Indica con un número del 1 al 3 que operación deseas realizar\n 1- Depositar\n 2- Retirar '
                         'fondos\n 3- Salir')
        if opciones == '1':
            dinero_depositado = int(input('¿Cuánto dinero desea depositar?'))
            cliente.depositar(dinero_depositado)
        elif opciones == '2':
            dinero_retirado = int(input('¿Cuánto dinero desea retirar?'))
            cliente.retirar(dinero_retirado)
        elif opciones == '3':
            break
        else:
            print('Has escrito un carácter incorrectamente.')


inicio()
