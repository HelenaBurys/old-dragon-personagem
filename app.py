from flask import Flask, render_template, request, session, redirect, url_for
import random
from services.character_creator import CharacterCreator
from model.character import Character
from services.save_service import save_character_to_json

app = Flask(__name__)
app.secret_key = 'old_dragon_rpg_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-character', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        # Coletar dados do formulário
        character_data = {
            'name': request.form['name'],
            'race_choice': request.form['race'],
            'class_choice': request.form['classe'],
            'distribution_choice': request.form['distribution']
        }
        
        # Criar personagem usando a fábrica existente (objetos de raça/classe)
        creator = CharacterCreator()

        # Gerar atributos baseado na escolha
        attributes = generate_attributes(character_data['distribution_choice'])

        # Instanciar o Character real (usa objetos de raça e classe)
        race_obj = creator.races.get(character_data['race_choice'])
        class_obj = creator.classes.get(character_data['class_choice'])

        # Se por algum motivo as escolhas não existirem, voltar com erro simples
        if race_obj is None or class_obj is None:
            return "Escolha de raça ou classe inválida.", 400

        character = Character(character_data['name'], race_obj, class_obj, attributes)

        # Salvar em arquivo JSON (serializa com __dict__ e converte nested objects)
        try:
            save_path = save_character_to_json(character)
        except Exception as e:
            # Se falhar ao salvar, logamos na sessão a mensagem de erro simples
            session['save_error'] = str(e)
            save_path = None

        # Guardar informações na sessão para a tela de ficha
        session['character_name'] = character_data['name']
        session['race_choice'] = character_data['race_choice']
        session['class_choice'] = character_data['class_choice']
        session['distribution_choice'] = character_data['distribution_choice']
        session['attributes'] = attributes
        session['save_path'] = save_path

        return redirect(url_for('character_sheet'))
    
    return render_template('create_character.html')

def generate_attributes(distribution_type):
    """Gera atributos baseado no método escolhido"""
    attributes = {}
    
    if distribution_type == '1':  # Clássico
        for attr in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            attributes[attr] = sum(random.randint(1, 6) for _ in range(3))
    
    elif distribution_type == '2':  # Aventureiro
        rolls = [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)]
        # Distribuir aleatoriamente para simplificar
        attrs = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        for i, attr in enumerate(attrs):
            attributes[attr] = rolls[i]
    
    elif distribution_type == '3':  # Heroico
        for attr in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            attributes[attr] = sum(rolls)
    
    return attributes

@app.route('/character-sheet')
def character_sheet():
    # Recuperar dados da sessão
    name = session.get('character_name', 'Herói Sem Nome')
    race_choice = session.get('race_choice', '1')
    class_choice = session.get('class_choice', '1')
    distribution_choice = session.get('distribution_choice', '1')
    attributes = session.get('attributes', {})
    
    # Mapear escolhas para nomes
    race_map = {
        '1': {'name': 'Humano', 'abilities': ['Aprendizado (+10% XP)', 'Adaptabilidade (+1 em uma JP)']},
        '2': {'name': 'Elfo', 'abilities': ['Percepção Natural', 'Gracioso (+1 JPD)', 'Arma Racial (+1 dano com arcos)', 'Imunidades (sono, ghoul)']},
        '3': {'name': 'Anão', 'abilities': ['Mineradores', 'Vigoroso (+1 JPC)', 'Armas Grandes (restrição)', 'Inimigos (orcs, ogros, hobgoblins)']},
        '4': {'name': 'Halfling', 'abilities': ['Furtivo (1-2 em 1d6)', 'Destemido (+1 JPS)', 'Bons de Mira', 'Pequenos (ataques difíceis de criaturas grandes)']}
    }
    
    class_map = {
        '1': {'name': 'Guerreiro', 'abilities': ['Aparar', 'Maestria em Arma'], 'hit_die': 10},
        '2': {'name': 'Clérigo', 'abilities': ['Magias Divinas', 'Afastar Mortos-Vivos', 'Cura Milagrosa'], 'hit_die': 8},
        '3': {'name': 'Ladrão', 'abilities': ['Ataque Furtivo', 'Ouvir Ruídos', 'Talentos de Ladrão'], 'hit_die': 6}
    }
    
    distribution_map = {
        '1': 'Clássico (3d6 em ordem)',
        '2': 'Aventureiro (3d6, distribuir livremente)',
        '3': 'Heroico (4d6, elimina o menor)'
    }
    
    # Calcular pontos de vida (simplificado)
    constitution = attributes.get('Constituição', 10)
    hit_die = class_map[class_choice]['hit_die']
    mod_con = (constitution - 10) // 2
    hit_points = hit_die + mod_con
    
    # Aplicar bônus raciais
    if race_choice == '2' or race_choice == '4':  # Elfo ou Halfling
        attributes['Destreza'] = attributes.get('Destreza', 10) + 1
    elif race_choice == '3':  # Anão
        attributes['Constituição'] = attributes.get('Constituição', 10) + 1
    
    character_data = {
        'name': name,
        'race': race_map[race_choice],
        'classe': class_map[class_choice],
        'attributes': attributes,
        'hit_points': hit_points,
        'distribution': distribution_map[distribution_choice]
    }
    
    return render_template('character_sheet.html', character=character_data)

@app.route('/roll-attributes/<distribution_type>')
def roll_attributes(distribution_type):
    """API para rolar atributos (usado pelo JavaScript)"""
    attributes = generate_attributes(distribution_type)
    return attributes

if __name__ == '__main__':
    app.run(debug=True)