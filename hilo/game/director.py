from game.card import Card
from game.format import color


class Director:
    """
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Cards]): A list of Cards instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        card = Card()
        self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_initial()
            self.do_updates()
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to draw a card.

        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Is the next card " + color.BOLD + "Higher" + color.END + " or " + color.BOLD + "Lower? [h/l] ")
        
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
      
        for i in range(len(self.cards)):
           card = self.cards[i]
           card.draw()
           self.score = card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to draw again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "

        print("The next card is a " + color.RED + f"{values}" + color.END)
        print("Your score is: " + color.BLUE + f"{self.total_score} \n" + color.END)
        self.is_playing == (self.score > 0)
        play_again = input("Would you like to play again? (y/n) ")
        self.is_playing = (play_again == "y")
    
    def do_initial(self):
        """Does the initial setup of the game and draws the first card. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        for i in range(len(self.cards)):
           card = self.cards[i]
           card.draw()

        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "

        print("Your card is a " + color.RED + f"{values}" + color.END)
        self.is_playing == (self.score > 0)