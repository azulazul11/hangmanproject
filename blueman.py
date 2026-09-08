import random


def menu():
    print("BLUEMAN")
    print()
    print("1. Play")
    print("2. Exit")
    
    option = int(input("Choose an option: "))
    return option


def play():
    word = random.choice(["python", "computer", "school"])
    
    print("Let's play Blueman!")
    print("The mystery word has been selected.")
    
    letter = input("Guess a letter: ")

    if letter in word:
        print("Correct!")
    else:
        print("Wrong!")


def main():
    option = menu()

    if option == 1:
        play()

    elif option == 2:
        print("Goodbye!")

    else:
        print("Invalid option.")


main()