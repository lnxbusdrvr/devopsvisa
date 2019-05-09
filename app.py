# -*- coding: utf-8 -*

# Tuodaan kysymykset.py -tiedostosta luokka: Questions
from kysymykset import Question

# Määritetään kysymykset ja vastaukset
question_prompts = [
    "Puhuttaessa DevOps -käsitteestä, mitä tarkoittaa Ops?\n(a) LaiteInfra\n(b) Ohjelmointi\n(c) Oulun Palloseura\n\n",
    "Puhuttaessa DevOps -käsitteestä, mitä tarkoittaa Dev?\n(a) LaiteInfra\n(b) Ohjelmointi\n(c) Oulun Palloseura\n\n",
    "Mitä tarkoitetaan lyhenteellä CD?\n(a) Combat Disc\n(b) Continous Delivery\n(c) Jatkuva integrointi\n",
    "Mitä tarkoitetaan lyhenteellä DVD?\n(a) Dalivery Vombat Disc\n(b) Continous Delivery\n(c) Ei liity aiheseen\n\n"
    ]
    
    
# Määritetään, mitkä ovat oikeat vastaukset
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    ]


# Aliohjelma
def run_test(questions):
    score = 0
    for question in questions:          # Verrataan kåyttäjän syöttämä vastausta oikeseen vastaukseen
        answer = input(question.prompt) # otetaan vastaan käyttäjän vastaus
        if answer == question.answer:   # jos käyttäjän vastaus on yhtä suuri kuin oikea vastaus
            score += 1                  # niin lisää yksi(1) tulokseen(score)
    print("Tuloksesi " + str(score) + "/" + str(len(questions)) + "Oikein") # Tulosta pisteet ja maksimipisteet

    
# Kutsutaan aliohjelma
run_test(questions)

# Koodi kopioitu lähteestä: https://www.youtube.com/watch?v=SgQhwtIoQ7o
