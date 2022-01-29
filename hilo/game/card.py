# import the random library to genereate random numbers
import random


class Card:
    """A card with a number from 1 to 13 on it.

    The responsibility of Card is to keep track of the card drawn and calculate the points for
    it.

    Attributes:
        value (int): The number on the card drawn.
    """

    def __init__(self):
        """Constructs a new instance of Cards.

        Args:
            self (Cards): An instance of Cards.
        """
        self.value = 0
        self.points = 0

    def draw(self):
        """Generates a new random value and calculates the points for the card drawn.

        Args:
            self (Cards): An instance of a card.
        """
        # Still need to work on how points are calculated and awarded!
        self.value = random.randint(1, 13)

        self.points = 100 if True else -75

