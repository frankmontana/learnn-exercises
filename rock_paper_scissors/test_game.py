import unittest
from game import GameRules


class TestGameRules(unittest.TestCase):

    def setUp(self):
        """Prepara l'ambiente di test con le regole base del gioco (carta, sasso, forbice)"""
        self.rules = {"carta": ["sasso"], "sasso": ["forbice"], "forbice": ["carta"]}
        self.game_rules = GameRules(self.rules)

    def test_valid_move(self):
        """Verifica che il gioco riconosca correttamente le mosse valide e invalide"""
        print("\nTest 1: Controllo mosse valide e invalide")
        try:
            self.assertTrue(self.game_rules.is_valid_move("carta"))
            self.assertFalse(self.game_rules.is_valid_move("spock"))
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: il controllo delle mosse valide non funziona correttamente")
            raise

    def test_get_random_move_returns_valid(self):
        """Verifica che la mossa casuale del computer sia sempre una mossa valida"""
        print("\nTest 2: Controllo mosse casuali del computer")
        try:
            for _ in range(10):
                move = self.game_rules.get_random_move()
                self.assertIn(move, self.rules)
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: la mossa casuale del computer non è valida")
            raise

    def test_draw(self):
        """Verifica che il gioco riconosca correttamente un pareggio (stessa mossa)"""
        print("\nTest 3: Controllo situazione di pareggio")
        try:
            result = self.game_rules.determine_winner("carta", "carta")
            self.assertEqual(result, 0)
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: il pareggio non viene riconosciuto correttamente")
            raise

    def test_player_wins(self):
        """Verifica che il gioco riconosca correttamente quando vince il giocatore 1"""
        print("\nTest 4: Controllo vittoria giocatore 1")
        try:
            result = self.game_rules.determine_winner("carta", "sasso")
            self.assertEqual(result, 1)
            print("OK! ✅")
        except AssertionError:
            print(
                "❌ Test fallito: la vittoria del giocatore 1 non viene riconosciuta correttamente"
            )
            raise

    def test_computer_wins(self):
        """Verifica che il gioco riconosca correttamente quando vince il giocatore 2"""
        print("\nTest 5: Controllo vittoria giocatore 2")
        try:
            result = self.game_rules.determine_winner("carta", "forbice")
            self.assertEqual(result, 2)
            print("OK! ✅")
        except AssertionError:
            print(
                "❌ Test fallito: la vittoria del giocatore 2 non viene riconosciuta correttamente"
            )
            raise

    def test_invalid_match_raises(self):
        """Verifica che il gioco sollevi un errore quando si usano mosse non definite nelle regole"""
        print("\nTest 6: Controllo gestione mosse non valide")
        try:
            custom_rules = {"carta": ["sasso"]}  # incomplete rules
            game = GameRules(custom_rules)
            with self.assertRaises(ValueError):
                game.determine_winner("forbice", "sasso")
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: il gioco non gestisce correttamente " "le mosse non valide")
            raise

    def test_extensible_rules_structure(self):
        """Verifica che il gioco funzioni anche con regole estese (es: aggiunta di spock e lizard)"""
        print("\nTest 7: Controllo regole estese (spock e lizard)")
        try:
            extended_rules = {
                "sasso": ["forbice", "lizard"],
                "forbice": ["carta", "lizard"],
                "carta": ["sasso", "spock"],
                "spock": ["forbice", "sasso"],
                "lizard": ["carta", "spock"],
            }
            extended_game = GameRules(extended_rules)
            self.assertTrue(extended_game.is_valid_move("spock"))
            self.assertEqual(extended_game.determine_winner("spock", "sasso"), 1)
            self.assertEqual(extended_game.determine_winner("carta", "spock"), 1)
            self.assertEqual(extended_game.determine_winner("lizard", "spock"), 1)
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: le regole estese non funzionano " "correttamente")
            raise

    def tearDown(self):
        print("----------------------------------------------------------------------")


if __name__ == "__main__":
    print("\n=== Test Carta, Sasso, Forbice ===")
    unittest.main(verbosity=1)
