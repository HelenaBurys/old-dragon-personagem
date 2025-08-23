import time
from entities.race import Humano, Elfo, Anao, Halfling
from entities.classes import Guerreiro, Clerigo, Ladrao
from services.attribute_service import AttributeService

class CharacterCreator:
    def __init__(self):
        self.attribute_service = AttributeService()
        self.races = {
            "1": Humano(),
            "2": Elfo(),
            "3": Anao(),
            "4": Halfling()
        }
        self.classes = {
            "1": Guerreiro(),
            "2": Clerigo(),
            "3": Ladrao()
        }
    
    def display_welcome(self):
        print("=" * 50)
        print("⚔️  Bem-vindo ao RPG Old Dragon!  ⚔️")
        print("=" * 50)
        print()
    
    def get_character_name(self):
        return input("Digite o nome do seu personagem: ")
    
    def select_race(self):
        print("\nEscolha a raça do seu personagem:")
        print("1 - Humano")
        print("2 - Elfo")
        print("3 - Anão")
        print("4 - Halfling")
        
        while True:
            choice = input("Digite sua opção: ")
            if choice in self.races:
                race = self.races[choice]
                print(f"Raça selecionada: {race.name}")
                return race
            print("Opção inválida! Tente novamente.")
    
    def select_class(self):
        print("\nEscolha a classe do seu personagem:")
        print("1 - Guerreiro")
        print("2 - Clérigo")
        print("3 - Ladrão")
        
        while True:
            choice = input("Digite sua opção: ")
            if choice in self.classes:
                classe = self.classes[choice]
                print(f"Classe selecionada: {classe.name}")
                return classe
            print("Opção inválida! Tente novamente.")
    
    def select_attribute_distribution(self):
        print("\nEscolha o estilo de criação de atributos:")
        print("1 - Clássico (3d6 em ordem)")
        print("2 - Aventureiro (3d6, distribuir livremente)")
        print("3 - Heroico (4d6, elimina o menor)")
        
        while True:
            choice = input("Digite sua opção: ")
            distribution = self.attribute_service.get_distribution_method(choice)
            if distribution:
                return distribution, choice
            print("Opção inválida! Tente novamente.")
    
    def create_character(self):
        self.display_welcome()
        
        name = self.get_character_name()
        print(f"\nSaudações, {name}! Vamos criar suas habilidades...\n")
        time.sleep(1)
        
        race = self.select_race()
        time.sleep(0.5)
        
        classe = self.select_class()
        time.sleep(0.5)
        
        distribution, choice = self.select_attribute_distribution()
        
        print("\nGerando atributos...")
        time.sleep(1)
        
        if choice == "1":  # Clássico
            attributes = self.attribute_service.distribute_attributes(distribution)
        else:  # Aventureiro ou Heroico
            rolls = distribution.generate_attributes()
            attributes = self.attribute_service.distribute_attributes(distribution, rolls)
        
        from entities.character import Character
        character = Character(name, race, classe, attributes)
        
        return character