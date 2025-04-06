import random
import time


class GameRules:
    def __init__(self, rules):
        """
        rules: dict dove ogni chiave è una mossa, e il valore è la lista di mosse che batte.
        """
        self.rules = rules
        self.valid_moves = set(rules.keys())

    def is_valid_move(self, move):
        return move in self.valid_moves

    def get_random_move(self):
        return random.choice(list(self.valid_moves))

    def determine_winner(self, move1, move2):
        if move1 not in self.rules or move2 not in self.rules:
            raise ValueError(f"Mossa non riconosciuta: {move1} o {move2}")
        if move1 == move2:
            return 0
        elif move2 in self.rules[move1]:
            return 1
        elif move1 in self.rules[move2]:
            return 2
        else:
            raise ValueError(f"Regole non definite per: {move1} vs {move2}")


def simulate_computer_thinking():
    print("🤖 Il computer sta pensando", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print()


def get_computer_choice(game_rules):
    simulate_computer_thinking()
    return game_rules.get_random_move()


def get_player_move(game_rules):
    move = input(f"\nScegli una mossa {tuple(game_rules.valid_moves)}: ").lower().strip()
    while not game_rules.is_valid_move(move):
        move = (
            input(f"Mossa non valida! Scegli tra {tuple(game_rules.valid_moves)}: ").lower().strip()
        )
    return move


def play_round(mode, game_rules):
    if mode == "human":
        player_move = get_player_move(game_rules)
        print("\n🤖 Il computer sta per fare la sua scelta...")
        computer_move = get_computer_choice(game_rules)
        print("\nIl computer sceglie:", computer_move)
        move1, move2 = player_move, computer_move
    else:
        print("\n🤖 Computer 1 sta pensando...")
        move1 = get_computer_choice(game_rules)
        print("\n🤖 Computer 2 sta pensando...")
        move2 = get_computer_choice(game_rules)
        print("\nComputer 1 sceglie:", move1)
        print("Computer 2 sceglie:", move2)

    result = game_rules.determine_winner(move1, move2)
    if result == 0:
        print("\nPareggio! 😐")
    elif mode == "human":
        print("\nHai vinto! 🎉" if result == 1 else "\nIl computer ha vinto! 😢")
    else:
        print(f"\nComputer {result} vince! 🎉")


def main():
    print("👋 Benvenuto a Carta, Forbice e Sasso!")

    # Regole del gioco (estendibili)
    RULES = {"carta": ["sasso"], "sasso": ["forbice"], "forbice": ["carta"]}

    # Possibile estensione:
    # RULES = {
    #     'sasso': ['forbice', 'lucertola'],
    #     'forbice': ['carta', 'lucertola'],
    #     'carta': ['sasso', 'spock'],
    #     'spock': ['forbice', 'sasso'],
    #     'lucertola': ['carta', 'spock']
    # }

    game_rules = GameRules(RULES)

    mode = input(
        "\nModalità di gioco: \n\n"
        " 1: Umano vs Computer\n"
        " 2: Computer vs Computer\n\n"
        "Inserisci 1 o 2: "
    ).strip()
    while mode not in ["1", "2"]:
        mode = input("Inserisci 1 o 2: ").strip()

    game_mode = "human" if mode == "1" else "computer"

    while True:
        play_round(game_mode, game_rules)
        again = input("\nVuoi giocare un altro round? (si/no): ").lower().strip()
        if again != "si":
            break

    print("\n\nGrazie per aver giocato!")


if __name__ == "__main__":
    main()
