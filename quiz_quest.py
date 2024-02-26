import tkinter as tk
# import p6

root = tk.Tk()
root.geometry("350x360")
root.title("Questionnaire")
root.configure(background="#F3CCF3")

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



main_page = tk.Frame(root, bg="#F3CCF3")
main_page.grid(row=0, column=0, sticky="nsew")

question_page = tk.Frame(root,bg = "#F3CCF3")
question_page.grid(row=0, column=0, sticky="nsew")

feedback_page = tk.Frame(root,bg="#F3CCF3")
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
b_button = tk.Button(main_page, text="<-", fg="#392467", bg="#FFE5E5")
b_button.grid(row = 0, column = 0, padx = 5, pady = 5)
for i in range(1, 11):
    for j in range(5):
        index = (i-1) * 5 + j
        button = tk.Button(main_page, text=f"{index + 1}", command=lambda idx=index: display_question(main_page, idx), font=("Arial", 9, "bold"), width=7, fg="#392467", bg="#F6D6D6")
        button.grid(row=i, column=j, padx=5, pady=3)
        question_buttons.append(button)

        if index != 0:
            button.config(state="disabled")


switch_frame(main_page)

root.mainloop()
