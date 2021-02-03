from random import choice
# Currently words are random out of a hard coded list. A bigger frequent words list could be used.
word = choice(["Secret", "Club", "Hand", "Computer", "Gearshift", "Seat", "Codeing", "Table"]) 

allowed_errors = 10
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("[]", end=" ")
    print("")
        
    guess = input(f"Allowed Errors Left {allowed_errors}, Next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
        
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
            
if done:
    print("*.*.* CONGRATULATIONS *.*.*")
    print("-----------------------------\n")
    print(f"You found the word! It was {word}!\n")
else:
    print(f"Game Over! The word was {word}!\n")