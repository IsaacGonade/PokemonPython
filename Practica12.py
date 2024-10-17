import requests
import json


class Pokemon:
    def __init__(self, nombre, id, peso, altura, tipo):
        self.nombre = nombre
        self.id = id
        self.peso = float(peso)
        self.altura = float(altura)
        self.tipo = tipo

    #esta funcion hace que cuando se tenga que imprimir un objeto de la clase se escriba con este formato
    def __str__(self):
        return f"Nombre :{self.nombre} Id: {self.id} Peso: {self.peso}kgs Altura: {self.altura}m Tipo: {self.tipo}"


# Función para obtener un pokemon desde su API
def obtener_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json() # convierte el json en un diccionario
            print("Nombre: ", datos["name"])
            print("ID: ", datos["id"])
            print("Peso: ", datos["weight"])
            print("Altura: ", datos["height"])
            print("Tipo(s): ")
            for type in datos["types"]:  # types es una lista
                print(type["type"]["name\n"])
        else:
            print(f"Error: {respuesta.status_code}; el pokemon {pokemon} no se ha encontrado")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

# Inicializar la lista de pokemons
pokemons = []


# Bucle principal
def main():
    while True:
        print("1. Agregar pokemon a la pokedex")
        print("2. Listar pokemons")
        print("3. Eliminar pokemon")
        print("4. Consultar la pokedex real")
        print("5. Ver los ID de todos los pokemons")
        print("6. Salir")
        opcion = int(input("Selecciona una opción: "))

        match opcion:
            #pido todas las variables al usuario y la meto en un objeto de la clase pokemon
            case 1:
                nombre = input("Nombre del pokemon: ")
                id = input("Id del pokemon: ")
                peso = input("Peso del pokemon: ")
                altura = input("Altura del pokemon: ")
                tipo = input("Tipo del pokemon: ")
                pokemon = Pokemon(nombre, id, peso, altura, tipo)
                #añado el objeto creado a la lista
                pokemons.append(pokemon)
                print("Pokemon añadido a la pokedex!\n")
            case 2:
                #verificar si la lista está vacia
                if len(pokemons) == 0:
                    print("No hay pokemons en la pokedex")
                else:
                    #mostrar los pokemon de la lista
                    for i, pokemon in enumerate(pokemons, 1):
                        print(f"{i}. {pokemon}\n")
            case 3:
                #pido al usuario que introduzca el número del pokemon que desea eliminar, se resta 1 porque los índices de las listas en python comienzan desde 0
                indice = int(input("Número del pokemon a eliminar: ")) - 1
                if 0 <= indice < len(pokemons):
                    #la funcion pop se usa para eliminar el pokemon de la lista pokemons en la posición indicada por indice
                    pokemons.pop(indice)
                    print("Pokemon eliminado\n")
                else:
                    print("Ese pokemon no existe\n")
            case 4:
                #llamo a la funcion del api
                pokemon = input("Dime el nombre o número del POKEMON a buscar: ").lower()
                obtener_pokemon(pokemon)
            case 5:
                #funcion lambda que muestra los ids de todos los pokemons que hay en la lista
                ids = list(map(lambda p: p.id, pokemons))
                print(f"Id de todos los pokemons: {ids}")
            case 6:
                print("¡Hasta luego!")
                break

# Ejecutar la función main()
main()
