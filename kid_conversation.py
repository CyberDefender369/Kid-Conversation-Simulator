#importing random module
from random import choice

#creating list of questions
questions = ["What's your favorite color?: ",
             "What's your favorite food to eat?: ",
             "Why do kids go to school?: "]

#randomly selecting a question from list
question = choice(questions)

#answering randomly selected question
answer = input(question).strip().lower()

#adequate answer that stops kid from asking why
stop = "just because"

#while loop that stops running only when sufficient answer is given
while answer != stop:
    answer = input("why?: ").strip().lower()
    
print("That makes sense!")