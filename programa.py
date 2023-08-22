# Juan Sebastian Lozano Siza. Grupo: R4
import json
import os

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")

def leerDatos():
    try:
        with open('Manuales.json', 'r', encoding="utf-8") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        return {"manuales": {}}

def guardarDatos(datos):
    with open('Manuales.json', 'w', encoding="utf-8") as file:
        json.dump(datos, file, indent=4)

def crearManual(datos):
    manual = input("Digite el nombre del manual: ")
    while not manual:
        msgError("¡El manual no puede estar vacío!")
        manual = input("Digite el nombre del manual: ")

    autor = input("Ingrese el nombre del autor: ")
    while not autor:
        msgError("¡El autor no puede estar vacío!")
        autor = input("Ingrese el nombre del autor: ")

    paginas = None
    while paginas is None:
        try:
            paginas = int(input("Ingrese el número de páginas: "))
        except ValueError:
            msgError("¡El número debe ser un número válido!")

    temas = None
    while temas is None:
        try:
            temas = int(input("Cuantos temas desea agregar? "))
        except ValueError:
            msgError("¡El número debe ser un número válido!")

    listadoTemas = []
    for i in range(temas):
        titulo = input(f"Ingrese el título del tema {i + 1}: ")
        while not titulo:
            msgError("¡El nombre del título no puede estar vacio!")
            titulo = input(f"Ingrese el título del tema {i + 1}: ")

        clasificacion = None    
        while clasificacion is None:
            try:
                clasificacion = int(input(f"Ingrese la clasificación del tema {i + 1} (1.Básicos, 2.Intermedios, 3.Avanzados): "))
            except ValueError:
                msgError("¡La clasificación debe ser un número valido!")    
        listadoTemas.append({"Titulo": titulo, "Clasificación": clasificacion})

    datos["manuales"][manual] = {
        "author": autor,
        "paginas": paginas,
        "temas": listadoTemas
    }
    guardarDatos(datos)
    os.system("clear")
    print("\n", "=" * 50)
    print("Manual creado exitosamente".center(50))
    print("=" * 50)

def modificarManual(datos):
    listarManuales(datos)
    while True:
        encontrado = False
        manual = input("\nDigite el nombre del manual: ")
        if manual in datos["manuales"]:
            titulo = input("Digite el título del tema a modificar: ")
            for tema in datos["manuales"][manual]["temas"]:
                if tema["Titulo"] == titulo:
                    encontrado=True
                    titulo = input("Ingrese el nuevo titulo del tema: ")
                    while not titulo:
                        msgError("¡El nombre del título no puede estar vacio!")
                        titulo = input("Ingrese el nuevo titulo del tema: ")

                    clasificacion = None    
                    while clasificacion is None:
                        try:
                            clasificacion = int(input("Ingrese la nueva clasificación para el tema(1.Básicos, 2.Intermedios, 3.Avanzados): "))
                        except ValueError:
                            msgError("¡La clasificación debe ser un número valido!")  
 
                    tema["Titulo"] = titulo              
                    tema["Clasificación"] = clasificacion
                    guardarDatos(datos)

                    os.system("clear")
                    print("\n", "=" * 50)
                    print("Tema modificado exitosamente".center(50))
                    print("=" * 50)
                    return
            msgError("El título del tema no fue encontrado en el manual")
        if not encontrado:
            msgError("El manual no fue encontrado.")
        else:
            break     

def eliminarManual(datos):
    listarManuales(datos)
    while True:
        encontrado= False
        manual = input("Digite el nombre del manual: ")
        if manual in datos["manuales"]:
            encontrado = True
            titulo = input("Digite el título del tema a eliminar: ")
            for tema in datos["manuales"][manual]["temas"]:
                if tema["Titulo"] == titulo:
                    datos["manuales"][manual]["temas"].remove(tema)
                    guardarDatos(datos)
                    os.system("clear")
                    print("\n", "=" * 50)
                    print("Tema eliminado exitosamente".center(50))
                    print("=" * 50)
                    return
            msgError("El título del tema no fue encontrado en el manual.")
        if not encontrado:
            msgError("El manual no fue encontrado")
        else:
            break    

def listarManuales(datos):
    print("{:^25} {:^15} {:^10} {:^35}".format("Nombre del manual", "Autor", "Paginas", "Temas"))
    print("{:^25} {:^15} {:^10} {:^20} {:^10}".format("", "", "", "Titulo", "Clasificacion"))
    print("=" * 90)  
    for manual, info in datos["manuales"].items():
        autor = info["author"]
        paginas = info["paginas"]
        for tema in info["temas"]:
            titulo = tema["Titulo"]
            clasificacion = tema["Clasificación"]
            print("{:^25} {:^15} {:^10} {:^20} {:^10}".format(manual, autor, paginas, titulo, clasificacion))

def generarInforme(datos):
    with open('datos.txt', 'w') as file:
        for manual, info in datos["manuales"].items():
            autor = info["author"]
            paginas = info["paginas"]
            file.write(f"Manual: {manual}\n")
            file.write(f"Autor: {autor}\n")
            file.write(f"Páginas: {paginas}\n")
            file.write("Temas:\n")
            for tema in info["temas"]:
                titulo = tema["Titulo"]
                clasificacion = tema["Clasificación"]
                file.write(f"\tTítulo: {titulo}, Clasificación: {clasificacion}\n")
            file.write("\n")
        print("=" * 50)    
        print("Informe generado exitosamente".center(50))
        print("=" * 50)

def menu():
    while True:
        try:
            print("\n\n** SISTEMA GESTOR DE LIBROS **")
            print("\tMENU")
            print("1. Crear manual")
            print("2. Modificar manual")
            print("3. Eliminar manual")
            print("4. Listar manuales")
            print("5. Generar informe en archivo .txt")
            print("6. Salir")
            op = int(input("\t>> Escoja una opción (1-6): "))
            if op < 1 or op > 6:
                msgError("Error. Opción Inválida (de 1 a 6).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 6).")
            continue

def main():
    os.system("clear")
    datos = leerDatos()
    while True:
        op = menu()
        if op == 1:
            os.system("clear")
            crearManual(datos)
        elif op == 2:
            os.system("clear")
            modificarManual(datos)
        elif op == 3:
            os.system("clear")
            eliminarManual(datos)
        elif op == 4:
            os.system("clear")
            listarManuales(datos)
        elif op == 5:
            os.system("clear")
            generarInforme(datos)
        elif op == 6:
            salir = input("¿Está seguro que desea salir? (S/N): ")
            if salir.upper() == "S":
                print("\nGracias por usar el programa... Adiós...\n".center(80))
                break
            elif salir.upper() == "N":
                continue
            else:
                msgError("Error. Digite una opción válida.")
                continue

main()