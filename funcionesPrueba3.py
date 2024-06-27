import csv
import datetime
import os

vehiculos = {}


#FUNCIONES PARA CSV
def crear_archivo():
    with open('BBDD/BaseAutos.csv', 'w', newline='') as archivo:
        campos = ["Patente", "Marca", "Modelo", "Año", "Valor", "Estado"]
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        escritor_csv.writeheader()
        print("Archivo creado")


def leer_csv():
    global vehiculos

    with open('BBDD/BaseAutos.csv', 'r', newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            vehiculos[fila["Patente"]] = fila

def escribir_csv():
    with open('BBDD/BaseAutos.csv', 'w', newline='') as archivo:
        campos = ["Patente", "Marca", "Modelo", "Año", "Valor", "Estado"]
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        escritor_csv.writeheader()
        for vehiculo in vehiculos.values():
            escritor_csv.writerow(vehiculo)



#FUNCIONES PARA APLICACION
def registro_auto():
    while True:
        # Instrucciones para insertar PATENTE. Restricciones y "Salir"
        patente = input("Ingrese su patente: ")
        if patente.lower() == "salir":
            break
        elif len(patente) != 6:
            print("Debe ingresar una patente válida")
            input("Pulse ENTER para continuar y volver al Menú Principal")
            return

        # Instrucciones para insertar MARCA. Restricciones y "Salir"
        marca_vehiculo = input("Ingrese la marca de su vehículo: ")
        if marca_vehiculo.lower() == "salir":
            break
        elif len(marca_vehiculo) <= 3:
            print("Debe ingresar una marca de vehículo válida para hacer válido el ingreso")
            print("ERROR ENCONTRADO: La marca que escribió tiene menos de 3 caracteres")
            input("Pulse ENTER para continuar y volver al Menú Principal")
            return

        # Instrucciones para insertar MODELO. Restricciones y "Salir"
        modelo_vehiculo = input("Ingrese el modelo de su vehículo: ")
        if modelo_vehiculo.lower() == "salir":
            break
        elif len(modelo_vehiculo) <= 3:
            print("Debe ingresar un modelo válido de vehículo para hacer válido el ingreso")
            print("ERROR ENCONTRADO: La marca que escribió tiene menos de 3 caracteres")
            input("Pulse ENTER para continuar y volver al Menú Principal")
            return

        # Instrucciones para insertar AÑO. Restricciones y "Salir"
        anno_vehiculo = input("Ingrese el año del vehículo: ")
        if anno_vehiculo.lower() == "salir":
            break
        try:
            anno_vehiculo = int(anno_vehiculo)
        except ValueError:
            print("Escriba un valor válido")
            input("Pulse ENTER para volver al Menú Principal")
            return

        if anno_vehiculo < 1980 or anno_vehiculo > 2024:
            print("Debe ingresar un año válido")
            input("Pulse ENTER para volver al Menú Principal")
            return

        # Instrucciones para insertar VALOR. Restricciones y "Salir"
        valor = input("Ingrese el valor del vehículo: ")
        if valor.lower() == "salir":
            break
        try:
            valor = int(valor)
        except ValueError:
            print("Escriba un valor válido")
            input("Pulse ENTER para volver al Menú")
            return

        if valor < 500000:
            print("Debe ingresar un valor mayor a $500.000")
            input("Pulse ENTER para continuar y volver al Menú Principal")
            return

        # Inserción de matriz de REGISTRO
        vehiculo = {
            "Patente": patente,
            "Marca": marca_vehiculo,
            "Modelo": modelo_vehiculo,
            "Año": anno_vehiculo,
            "Valor": valor,
            "Estado": "Disponible"
        }

        vehiculos[patente] = vehiculo
        escribir_csv()

        input("Se ha registrado con éxito.\nPulse ENTER para continuar")
        break

# Función para CONSULTAR SOBRE EL AUTO
def consulta_auto():
    print("Ingrese la patente del auto a revisar")
    pat = input("")
    print("")

    vehiculo = vehiculos.get(pat, None)

    if vehiculo is None:
        print("Vehículo no encontrado")
        input("Pulse ENTER para continuar")
        return

    print(f'Patente: {vehiculo["Patente"]}')
    print(f'Año: {vehiculo["Año"]}')
    print(f'Marca: {vehiculo["Marca"]}')
    print(f'Modelo: {vehiculo["Modelo"]}')
    print(f'Valor: {vehiculo["Valor"]}')
    print(f'Años desde fabricación: {2024 - int(vehiculo["Año"])}')
    print(f'Estado: {vehiculo["Estado"]}')

    print("")
    input("Pulse ENTER para continuar")

# Función para LISTAR VEHICULOS y ver DISPONIBILIDAD
def lista_vehiculos():
    print("VEHICULOS\n")
    for patente, vehiculo in vehiculos.items():
        print(f'Vehiculo: {vehiculo["Marca"]} {vehiculo["Modelo"]}')
        print(f'Patente: {vehiculo["Patente"]}')
        print(f'Estado: {vehiculo["Estado"]}')
        print("")
    input("Pulse ENTER para continuar")

# Función para IMPRIMIR CONTRATO y VENDER
def contrato():
    print("CREACION DE CONTRATO\n")
    print("Ingrese la patente del auto a vender. Recuerde que el auto debe estar Disponible para vender")
    pat = input("")

    if pat not in vehiculos:
        print("El vehículo no se encuentra disponible para vender\n")
        input("Pulse ENTER para volver al Menú Principal")
        return

    vehiculo = vehiculos[pat]

    if vehiculo["Estado"] != "Disponible":
        print("El vehículo no se encuentra disponible para vender\n")
        input("Pulse ENTER para continuar y volver al Menú Principal")
        return

    # FORMATO DE TEXTO DEL CONTRATO
    print("==== CONTRATO ====\n")
    print(f'FECHA: {datetime.datetime.now().strftime("%Y-%m-%d")}')
    print(f'HORA: {datetime.datetime.now().strftime("%H:%M:%S")}\n')

    print(f'Patente: {vehiculo["Patente"]}')
    print(f'Año: {vehiculo["Año"]}')
    print(f'Marca: {vehiculo["Marca"]}')
    print(f'Modelo: {vehiculo["Modelo"]}')
    print(f'Valor: {vehiculo["Valor"]}')
    print(f'Años desde fabricación: {2024 - int(vehiculo["Año"])}')
    print(f'Estado: {vehiculo["Estado"]}\n')

    # CONFIRMACION VENTA
    print("Confirme para realizar la venta")
    print("1 - CONFIRMAR")
    print("2 - VOLVER AL MENÚ PRINCIPAL")

    ans = input("")
    if ans == "1":
        vehiculo["Estado"] = "Vendido"
        vehiculos[pat] = vehiculo
        escribir_csv()
        print("La venta ha sido realizada con éxito.")
    elif ans == "2":
        return


