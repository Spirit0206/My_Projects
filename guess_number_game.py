import win32com.client as wincom
import random

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

# welcome text

getname = "welcome! Enter your name"
print(getname)
speak.Speak(getname)
name = input()


# welcome user by pronouncing their name

# coardinating rules to play the game

def mymethod():
    welcome = f"welcome {name}! This is guess the number game and the instruction to play it are given bewlow"
    time.sleep(1)
    print(welcome)
    speak.Speak(welcome)
    instruction1 = "Some of the rules to play this game are as follows-"
    print(instruction1)
    speak.Speak(instruction1)

    rule1 = " rule number one! you can to guess the number between 1 to 100"
    print("1. you can to guess the number between 1 to 100")
    speak.Speak(rule1)
    rule2 = "rule number two! you get only 10 attempts to guess the number"
    print("2. you get only 10 attempts to guess the number.")
    speak.Speak(rule2)
    rule3 = "rule number three! If you will not guess the number , the game will be over and you will loss"
    print("3. If you will not guess the number , the game will be over and you will loss.")
    speak.Speak(rule3)
    rule4 = "rule number four! if you guess the number within 10 attempts you will win"
    print("4. If you guess the number within 10 attempts you will win.")
    speak.Speak(rule4)
    rule5 = "rule number five! at every atep you will get the instruction like number is too high or too low etc"
    print("5. At every step you will get the instruction like number is too high or too low etc.")
    speak.Speak(rule5)
    rule6 = "rule number six! lastly if you want to play tha game again just press 1 and if you want to exit just press 2 from your keyboard."
    print("6. Lastly if you want to play tha game again just press 1 and if you want to exit just press 2 from your keyboard.")
    speak.Speak(rule6)


# function to check weitheer the number guesssed is right or not

def check():
    randnum = random.randint(1, 101)
    attempts = 0
    while attempts <= 10:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < randnum:
                low = "Too low! Try a higher number."
                print(low)
                speak.Speak(low)
            elif user_guess > randnum:
                high = "Too high! Try a lower number."
                print(high)
                speak.Speak(high)
            else:
                congrats = f"Congratulations! You guessed the right number which is {randnum} in {attempts} attempts."
                print(congrats)
                speak.Speak(congrats)
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            speak.Speak("Invalid input. Please enter a valid number.")


# function to know user opinion weither they want to play the game or not

def guess_number():
    print("Lets go! Are you excited to play the game!")
    speak.Speak("Lets go! Are you excited to play the game!")
    try:
        while True:
            speak.Speak("Press 1 to start or 2 to exit!")
            user_choice = int(input("Press 1 to start or 2 to exit!"))
            if user_choice == 1:
                check()
            else:
                print("Thank you for playing the game now you can exit.")
                speak.Speak("Thank you for playing the game now you can exit.")
                break
    except ValueError:
        print("please enter valid number!")


if __name__ == "__main__":
    mymethod()
    guess_number()