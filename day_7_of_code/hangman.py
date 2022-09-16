import random

word_list = ["mirtilo", "alcachofra", "ampulheta", "bicarbonato", "bumerangue", "camuflagem", "cleptomaniaco", "crepusculo", "empecilho", "embaixador", "enxaqueca", "estapafurdio", "inflamado", "invertebrado", "marimbondo", "nebulizador", "paralisado", "iogurte", "prodigio", "sobrevivente", "superfluo", "travesseiro", "termometro", "zodiaco", "ventilador"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

lives = 6

secret_word = ['_' for i in chosen_word]
print(f"O tamanho da palavra é: {len(secret_word)}")
print(secret_word)

end_of_game = False

guesses = []

while not end_of_game:
    guess = input("Please enter a letter: ").lower()
    guesses.append(guess)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            secret_word[position] = letter
    if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"Your lose! The word was: {chosen_word}")
    
    print(stages[lives])
    print(f"Your guessings: {guesses}")
    print(secret_word)
    
    if "_" not in secret_word:
        end_of_game = True
        print(f"You win! The word was: {chosen_word}")
