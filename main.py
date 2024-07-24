from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

word = choice(word_list)                    

display = ['_'] * len(word)

print(logo)
print(f'Pssst, the word is {word}.')

while '_' in display and lives > 0:
  guess = input('Guess a letter: ').lower()
  if guess in display:
    print('You\'ve already guessed this letter.')
  for pos in range(len(word)):
    letter = word[pos]
    if guess == letter:
      display[pos] = guess
  if guess not in word:
    print(f'you guessed {guess}, that\'a not in the word, you lose a life.')
    lives -= 1
  print(' '.join(display))
  print(stages[lives])

if lives == 0:
  print(stages[0])
  print('You have lost.')
  print('You can try again!')
else:
  print('You have won!')
