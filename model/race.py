from abc import ABC, abstractmethod

class Race(ABC):
    def __init__(self, name, movement, darkvision, alignment, abilities):
        self.name = name
        self.movement = movement
        self.darkvision = darkvision
        self.alignment = alignment
        self.abilities = abilities
    
    @abstractmethod
    def apply_racial_bonuses(self, character):
        pass

    def __str__(self):
        return f"{self.name} (Mov: {self.movement}m, Infravisão: {self.darkvision}m, Alinhamento: {self.alignment})"

class Humano(Race):
    def __init__(self):
        super().__init__(
            "Humano", 9, 0, "Qualquer",
            ["Aprendizado (+10% XP)", "Adaptabilidade (+1 em uma JP)"]
        )
    
    def apply_racial_bonuses(self, character):
        # Humanos recebem +1 em um atributo à escolha
        pass

class Elfo(Race):
    def __init__(self):
        super().__init__(
            "Elfo", 9, 18, "Neutro",
            ["Percepção Natural", "Gracioso (+1 JPD)", "Arma Racial (+1 dano com arcos)", "Imunidades (sono, ghoul)"]
        )
    
    def apply_racial_bonuses(self, character):
        # Elfos recebem +1 em Destreza
        character.attributes["Destreza"] += 1

class Anao(Race):
    def __init__(self):
        super().__init__(
            "Anão", 6, 18, "Ordem",
            ["Mineradores", "Vigoroso (+1 JPC)", "Armas Grandes (restrição)", "Inimigos (orcs, ogros, hobgoblins)"]
        )
    
    def apply_racial_bonuses(self, character):
        # Anões recebem +1 em Constituição
        character.attributes["Constituição"] += 1

class Halfling(Race):
    def __init__(self):
        super().__init__(
            "Halfling", 6, 0, "Neutro",
            ["Furtivo (1-2 em 1d6)", "Destemido (+1 JPS)", "Bons de Mira", "Pequenos (ataques difíceis de criaturas grandes)"]
        )
    
    def apply_racial_bonuses(self, character):
        # Halflings recebem +1 em Destreza
        character.attributes["Destreza"] += 1