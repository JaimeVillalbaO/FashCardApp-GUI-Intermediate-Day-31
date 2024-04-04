from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
words_dict = {}

try:
    words = pd.read_csv('./data/words_to_learn.csv')
except:
    words = pd.read_csv('./data/english_words.csv')
words_dict = words.to_dict(orient='records') #para crear el dict con el nombre de la column

def next_card():
    global current_card, flip_timer #para que no se resetee el tiempo 
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)    
    canvas.itemconfig(lenguage_text, text='English', fill='black')
    canvas.itemconfig(word_text, text=current_card['english'], fill='black')
    canvas.itemconfig(card_background, image=cardfront_img)
    flip_timer = window.after(3000, func=flip_card)
    
def is_known():
    words_dict.remove(current_card)
    # print(len(words_dict))
    next_card()
    df = pd.DataFrame(words_dict)
    df.to_csv('./data/words_to_learn.csv', index=False)
    
def flip_card():
    canvas.itemconfig(lenguage_text, text='Spanish', fill='white')
    canvas.itemconfig(word_text, text= current_card['spanish'], fill='white')
    canvas.itemconfig(card_background, image=cardback_img)    
   

window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
cardfront_img = PhotoImage(file='./images/card_front.png')
cardback_img = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image = cardfront_img)
lenguage_text = canvas.create_text(400, 150, text='', fill='black', font=('arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', fill='black', font=('arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

check_img = PhotoImage(file='./images/right.png')
check_button = Button(image=check_img, highlightthickness=0, background=BACKGROUND_COLOR, command=is_known)
check_button.grid(column=0, row=1)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()


window.mainloop()