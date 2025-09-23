from abc import ABC, abstractmethod

class Class(ABC):
    def __init__(self, name, hit_die, armor, weapons, abilities):
        self.name = name
        self.hit_die = hit_die
        self.armor = armor
        self.weapons = weapons
        self.abilities = abilities
    
    @abstractmethod
    def calculate_hit_points(self, constitution):
        pass

    def __str__(self):
        return f"{self.name} (Dado de Vida: d{self.hit_die})"

class Guerreiro(Class):
    def __init__(self):
        super().__init__(
            "Guerreiro", 10, "Todas", "Todas",
            ["Aparar", "Maestria em Arma"]
        )
    
    def calculate_hit_points(self, constitution):
        mod_con = (constitution - 10) // 2
        return self.hit_die + mod_con

class Clerigo(Class):
    def __init__(self):
        super().__init__(
            "Clérigo", 8, "Todas", "Impactantes",
            ["Magias Divinas", "Afastar Mortos-Vivos", "Cura Milagrosa"]
        )
    
    def calculate_hit_points(self, constitution):
        mod_con = (constitution - 10) // 2
        return self.hit_die + mod_con

class Ladrao(Class):
    def __init__(self):
        super().__init__(
            "Ladrão", 6, "Leves", "Pequenas ou Médias",
            ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"]
        )
    
    def calculate_hit_points(self, constitution):
        mod_con = (constitution - 10) // 2
        return self.hit_die + mod_con