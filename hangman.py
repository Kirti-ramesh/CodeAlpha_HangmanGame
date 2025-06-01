import random
word_list=["apple","banana","mango","strawberry","orange","pomegranate"]
secret_word=random.choice(word_list)
guessed_word=["_"]*len(secret_word)
wrong_guess=0
max_attempt=6
guessed_letter=[]
print("welcome to kirti\'s hangman.find the fruit!")
while wrong_guess<max_attempt and "_" in guessed_word:
    print("\n current word"+"".join(guessed_word))
    guess = input("guess a letter:").lower()
    if guess in guessed_letter:
        print("you already guessed the letter!")
        continue
    guessed_letter.append(guess)
    if guess in secret_word:
        print("great guess!")
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                guessed_word[i]=guess
    else:
        print("wrong guess")
        wrong_guess +=1
        print(f"chance left:{max_attempt - wrong_guess}")
if "_"not in guessed_word:
    print("your guess in correct.congrats,the guessed word:",secret_word)
else:
    print("\n game over. the word was:",secret_word)