from funcionesPrueba3 import *
import time

os.system("clear")
print(
""""
         _    _ _______ ____  __  __  ____ _______ ____  _____            
    /\  | |  | |__   __/ __ \|  \/  |/ __ \__   __/ __ \|  __ \     /\    
   /  \ | |  | |  | | | |  | | \  / | |  | | | | | |  | | |__) |   /  \   
  / /\ \| |  | |  | | | |  | | |\/| | |  | | | | | |  | |  _  /   / /\ \  
 / ____ \ |__| |  | | | |__| | |  | | |__| | | | | |__| | | \ \  / ____ \ 
/_/    \_\____/   |_|  \____/|_|  |_|\____/  |_|  \____/|_|  \_\/_/    \_\
                                                                          
                                                                          
 _  ___    _ _____   ____  
| |/ / |  | |  __ \ / __ \ 
| ' /| |  | | |__) | |  | |
|  < | |  | |  _  /| |  | |
| . \| |__| | | \ \| |__| |
|_|\_\_____/|_|  \_\_____/ 
"""
)
time.sleep(2)

while True:
    
    #MENU
    os.system("clear")

    print("***Menú Automotora***\n")
    print("1- Registrar vehículo")
    print("2- Consulta vehículo")
    print("3- Lista de vehículos")
    print("4- Vender Auto / Contrato")
    print("5- Salir")
    
    try:
        opc = int(input("\nSeleccione una respuesta: "))
    except:
        print("Escriba una opción válida")
        input()
        continue

    if opc not in [1, 2, 3, 4, 5]:
        print("Escriba una respuesta válida")
        input("")

    os.system("clear")


    #LOGICA PRINCIPAL DEL PROGRAMA
    if opc == 1:
        registro_auto()
    if opc == 2:
        consulta_auto()
    if opc == 3:
        lista_vehiculos()
    if opc == 4:
        contrato()
    if opc == 5:
        break

print("Cerrando Sesión")
