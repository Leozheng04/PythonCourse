import random 
from Project3.words import words

random_word = random.choice(words)

def hangman(word:str, life_amount:int) -> None:
    life = life_amount
    count = 0
    size = len(word)
    arr = ["*"] * size
    guesses = "".join(arr)
    guessed_already = []
    while guesses != word:
        if life == 0:
            print(f"You lose!. The word is {word}.")
            return
        
        print(f"Your current guesses are: {guesses} and your current chances are: {life}")
        temp = input("Take another guess on a character or enter wild for a wild guess: ").strip().lower()

        if (temp == "wild"):
            count += 1
            wild_guess = input("Enter your wild guess: ").strip().lower()
            if wild_guess == word:
                print(f"\nThe answer is {word}!")
                print(f"You win with a total of {count} guesses")
                return
            life -= 1
            print(f"Nope! (wild guess) you got {life} lives left")
            continue

        if len(temp) != 1 or not temp.isalpha():
            temp = input("Please enter a character (a-z): ").strip().lower()

        if temp in guessed_already:
            temp = input("You already gussed that character enter another character: ").strip().lower()
        
        else:
            found = False
            guessed_already.append(temp)
            for i,letter in enumerate(word):
                if temp == letter:
                    found = True
                    arr[i] = temp
            guesses = "".join(arr)
            count += 1
            if found == False:
                life -= 1
    print(f"\nThe answer is {word}!")
    print(f"You win with a total of {count} guesses")

hangman(random_word,6)

    
    


