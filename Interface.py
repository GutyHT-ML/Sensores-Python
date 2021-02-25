import Sensores as s
import Registros_MongoDB
import sys 
import time

def read():
    x = input()
    if x == "a" or x == "A": 
        values()
        menu()
    if x == "b" or x == "B": 
        values()
        opciones()
    if x == "c" or x == "C": 
       print("Adios")
       sys.exit()

def readd():
    x = input()
    if x == "a" or x == "A": 
        r = Registros_MongoDB
        r.addRegistro()
    if x == "b" or x == "B": 
        print("No")
    if x == "c" or x == "C": 
       print("No")
    if x == "d" or x == "B": 
        menu()

def menu():
    print("----------------Menú-----------------")
    print("a) Ver sensores......................")
    print("b) Guardar valores...................")
    print("c) Salir.............................")
    read()

def values():
    print("----------------Sensores-------------")
    sensores = Registros_MongoDB
    data = sensores.getValores()
    print("............Valores.............")
    print("Ultrasonico:{0}".format(data[3]))
    print("PIR:{0}".format(data[2]))
    print('Humedad:{0:0.1f}%'.format(data[0]))
    print('Temperatura:{0:0.1f} C'.format(data[1]))
    time.sleep(5)

def opciones():
    print("----------------Menú-----------------")
    print("a) Guardar en mongoDB................")
    print("b) Guardar en Mysql..................")
    print("c) Guardar de manera local...........")
    print("d) Atras.............................")
    readd()

menu()