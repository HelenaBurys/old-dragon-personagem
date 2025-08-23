class Character:
    def __init__(self, name, race, classe, attributes):
        self.name = name
        self.race = race
        self.classe = classe
        self.attributes = attributes
        self.hit_points = classe.calculate_hit_points(attributes["Constituição"])
        
        # Aplicar bônus raciais
        race.apply_racial_bonuses(self)
    
    def __str__(self):
        return (f"{self.name} - {self.race} | {self.classe} | "
                f"PV: {self.hit_points} | Atributos: {self.attributes}")
    
    def show_detailed_sheet(self):
        print(f"\n⚔️  Ficha do Personagem: {self.name}  ⚔️")
        print("=" * 50)
        print(f"🏹 Raça: {self.race.name}")
        print(f"🛡️  Classe: {self.classe.name}")
        print(f"❤️  Pontos de Vida: {self.hit_points}")
        print("\n📊 Atributos:")
        print("-" * 30)
        for attr, value in self.attributes.items():
            desc = self._get_attribute_description(value)
            print(f"{attr}: {value} {desc}")
        
        print("\n🌟 Habilidades da Raça:")
        for ability in self.race.abilities:
            print(f"• {ability}")
            
        print("\n🎯 Habilidades da Classe:")
        for ability in self.classe.abilities:
            print(f"• {ability}")
        print("=" * 50)
    
    def _get_attribute_description(self, value):
        if value <= 6:
            return "(Fraco)"
        elif value <= 10:
            return "(Mediano)"
        elif value <= 15:
            return "(Bom)"
        else:
            return "(Excelente)"