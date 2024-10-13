from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemons=[]):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, character: Pokemon):
        if character in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(character)
            return f"Caught {character.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for character in self.pokemons:
            if pokemon_name == character.name:
                self.pokemons.remove(character)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        if self.pokemons:
            for character in self.pokemons:
                result += f"\n- {character.pokemon_details()}"
        return result
