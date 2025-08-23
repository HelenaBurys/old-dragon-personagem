import random
from abc import ABC, abstractmethod
from enums.attribute_enum import AttributeType

class AttributeDistribution(ABC):
    @abstractmethod
    def generate_attributes(self):
        pass

    def _roll_dice(self, quantity, sides=6, drop_lowest=False):
        rolls = [random.randint(1, sides) for _ in range(quantity)]
        if drop_lowest:
            rolls.remove(min(rolls))
        return sum(rolls)

class ClassicDistribution(AttributeDistribution):
    def generate_attributes(self):
        attributes = {}
        for attr in AttributeType:
            attributes[attr.value] = self._roll_dice(3)
        return attributes

class AdventurousDistribution(AttributeDistribution):
    def generate_attributes(self):
        rolls = [self._roll_dice(3) for _ in range(6)]
        return rolls

class HeroicDistribution(AttributeDistribution):
    def generate_attributes(self):
        rolls = [self._roll_dice(4, drop_lowest=True) for _ in range(6)]
        return rolls

class AttributeService:
    def __init__(self):
        self.distributions = {
            "1": ClassicDistribution(),
            "2": AdventurousDistribution(),
            "3": HeroicDistribution()
        }
    
    def get_distribution_method(self, choice):
        return self.distributions.get(choice, self.distributions["1"])
    
    def distribute_attributes(self, distribution_method, rolls=None):
        if isinstance(distribution_method, ClassicDistribution):
            return distribution_method.generate_attributes()
        
        elif isinstance(distribution_method, AdventurousDistribution):
            if rolls is None:
                rolls = distribution_method.generate_attributes()
            
            print("Resultados disponíveis:", rolls)
            attributes = {}
            for attr in AttributeType:
                while True:
                    try:
                        choice = int(input(f"Escolha um valor para {attr.value}: "))
                        if choice in rolls:
                            rolls.remove(choice)
                            attributes[attr.value] = choice
                            break
                        else:
                            print("Valor inválido. Escolha um dos valores disponíveis.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
            return attributes
        
        elif isinstance(distribution_method, HeroicDistribution):
            if rolls is None:
                rolls = distribution_method.generate_attributes()
            
            print("Resultados disponíveis:", rolls)
            attributes = {}
            for attr in AttributeType:
                while True:
                    try:
                        choice = int(input(f"Escolha um valor para {attr.value}: "))
                        if choice in rolls:
                            rolls.remove(choice)
                            attributes[attr.value] = choice
                            break
                        else:
                            print("Valor inválido. Escolha um dos valores disponíveis.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
            return attributes