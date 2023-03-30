import os

if __name__ == '__main__':
    print("Welcome to this small and cute project")
    while True:
        x = input("What you want to speak: ")
        if x == "!":
            os.system("See you Soon! Bye")
            break
        command = f"eSpeak {x}"
        os.system(command)
