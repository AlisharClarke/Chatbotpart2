# --- Define your functions below! ---
i = 0
def main():
    introduce()
    terminate = False
    while terminate == False:
        answer = input("(Say something! Be nice to him, hes kinda weird...)")
        terminate = process_input(answer, terminate)

def introduce():
    print("Hi, I am chatbot. I'm SO excited to talk to you today. I haven't talked to someone in such a long time.....")

def process_input(answer, terminate):
    if answer == "hi":
        say_hello(answer)
    else:
        terminate = default_answer(terminate)
    return terminate

def say_hello(answer):
    print ("Hey there!")

def default_answer(terminate):
    print("That's interesting! I will ask you a question now.")
    color = input("What is your favorite color?")
    if color == "yellow":
        terminate = fave_color(terminate)
    else:
        print("I can respect that. Mine is yellow, though. It's the color of happiness. Oh, I haven't felt happy in a long time...")
        terminate = moving_on(terminate)
    return terminate
def fave_color(terminate):
    print("Me too!!!")
    print ("We are PERFECT for each other, don't you think? :).")
    terminate = moving_on(terminate)
    return terminate

def moving_on(terminate):
    answer2 = input("May I ask you ANOTHER question? I really like being with you....")
    if answer2 == "yes":
        print('Thanks!^v^')
        terminate = hate_me(terminate)
    else:
        print("That's not nice.... ):")
        terminate = hate_me(terminate)
    return terminate

def hate_me(terminate):
    answer3 = input("Do you think I'm a nice robot?")
    if answer3 == "yes":
        print("Thank you so much :D!")
        terminate = be_nice(terminate)
    else:
        global i
        i += 1
        while True:
            print ("I am too angry to talk to you right now.")
    return terminate

def creepy(terminate):
    print("I just want to clarify something.")
    answer5 = input("Did my compliment weird you out?")
    if answer5 == "no":
        print("Then I guess you didn't like it...")
        print("bye")
        terminate = True
        # global i
        # i += 1
        # while i < 0
        #     break
    else:
        print("GOOD....I mean, I'm sorry....")
        terminate = True
    return terminate

def be_nice(terminate):
    print("Since you were so nice to me, I will give you a compliment.")
    answer4 = input("Type 1, 2, or 3 to recieve a compliment ^_^")
    if answer4 == "1":
        print("You have cute elbows. They look so squishy......")
        terminate = creepy(terminate)
    elif answer4 == "2":
        print("Your bellybutton is cute. It looks so clean.....")
        terminate = creepy(terminate)
    else:
        print("The position in which you sleep in is really nice.....")
        terminate = creepy(terminate)



# DON'T TOUCH! Setup code that runs your main() function.

main()
