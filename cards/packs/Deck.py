import Card


class Deck:
    """
    Represents a deck of cards
    Could be the entire standard playing card deck, a players hand, or cards in a discard pile
    """
    def __init__(self):
        self.cards = list(Card.build_standard_suit('Hearts') +
                          Card.build_standard_suit('Spades') +
                          Card.build_standard_suit('Diamonds') +
                          Card.build_standard_suit('Clubs'))

    def __init__(self, my_cards):
        self.cards = my_cards

    def add_card(self, card):
        """
        Add card to deck
        :param card: The card to be added to the deck
        :return:
        """
        self.cards.append(card)

    def remove_card(self, card):
        """
        Removes the card from the deck
        :param card:
        :return:
        """
        index = self.cards.index(card)
        card.pop(index);

    def shuffle_deck(self):
        """
        Shuffles the deck
        :return:
        """
        self.cards.shuffle()

    def draw_card(self):
        """
        Draws the top card from the deck
        This is also removes the card from the current deck
        :return:
        """
        return self.cards.pop(0)