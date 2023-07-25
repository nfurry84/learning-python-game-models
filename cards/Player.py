# import to define player as an abstract class
from abc import ABC, abstractmethod
from packs import Deck, Card


class Player(ABC):
    """
    Card Game Player instance
    """
    def __init__(self, name):
        self.name = name
        self.draw_pile
        self.hand
        self.discard_pile
        self.card_in_play

    @abstractmethod
    def draw_card(self):
        """
        Draws the top card from draw_pile and adds it to players hand
        :return:
        """
        card = self.draw_pile.pop(0)
        self.hand += list(card)

    @abstractmethod
    def play_card(self):
        pass

