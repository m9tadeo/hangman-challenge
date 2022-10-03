class Hangman:
    """Class defining Hangman. A game in game.py file in utils folder"""

    import random
    possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'mug', 'book', 'lamp'] ##list of words to find
    word_to_find = random.choice(possible_words) ##randomly selected word to find
    list_word_to_find = list(word_to_find) ##word to find converted to list (e.g. ['b','e','c','o','d','e'])
    well_guessed_letters = ['_'] * len(list_word_to_find) ##list of letters to be guessed by the user
    bad_guessed_letters = [] ##list of letters guessed by the user that is NOT in the word to find
    turn_count = 0 ## # of turns
    error_count = 0 ## # of errors
    lives = 5 #lives counter

    def __init__(self):
        self.result = "start"

    def play():
        """Function that will ask user to input a letter, check if the input is valid, check if the letter is one of the 
        letters in the word to find, and add input to well guessed letters or bad guessed letters """
        valid_input = False
        idx = 0
        check_input = 0
        user_input = input("Please enter a letter: ") ##user input letter
        while valid_input is False:    ##check for user input validity
            if len(user_input) == 1 and user_input.isalpha(): ##input is one character and a letter
                valid_input = True
                Hangman.turn_count =+ 1
            else:
                Hangman.error_count =+ 1
                user_input = input("Please enter one letter only: ") 
                ##ask user to input again if input is not one character and not a letter
        for letter in Hangman.list_word_to_find: ##check if user input is one of the letters
            if user_input == letter:
                Hangman.well_guessed_letters[idx] = user_input ##add user input to well guessed letters
                idx =+ 1 ##next index
                check_input =+1 ##checker if input is one of the letters
            else:
                idx =+ 1 ##next index
        if check_input == 0: ##check if input did not match at least one of the letters of word to find
            Hangman.bad_guessed_letters.append(user_input) ##add user input to bad guessed letters
            Hangman.error_count =+ 1 ##add to error count
            Hangman.lives =- 1 ##subtract a life
            Hangman.result = 'bad_guessed'
        if check_input > 0: ## check if user has guessed the word to find
            for item in Hangman.well_guessed_letters:
                if item == '_': ##check if there are letters left to find
                    Hangman.result = 'well_guessed'
                    break
                else:
                    continue
            Hangman.result = 'well_played' ##user has guessed word to find
        return Hangman.result

    def game_over():
        """Function that will stop the game and display 'game over...'"""
        print("game over...")
        Hangman.result = 'game_over'
        return Hangman.result

    def well_played():
        """Function that will tell the user they have found the word to find"""
        print(f"You found the word: {Hangman.word_to_find} in {Hangman.turn_count} turns with {Hangman.error_count} errors!")
        Hangman.result = 'game_over'
        return Hangman.result

    def start_game():
        """Function that will call all the other functions to play the game"""
        while Hangman.result != 'game_over': ##check if game is not over
            if Hangman.result == 'start': ##start of game
                print("Welcome to Hangman!")
                Hangman.result = Hangman.play()
            elif Hangman.result == 'bad_guessed':
                if Hangman.lives > 0: ##check if user has lives left
                    print("Well guessed letters: ", Hangman.well_guessed_letters)
                    print("Bad guessed letters: ", Hangman.bad_guessed_letters)
                    print("Life: ", Hangman.lives)
                    print("Errors: ", Hangman.error_count)
                    print("Turns: ", Hangman.turn_count) 
                    Hangman.result = Hangman.play()
                else: ##call game over if user has no lives left
                    Hangman.result = Hangman.game_over()
            elif Hangman.result == 'well_guessed': ##play again
                print("Well guessed letters: ", Hangman.well_guessed_letters)
                print("Bad guessed letters: ", Hangman.bad_guessed_letters)
                print("Life: ", Hangman.lives)
                print("Errors: ", Hangman.error_count)
                print("Turns: ", Hangman.turn_count)
                Hangman.result = Hangman.play()
            elif Hangman.result == 'well_played':  ##user has guessed the word
                Hangman.result == Hangman.well_played()