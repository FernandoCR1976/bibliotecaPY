import json
import os
from pathlib import Path

# Obtener la ruta del directorio donde se ejecuta el script
SCRIPT_DIR = Path(__file__).resolve().parent
# Definir la ruta completa al archivo de datos
DATA_FILE = SCRIPT_DIR / "biblioteca.json"



def load_libros():

    try:
        with open(DATA_FILE,'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # si el archivo no existe, retorne una lista vacia o data inicial
        return [
            {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "ISBN": "978-3-16-148410-0"
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605,
        "ISBN": "978-1-23-456789-7"
    },
    {
        "titulo": "La casa de los espíritus",
        "autor": "Isabel Allende",
        "año": 1982,
        "ISBN": "978-0-12-345678-9"
    },
    {
        "titulo": "El amor en los tiempos del cólera",
        "autor": "Gabriel García Márquez",
        "año": 1985,
        "ISBN": "978-4-56-789012-3"
    }
        ]
    except json.JSONDecodeError:
        print('Error: Que no se pudo decodificar la informacion del archivo')
        return [
            {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "ISBN": "978-3-16-148410-0"
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605,
        "ISBN": "978-1-23-456789-7"
    },
    {
        "titulo": "La casa de los espíritus",
        "autor": "Isabel Allende",
        "año": 1982,
        "ISBN": "978-0-12-345678-9"
    },
    {
        "titulo": "El amor en los tiempos del cólera",
        "autor": "Gabriel García Márquez",
        "año": 1985,
        "ISBN": "978-4-56-789012-3"
    }
        ]
    
def save_libros(libros_data):
    with open(DATA_FILE,'w', encoding='utf-8') as f:
        json.dump(libros_data, f, indent=4, ensure_ascii=False)

def display_libros(libros_data):

    if not libros_data:
        print("No hay libros en la Biblioteca")
        return
    for i, libro in enumerate(libros_data):
        print(f'{i+1}. Titulo: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, ISBN: {libro['ISBN']} ')
    print('-'*30)

def add_libro(libros_data):

    titulo = input("Ingerse el titulo deol libro: ")
    autor = input('Ingrese el nombre del autor: ')
    while True:
        try:
            año = int(input("Ingrese el año de publicacion: "))
            break
        except ValueError:
            print("Entrada invalida, por favor ingrese un numero para el año")

    isbn = input("Ingrese el ISBN del libro")

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "ISBN": isbn
    }

    libros_data.append(nuevo_libro)
    save_libros(libros_data)
    print(f"'{titulo}' ha sido añadido a la bilbioteca")

def modify_libro(libros_data):
    return


def delete_libro(libros_data):
    display_libros(libros_data)
    if not libros_data:
        return
    while True:
        try:
            index = int(input("Ingrese el numero de libro que desea eliminar:\n"))
            if 0 <= index < len(libros_data):
                break
            else:
                print('Numero invalido, Intente de nuevo')
        except ValueError:
            print(" Debe de ingresar el NUMERO de la lista de libros")
    libro_eliminado = libros_data.pop(index-1)
    save_libros(libros_data)
    print(f"'{libro_eliminado}' ha sido borrado de la biblioteca")

def main():
    libros = load_libros()

    while True:
        print('\n---- Menu de la Biblioteca ----')
        print('1. Ver todos los libros')
        print('2. Añadir un libro')
        print('3. Modificar un libro')
        print('4. Eliminar un libro')
        print('5. Salir')

        choice = input('Seleccione una opcion (1-5):\n')

        if choice == '1':
            display_libros(libros)
        elif choice == '2':
            add_libro(libros)
        elif choice == '3':
            modify_libro(libros)
        elif choice == '4':
            delete_libro(libros)
        elif choice == '5':
            print('Saliendo del programa')
            break
        else:
            print('OPCION INVALIDA\nSeleccione una opcion (1-5):\n')

if __name__ == "__main__":
    main()