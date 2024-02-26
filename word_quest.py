import tkinter as tk
from tkinter import messagebox
import random
import time

root = tk.Tk()
root.title('Word Guessing Game')
root.configure(bg='#F3CCF3')
root.geometry("350x360")

def sleep(ms):
    root.update()
    time.sleep(ms / 1000)

def check_guess():
    global turns, guesses
    guess = guess_entry.get().lower()
    if len(guess) != 1 or not guess.isalpha():
        reason_label.config(text='Invalid Input! Please enter a single alphabetical character.')
        sleep(200)
        reason_label.config(text='')
        return
    if guess not in guesses:
        guesses += guess
        guess_entry.delete(0, tk.END)
        if guess in word.lower():
            for index, char in enumerate(word.lower()):
                if char in guesses:
                    word_label.config(text=word_label.cget('text')[:index*2] + char + word_label.cget('text')[index*2+1:])
            if '_' not in word_label.cget('text'):
                reason_label.config(text='Congratulations! You won!')
                return
        else:
            turns -= 1
            if turns == 0:
                reason_label.config(text=f'Sorry, you lost. The correct word was: {word}')
                word_label.config(text=word)
                guess_entry.config(state=tk.DISABLED)
            else:
                reason_label.config(text=f'Wrong guess! You have {turns} more turns left.')
    else:
        reason_label.config(text='You already guessed that letter.')

def start_game():
    global word, turns, guesses      
    guesses = ''
    turns = 10
    words = ['Donkey', 'Aeroplane', 'America', 'Program', 'Python', 'Language', 'Cricket', 'Football', 'Hockey', 'Spaceship', 'Bus',
              'Flight', 'Chocolate', 'Beach', 'Guitar','Cat', 'Dog', 'Sun', 'Moon', 'Star', 'Tree', 'Flower', 'House', 'Car', 'Ball',
              'Book', 'Apple', 'Banana', 'Pencil', 'Chair', 'Bed', 'Clock', 'Rainbow', 'Butterfly', 'Fish', 'Bird', 'Robot', 
              'Computer', 'Cake', 'Pizza', 'Ice Cream', 'Milk', 'Shoe', 'Hat']
    hints = ['It\'s an animal often seen on farms.', 
             'It\'s a mode of transportation that flies in the sky.', 
             'It\'s a country known for its democratic system and diverse culture.', 
             'It\'s a set of instructions that a computer can execute.', 
             'It\'s a popular programming language known for its simplicity and versatility.', 
             'It\'s a system of communication using words and sounds.', 
             'It\'s a popular sport played with a bat and a ball.', 
             'It\'s a sport played between two teams with a spherical ball.', 
             'It\'s a sport played on ice with sticks and a puck.', 
             'It\'s a vehicle designed for travel in outer space.', 
             'It\'s a large motor vehicle used for transporting passengers by road.', 
             'It\'s a journey made by air, especially in a plane.', 
             'It\'s a sweet treat made from cocoa beans.', 
             'It\'s a sandy shore by the ocean or sea.', 
             'It\'s a musical instrument with strings.',
             'It\'s a small furry animal that says "meow".', 
            'It\'s a loyal pet that says "woof".', 
            'It shines brightly in the sky during the day.', 
            'It lights up the night sky.', 
            'It twinkles and glitters in the sky.', 
            'It grows tall and has leaves.', 
            'It blooms and smells nice.', 
            "It's a place where people live.", 
            "It's a vehicle with four wheels.", 
            "It's round and you can bounce it.", 
            'You read it to learn new things.', 
            "It's a sweet and juicy fruit.", 
            "It's a yellow fruit that monkeys love.", 
            'You use it to write or draw.', 
            'You sit on it.', 
            'You sleep on it.', 
            'It tells you the time.', 
            "It's a colorful arc in the sky after rain.", 
            'It starts as a caterpillar and turns into a beautiful insect.', 
            'It swims in water.', 
            'It has wings and can fly.', 
            "It's a machine that can do tasks automatically.", 
            "It's an electronic device for playing games and browsing the internet.", 
            "It's a delicious dessert.", 
            "It's a popular food with toppings.", 
            "It's a frozen treat.", 
            'It comes from cows.', 
            'You wear it on your feet.', 
            'You wear it on your head.']
    
    word = random.choice(words)
    hint = hints[words.index(word)]
    hint_label.config(text=f'Hint: {hint}')
    word_label.config(text=' '.join(['_' if char.isalpha() else char for char in word]))

    guess_entry.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)
    guess_entry.focus()


back_button = tk.Button(root, text='<-', fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"))
back_button.grid(row=0, column=0, sticky="nw", pady=10)

hint_label = tk.Label(root, text='', bg='#F3CCF3', font=('Arial', 14), wraplength=300)
hint_label.grid(row=1, column=0)

word_label = tk.Label(root, text='', bg='#F3CCF3', font=('Arial', 24))
word_label.grid(row=2, column=0)

guess_entry = tk.Entry(root, font=('Arial', 16), width=10)
guess_entry.grid(row=3, column=0, padx=10, pady=10)

guess_button = tk.Button(root, text='Guess', command=lambda: check_guess(), fg="#392467", bg = "#FFE5E5", font=('Arial', 10 ,"bold"))
guess_button.grid(row=4, column=0, padx=10, pady=10)

reason_label = tk.Label(root, text="", font="Arial 15 bold", fg="black", relief="ridge", width=29, background="#F3CCF3", wraplength=300)
reason_label.grid(row=5, column=0, pady=10)

next_button = tk.Button(root, text='Next', command=start_game, fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"))
next_button.grid(sticky="se", pady=10)


start_game()
root.mainloop()