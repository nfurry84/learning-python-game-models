import unittest
from cards.packs import Card


class Test_Card(unittest.TestCase):
    def test_ace_card(self):
        card = Card.Card('MySuits', 'Ace', 1)
        self.assertEqual('MySuits', card.suit)
        self.assertEqual('Ace', card.face)
        self.assertEqual(1, card.value)

    def test_suit_of_cards_count(self):
        cards = Card.build_standard_suit('TheSuits')
        self.assertEqual(13,len(cards))

    def test_suit_of_cards_suit(self):
        cards = Card.build_standard_suit('TheSuits')
        for card in cards:
            self.assertEqual('TheSuits', card.suit)


if __name__ == "__main__":
    unittest.main()