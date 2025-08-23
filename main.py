from services.character_creator import CharacterCreator

def main():
    creator = CharacterCreator()
    character = creator.create_character()
    
    print("\n" + "=" * 60)
    character.show_detailed_sheet()
    print("\nPrepare-se para a aventura! ⚔️\n")

if __name__ == "__main__":
    main()