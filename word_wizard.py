import tkinter as tk
import sqlite3
from tkinter import messagebox
import random
import time

root = tk.Tk()
root.geometry("350x360")
root.title("WORD WIZARD")
root.configure(background="#F3CCF3")

def open_game():
    def open_game1():
        game1_window = tk.Tk()
        game1_window.title('Word Quest')
        game1_window.configure(bg='#F3CCF3')
        game1_window.geometry("350x360")

        def sleep(ms):
            game1_window.update()
            time.sleep(ms / 2000)

        def check_guess():
            global turns, guesses
            guess = guess_entry.get().lower()
            if len(guess) != 1 or not guess.isalpha():
                reason_label.config(text='Invalid Input! Please enter a single alphabetical character.')
                sleep(2000)
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
                        sleep(2000)
                        reason_label.config(text='')
                        return
                else:
                    turns -= 1
                    if turns == 0:
                        reason_label.config(text=f'Sorry, you lost. The correct word was: {word}')
                        sleep(2000)
                        reason_label.config(text='')
                        word_label.config(text=word)
                        guess_entry.config(state=tk.DISABLED)
                    else:
                        reason_label.config(text=f'Wrong guess! You have {turns} more turns left.')
                        sleep(2000)
                        reason_label.config(text='')
            else:
                reason_label.config(text='You already guessed that letter.')
                sleep(2000)
                reason_label.config(text='')

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


        back_button = tk.Button(game1_window, text='<-', fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"), command=game1_window.destroy)
        back_button.grid(row=0, column=0, sticky="nw", pady=10)

        hint_label = tk.Label(game1_window, text='', bg='#F3CCF3', font=('Arial', 14), wraplength=300)
        hint_label.grid(row=1, column=0)

        word_label = tk.Label(game1_window, text='', bg='#F3CCF3', font=('Arial', 24))
        word_label.grid(row=2, column=0)

        guess_entry = tk.Entry(game1_window, font=('Arial', 16), width=10)
        guess_entry.grid(row=3, column=0, padx=10, pady=10)

        guess_button = tk.Button(game1_window, text='Guess', command=lambda: check_guess(), fg="#392467", bg = "#FFE5E5", font=('Arial', 10 ,"bold"))
        guess_button.grid(row=4, column=0, padx=10, pady=10)

        reason_label = tk.Label(game1_window, text="", font="Arial 15 bold", fg="black", relief="ridge", width=29, background="#F3CCF3", wraplength=300)
        reason_label.grid(row=5, column=0, pady=10)

        next_button = tk.Button(game1_window, text='Next', command=start_game, fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"))
        next_button.grid(sticky="se", pady=10)

        start_game()







    def open_game2():
        # game_window.withdraw()
        game2_window = tk.Tk()
        game2_window.geometry("350x360")
        game2_window.title("Quiz Quest")
        game2_window.configure(background="#F3CCF3")

        questions = [
            "Which is the largest animal in the earth?",
            "Name of the largest cat in the world?",
            "A queen bee has how many legs?",
            "Which is the fastest two-legged bird in the world?",
            "A baby giraffe is known as?",
            "An octopus has how many hearts?",
            "A butterfly has how many legs?",
            "What type of animal eats both animals and plants?",
            "Which bird can fly backward?",
            "Which is the second largest continent of the world?",
            "Which of the following continent does not have volcano?",
            "Which continent sets record for lowest temperature ever on Earth?",
            "which is the largest country in asia?",
            "How many countries are there in Africa continent?",
            "How many times the hands of a clock coincide in a day?",
            "What is the average of first five multiples of 12?",
            "Which two numbers come next in the sequence? 22, 26, 28, 32, 34, 38, 40, ?, ? (Enter answer separated by commas)",
            "40% of 280 = ?",
            "What is the HCF of 1095 and 1168?",
            "What is the area of a triangle with base 5 meters and height 10 meters?",
            "Find the odd one out: 2, 4, 7, 8, 6",
            "Find the odd one out: 3, 9, 27, 35, 45",
            "Identify the word that doesn't belong: cat, dog, horse, apple, mouse.",
            "Which word is the odd one out: happy, sad, joyful, cheerful, blue",
            "Which shape is the odd one out: circle, square, triangle, rectangle, pentagon",
            "A shopkeeper sold an article for Rs. 2500. If the cost price of the article is 2000, find the profit percent?",
            "What is the antonym of ARTIFICIAL",
            "What is the antonym of REFUSE",
            "Antonym of BEAUTIFUL",
            "Synonym of BUT (besides, behind)",
            "Synonym of HAPPY (content, detest)",
            "Where is the Sangai Festival celebrated in India?",
            "Who said, “For the next 50 Years let Mother India be the only God to be worshipped by the Indians”? ",
            "Where is the Elephant Festival celebrated every year in india?",
            "What is the Classical Dance of Tamil Nadu?",
            "How many Classical Dances are Recognised By The Sangeet Natak Akademi?",
            "Who was the first Asian to win the Nobel Prize?",
            "Who was the Composer of Vande Mataram?",
            "Who is the Father of the Indian Constitution?",
            "Which Place in India receives the Highest Rainfall annually?",
            "What is India’s rank in producing Sugarcane?",
            "In India, What is River “Yarlung Tsangpo” Known as?",
            "What is the largest planet of the Solar System according to size?",
            "Which planet in the Solar System takes the shortest revolution?",
            "Which planet in the Solar System has the highest density?",
            "What is the largest planet in our solar system",
            "What is the hottest planet in our solar system? ",
            "Which animal is featured on the emblem of the Reserve Bank of India?",
            "The words 'Satyamev Jayate' symbolizing the rule of India have been taken from which book?",
            "What is the logo of the World Wildlife Fund?",
            "Who gave the slogan of Satyamev Jayate?"
        ]

        correct_answers = [
            "blue whale",
            "siberian Tiger",
            "6",
            "ostrich",
            "calf",
            "3",
            "6",
            "omnivore",
            "humming bird",
            "africa",
            "australia",
            "antarctica",
            "china",
            "54",
            "22",
            "36",
            "44,46",
            "112",   
            "73",
            "25",
            "7",
            "35",
            "apple",
            "blue",
            "circle",
            "25%",
            "natural",
            "accept",
            "ugly",
            "besides",
            "content",
            "manipur",
            "swami vivekananda",
            "jaipur",
            "bharatanatyam",
            "8",
            "rabindranath tagore",
            "bankim chandra chatterjee",
            "dr b r ambedkar",
            "meghalaya",
            "2",
            "brahmaputra",
            "jupiter",
            "mercury",
            "earth",
            "jupiter",
            "venus",
            "tiger",
            "upanishads",
            "panda",
            "pandit madan mohan malviya"
        ]

        def switch_frame(frame):
            frame.tkraise()

        def display_question(frame, index):
            global current_question
            current_question = index
            
            switch_frame(frame)
            
            question_label.config(text=questions[index])
            
            switch_frame(question_page)

        def next_question():
            next_index = current_question + 1
            if next_index < len(questions):
                display_question(main_page, next_index)
            else:
                feedback_label.config(text="You have completed all questions!")

        def try_again():
            display_question(main_page, current_question)

        def go_back():
            switch_frame(main_page)

        def go_back1():
            switch_frame(root)



        main_page = tk.Frame(game2_window, bg="#F3CCF3")
        main_page.grid(row=0, column=0, sticky="nsew")

        question_page = tk.Frame(game2_window,bg = "#F3CCF3")
        question_page.grid(row=0, column=0, sticky="nsew")

        feedback_page = tk.Frame(game2_window,bg="#F3CCF3")
        feedback_page.grid(row=0, column=0, sticky="nsew")

        back_button = tk.Button(question_page, text="<-", command=go_back, fg="#392467", bg = "#FFE5E5")
        back_button.pack(pady=10,anchor='nw')

        question_label = tk.Label(question_page, font=("Arial", 11),bg="#F3CCF3", wraplength=300) 
        question_label.pack(pady=10)

        answer_entry = tk.Entry(question_page, font=("Arial", 11))
        answer_entry.pack(pady=10)

        submit_button = tk.Button(question_page, text="Submit",command=lambda: submit_answer(main_page, answer_entry), font=("Arial", 11,"bold"), fg="#392467", bg = "#FFE5E5")
        submit_button.pack(pady=10)

        back_button = tk.Button(feedback_page, text="<-",command=go_back, fg="#392467", bg = "#FFE5E5")
        back_button.pack(pady=10,anchor='nw')

        feedback_label = tk.Label(feedback_page, font=("Arial", 11), bg="#F3CCF3")
        feedback_label.pack(pady=20)

        try_again_button = tk.Button(feedback_page, text="Try Again",command=try_again, font=("Arial", 11,"bold"), fg="#392467", bg = "#FFE5E5")
        try_again_button.pack(pady=10)

        next_question_button = tk.Button(feedback_page, text="Next Question",command=next_question, font=("Arial", 11,"bold"), fg="#392467", bg = "#FFE5E5")
        next_question_button.pack(pady=10)


        answered = [False] * len(questions)

        def submit_answer(frame, answer_entry):

            user_answer = answer_entry.get()
            
            correct_answer = correct_answers[current_question]
            
            if user_answer.lower() == correct_answer.lower():
                feedback_label.config(text="Correct!")
                next_question_button.pack()  # Show the next question button
                try_again_button.pack_forget()  # Hide the try again button
                answered[current_question] = True
                if current_question + 1 < len(questions):
                    question_buttons[current_question + 1].config(state="normal")  # Enable next question button
            else:
                feedback_label.config(text="Incorrect! Try again")
                next_question_button.pack_forget()  # Hide the next question button
                try_again_button.pack()  # Show the try again button
            
            answer_entry.delete(0, tk.END)
            
            switch_frame(feedback_page)

        question_buttons = []
        b_button = tk.Button(main_page, text = "<-", command = game2_window.destroy, fg="#392467", bg = "#FFE5E5")
        b_button.grid(row = 0, column = 0, padx = 5, pady = 5)
        for i in range(1, 11):
            for j in range(5):
                index = (i-1) * 5 + j
                button = tk.Button(main_page, text=f"{index + 1}", command=lambda idx=index: display_question(main_page, idx),  font=("Arial", 9,  "bold"), width = 7, fg="#392467", bg = "#F6D6D6")
                button.grid(row=i, column=j, padx=5, pady=3)
                question_buttons.append(button)

                if index != 0:
                    button.config(state="disabled")


        switch_frame(main_page)



    root.withdraw()  
    game_window = tk.Tk()
    game_window.geometry("350x360")
    game_window.title("Games")
    game_window.configure(background="#F3CCF3")

    game1 = tk.Button(game_window, text="   Word Quest   ", fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"), command=open_game1)
    game1.grid(row=0, column=0, padx=100, pady=80)

    game2 = tk.Button(game_window, text="   Quiz Quest   ", fg="#392467", bg = "#FFE5E5", font=('Arial', 13 ,"bold"), command=open_game2)
    game2.grid(row=1, column=0)

    game_window.mainloop()

Tops = tk.Frame(root, bg="#F3CCF3", pady=2, width=300, height=70, relief="ridge")
Tops.grid(row=0, column=0, pady=(10, 0))

Mid = tk.Frame(root, bg="#F3CCF3", pady=2, width=300, height=150, relief="ridge")
Mid.grid(row=1, column=0)

Down = tk.Frame(root, bg="#F3CCF3", pady=2, width=300, height=80, relief="ridge")
Down.grid(row=2, column=0, pady=(0, 10))

lblTitle = tk.Label(Tops, font=("arial", 15, "bold"), text="              WORD WIZARD           ", bd=15, bg="#F3CCF3", fg="#5D3587")
lblTitle.grid(row=0, column=0)

name_label = tk.Label(Mid, font=("arial", 15, "bold"), text="Name", bd=15, bg="#F3CCF3", fg="#5D3587")
name_label.grid(row=0, column=0, padx=(10, 0))

entry_name = tk.Entry(Mid)
entry_name.grid(row=0, column=1)

age_label = tk.Label(Mid, font=("arial", 15, "bold"), text="Age", bd=15, bg="#F3CCF3", fg="#5D3587")
age_label.grid(row=1, column=0, padx=(10, 0))

entry_age = tk.Entry(Mid)
entry_age.grid(row=1, column=1)

def checker():
    name = entry_name.get()
    age = entry_age.get()
    
    if not name or not age:
        messagebox.showwarning("Incomplete Details", "Please fill all details")
    else:
        submit()
        open_game()

def submit():
    name_val = entry_name.get()
    age_val = entry_age.get()
    
    conn = sqlite3.connect("wordwizard.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS userdata (
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL
                    )''')
    cursor.execute("INSERT INTO userdata (name, age) VALUES (?, ?)", (name_val, age_val))
    conn.commit()
    conn.close()

submit_button = tk.Button(Down, text="Submit", font=("Arial", 10, "bold"), width=6, fg="#392467", bg = "#FFE5E5", command=checker)
submit_button.grid(row=0, column=0, pady=10)

root.mainloop()