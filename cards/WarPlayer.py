import Player


class WarPlayer(Player):

    def __init__(self, name, deck):
        super().__init__(self, name)
        self.hand = deck

    def draw_card(self):
        super().draw_card()

    def play_card(self):
        current_card = self.hand.draw_card()
        self.card_in_play

