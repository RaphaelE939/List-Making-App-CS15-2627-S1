og_list = []
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
RESET = "\033[0m"
import time



def list_app():
    global og_list
    global change
    global stuff
    global position
    stuff = None
    previous_list = None
    while True:
        player_choice = input(f"{UNDERLINE}{BOLD} TO-DO LIST APP {RESET}"
                              f"\nWould you like to:"
                              f"\n{BOLD}A:{RESET} Add something to your list"
                              f"\n{BOLD}B:{RESET} Remove something from your list"
                              f"\n{BOLD}C:{RESET} Display your list"
                              f"\n{BOLD}D:{RESET} Undo a previous change"
                              f"\n{BOLD}E:{RESET} Exit the app"
                              f"\n").strip().lower()
        time.sleep(1.3)
        if player_choice == "a":
            add = input("Please type what you wish to add:"
                        "\n").strip().capitalize()
            if add == "":
                print("Invalid input, try again.")
            else:
                og_list.append(add)
                previous_list = og_list.copy()
                print(f"{add} has been added to your to do list.")
                time.sleep(1.3)

        elif player_choice == "b":
            if og_list == []:
                print("There is nothing in your todo list to remove.")
                time.sleep(1.3)
            else:
                print("At which position is the index you would like to remove? (Answer as 1,2,3,4, etc.)")
                score = 0
                for i in og_list:
                    score += 1
                    print(score, i)
                remove = input()
                if not remove.isdigit():
                    print("Invalid input, try again.")
                else:
                    rem = int(remove)

                    if rem == 0:
                        print("Invalid input, try again.")
                    else:
                        score = 0
                        position = rem - 1
                        for i in og_list:
                            score += 1
                        if rem < 1 or rem > score:
                            print("Invalid input. Try again")
                        else:
                            previous_list = og_list.copy()
                            stuff = og_list.pop(position)
                            print("Index has been removed.")
                            time.sleep(1.3)

        elif player_choice == "c":
            if og_list == []:
                print("There is nothing in your list to display.")
            else:
                for i in og_list:
                    print(i)
                time.sleep(3)

        elif player_choice == "d":
            if previous_list == None:
                print("You have not made any previous changes.")
                time.sleep(1.3)
            else:
                og_list = previous_list.copy()
                previous_list = None
                print("Change has been undone.")
                time.sleep(1.3)

        elif player_choice == "e":
            print("Exiting app...")
            time.sleep(1.3)
            break
        else:
            print("Invalid input, try again.")
            time.sleep(0.3)



list_app()