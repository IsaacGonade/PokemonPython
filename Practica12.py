import requests
import json


class Pokemon:
    def __init__(self, nombre, id, peso, altura, tipo):
        self.nombre = nombre
        self.id = id
        self.peso = peso
        self.altura = altura
        self.tipo = tipo

    #esta funcion hace que cuando se tenga que imprimir un objeto de la clase se escriba con este formato
    def __str__(self):
        return f"Nombre :{self.nombre} Id: {self.id} Peso: {self.peso} Altura: {self.altura} Tipo: {self.tipo}"


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
                print(type["type"]["name"])
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
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))

        match opcion:
            case 1:
                nombre = input("Nombre del pokemon: ")
                id = input("Id del pokemon: ")
                peso = input("Peso del pokemon: ")
                altura = input("Altura del pokemon: ")
                tipo = input("Tipo del pokemon: ")
                pokemon = Pokemon(nombre, id, peso, altura, tipo)
                pokemons.append(pokemon)
                print("Pokemon añadido a la pokedex!")
            case 2:
                # len lo que hace es contar los elementos dentro de la lista y si hay cero pues hace eso
                if len(pokemons) == 0:
                    print("No hay pokemons en la pokedex")
                for i, tarea in enumerate(pokemons, 1):
                    print(f"{i}. {pokemon}")
            case 3:
                indice = int(input("Número del pokemon a eliminar: ")) - 1
                if 0 <= indice < len(pokemons):
                    pokemons.pop(indice)
                    print("Pokemon eliminado")
                else:
                    print("Ese pokemon no existe")
            case 4:
                pokemon = input("Dime el nombre o número del POKEMON a buscar: ").lower()
                obtener_pokemon(pokemon)
            case 5:
                print("¡Hasta luego!")
                break

# Ejecutar la función main()
main()
