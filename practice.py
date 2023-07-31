#!/usr/bin/env python
# coding: utf-8

# # factorial
# 

# In[3]:


n=int(input("Enter the number:"))
for i in range(1,n):
    n=n*i
print(n)


# In[4]:


print("hello world")


# In[5]:


n=int(input("enter no 1"))
m=int(input("enter no 2"))
print("sum=",n+m)


# In[7]:


import math
sqrt = math.sqrt(n)
print(sqrt)


# In[8]:


#area= breadth*heaight
print("area=",n*m)


# In[10]:


import math
z=10
x1,x2 = math.roots(n,m,z)
print(x1,x2)


# In[15]:


def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
        
    
    
    
    return factorial
for j in range (10):
    print(factorial(j))


# In[17]:


x=10
y=12
temp=x
x=y
y=temp
print(x,y)


# In[26]:


#fizzbuzz
for i in range (1,101):
    if (i%5==0 and i%3==0):
        print("fizzbuzz")
    elif (i%5==0):
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)


# In[36]:


def fizz_buzz(n):
    for i in range (1,n+1):
        if (i%5==0 and i%3==0):
            print("fizzbuzz")
        elif (i%5==0):
            print("buzz")
        elif(i%3==0):
            print("fizz")
        else:
            print(i)
if __name__ == "__main__":
    print(fizz_buzz(100))


# # rock paper scissors

# In[59]:


import random
def get_user_choice():
    choices=["rock","paper","scissors"]
    while True:
        user_choice = input("enter the choice ")
        if user_choice in choices:
            return user_choice
        else:
            print("wrong input by the user")
            


# In[60]:


def get_computer_choice():
    return random.choice(["rock","paper","scissors"])
    


# In[61]:


def winning(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock" and computer_choice == "paper":
        return "you lose"
    elif user_choice == "paper" and computer_choice == "rock":
        return "you win"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "you win"
    elif user_choice == "paper" and computer_choice == "rock":
        return "you win"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "you lose"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "you win"
    
    


# In[62]:


def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("you chose:",user_choice)
    print("computer chose:",computer_choice)
    print(winning(user_choice,computer_choice))
if __name__ == "__main__":
    main()


# 
# # hangman
# 

# In[67]:


def get_random_word():
    words = ["hi","guys","my","name","is","biyas"]
    return random.choice(words)
def get_user_guesses():
    while True:
        guess = input("guess a letter ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("invalid guess")
def reveal_letter(word,guess):
    revealed_word=""
    for letter in word:
        if letter == guess:
            revealed_word += "_"
    return revealed_word
def game_over(revealed_word):
    if "_" not in revealed_word:
        return True 
    else:
        return False
def main():
    word=get_random_word()
    revealed_word = ""
    lives=6
    while not game_over(revealed_word):
        guess = get_user_guesses()
        revealed_word = reveal_letter(word,guess)
        if guess not in word:
            lives -=1
            print(revealed_word)
            if lives  == 0:
                print("game over")
                break
    else:
        print("you won")
if __name__ == "__main__":
    main()


# In[68]:


import random

def get_random_word():
    words = ["python", "programming", "machine learning", "artificial intelligence", "data science"]
    return random.choice(words)

def get_user_guess():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid guess. Please guess a single letter.")

def reveal_letter(word, guess):
    revealed_word = ""
    for letter in word:
        if letter == guess:
            revealed_word += letter
        else:
            revealed_word += "_"
    return revealed_word

def is_game_over(revealed_word):
    if "_" not in revealed_word:
        return True
    else:
        return False

def main():
    word = get_random_word()
    revealed_word = ""
    lives = 6
    while not is_game_over(revealed_word):
        guess = get_user_guess()
        revealed_word = reveal_letter(word, guess)
        if guess not in word:
            lives -= 1
        print(revealed_word)
        if lives == 0:
            print("You lose!")
            break
    else:
        print("You win!")

if __name__ == "__main__":
    main()


# In[69]:


import random

def choose_random_word():
    word_list = ["hi","my","name","is","biyas","nice","to","meet","you","guys"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print("Current word:", display)

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")

    else:
        print("\nGame over. The word was:", word)

if __name__ == "__main__":
    hangman()


# In[5]:


import random
def random_words():
    words=["hi","my","name","is","biyas","nice","to","meet","you","guys"]
    return random.choice(words)


# In[10]:


def display_words(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display +="_"
    return display
def hangman():
    word=random_words()
    guessed_letters=[]
    attempts=6
    print("welcome to the game/n let's have some fun")
    while attempts>0:
        print(" attempts left:",attempts)
        display = display_words(word,guessed_letters)
        print("current word:",display)
        if "_" not in display:
            print("you win ",word)
            break
        guess = input("guess a letter").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("wrong input ")
            continue
        if guess in guessed_letters:
            print("you already guessed this letter")
            continue
    
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print("incorret guess")
    else:
        print("game over, the correct word was",word)
            


# In[11]:


if __name__ == "__main__":
    hangman()


# In[ ]:





# 
# # random no generation
# 

# In[17]:


import random
def random_n_gen(min_val,max_val):
    return random.randint(min_val,max_val)
def main():
    number=random_n_gen(1,100)
    print("random no=",str(number))
if __name__ == "__main__":
    main()


# In[35]:


import math
def quadratic(a,b,c):
    x=(b*b)-(4*a*c)
    x1=(-b+math.sqrt(x))/2*a
    x2=(-b-math.sqrt(x))/2*a
    return x1,x2

if __name__ == "__main__":
    a = float(input("enter coefficient a "))
    b = float(input("enter coefficient b "))
    c = float(input("enter coefficient c "))
    print("roots",quadratic(a,b,c))
        
        


# In[ ]:





# In[ ]:




