from rock_paper_scissores import play_rps
from number_gussing import play_guessing


print("🎮 WELCOME TO PYTHON MINI GAMES 🎮")

while True:
    print("\nChoose a game:")
    print("1. ✊ Rock Paper Scissores")
    print("2. 🔢 Number Gussing")
    print("3. 🚪 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        play_rps()

    elif choice == "2":
        play_guessing()

    elif choice == "3":
        print("Thanks for playing! 👋")
        break

    else:
        print("❌ Invalid choice. Try again!")