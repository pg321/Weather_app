import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Saachi")
    while True:
        x = input("Enter what you want to speak:")
        if x == "q":
            os.system("espeak 'bye bye friend'")
            break
        command = (f"espeak '{x}'")
        os.system(command)
