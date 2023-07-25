class Card():
    """
    Represents a single card among a deck of cards
    """
    def __init__ (self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return f'{self.face} of {self.suit}'.title()

    def __eq__(self, other):
        if type(other) == 'Card':
            return self.face == other.face and self.suit == other.suit
        else:
            return False

    def __lt__(self, other):
        if type(other) == 'Card':
            return self.value < other.value
        elif type(other) == 'int':
            return self.value < other
        elif type(other) == 'string' and other.isnumber():
            return self.value < int(other)
        else:
            raise TypeError("Card cannot be compared to " + type(other))

    def is_number(self):
        """
        returns true if is number
        :return:
        """
        return self.face.isnumber()

    def is_face(self):
        """
        Only returns true when card is Jack, Queen, or King
        :return:
        """
        is_number = self.is_number()
        if is_number:
            return False
        elif self.face.lower() == "ace":
            return False
        else:
            return True

def build_standard_suit(suit):
    """
    Generates the appropiate cards for a single suit
    :param suit: suit name
    :return: list of cards in the suit
    """
    card_list = [Card(suit, 'Ace', 1)]
    for number in range(2,11):
        card_list.append(Card(suit, str(number), number))

    card_list += [Card(suit, 'Jack', 11), Card(suit, 'Queen', 12), Card(suit, 'King', 13)]
    return card_list