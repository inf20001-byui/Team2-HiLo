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
        return draw_card

    #this is the function i'm working at.
    #I'm trying to assign a value to the user's input, so we can use if statements to
    #decide the scores.
    def get_score(self):
        self.guess = ""
        if self.first_value < self.second_value:
            self.guess.lower() == "h"
        elif self.first_value > self.second_value:
            self.guess.lower() == "l"
        else:
            print("Please type H or L")

        if self.get_inputs.lower() == self.guess:
            self.score = 100
        elif self.get_inputs.lower() != self.guess:
            self.score = -75


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

        
        self.second_value = 0
        for i in range(len(self.cards)):
            card = self.cards[i]
            self.second_value += card.value


        print()
        print("The next card was " + color.RED + f"{self.second_value}" + color.END)

        #I added a score message to the user knows if the guess was right or not
        if self.score == 100:
            print("Great! You've earned 100 Points")
        elif self.score == -75:
            print("Too bad! You've lost 75 Points")

        print("Your score is: " + color.BLUE + f"{self.total_score} \n" + color.END)

        self.is_playing == (self.total_score > 0)
        play_again = input("Would you like to play again? (y/n) ")
        print()
        self.is_playing = (play_again == "y")
        #I added this if Statement so if the user decides to leave the game it shows the final score and a thank you message
        if play_again == "n":
            print()
            print("Your final score is: " + color.BLUE + f"{self.total_score} \n" + color.END)
            print()
            print("Thank you for playing!")
        


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

        self.first_value = 0 
        for i in range(len(self.cards)):
            card = self.cards[i]
            self.first_value += card.value

        print("The card is " + color.RED + f"{self.first_value}" + color.END)

        while self.score > 0:
            self.is_playing = True
        


