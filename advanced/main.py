og_list = []
complete_list = []
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
RESET = "\033[0m"
import time



def list_app():
    global og_list
    global complete_list
    global change
    global stuff
    global position
    stuff = None
    previous_list = None
    previous_complete = None
    while True:
        player_choice = input(f"{UNDERLINE}{BOLD} TO-DO LIST APP {RESET}"
                              f"\nWould you like to:"
                              f"\n{BOLD}A:{RESET} Add something to your list"
                              f"\n{BOLD}B:{RESET} Remove something from your list"
                              f"\n{BOLD}C:{RESET} Display your list"
                              f"\n{BOLD}D:{RESET} Undo a previous change"
                              f"\n{BOLD}E:{RESET} Replace item in list"
                              f"\n{BOLD}F:{RESET} Mark an item in the list as complete"
                              f"\n{BOLD}G:{RESET} Exit the app"
                              f"\n").strip().lower()
        time.sleep(1.3)
        if player_choice == "a":
            add = input("Please type what you wish to add:"
                        "\n").strip().capitalize()
            print(f"{add} has been added to your to do list.")
            previous_list = og_list.copy()
            previous_complete = complete_list.copy()
            og_list.append(add)
            time.sleep(1.3)

        elif player_choice == "b":
            previous_list = og_list.copy()
            previous_complete = complete_list.copy()
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
                            previous_complete = complete_list.copy()
                            stuff = og_list.pop(position)
                            print("Index has been removed.")
                            time.sleep(1.3)

        elif player_choice == "c":
            inp = input("Which list would you like to see:"
                        f"\n{BOLD}A:{RESET} To-do list"
                        f"\n{BOLD}B:{RESET} Completed list").strip().lower()
            if inp == "a":
                if og_list == []:
                    print("There is nothing in the list to display.")
                else:
                    for i in og_list:
                        print(i)
                    time.sleep(3)
            elif inp == "b":
                if complete_list == []:
                    print("There is nothing in the list to display")
                else:
                    for i in complete_list:
                        print(i)
                    time.sleep(3)
            else:
                print("Invalid Input, try again!")

        elif player_choice == "d":
            if previous_list == None:
                print("You have not made any previous changes.")
                time.sleep(1.3)
            else:
                og_list = previous_list.copy()
                complete_list = previous_complete.copy()
                previous_list = None
                previous_complete = None
                print("The change has been undone.")
                time.sleep(1.3)

        elif player_choice == "e":
            if og_list == []:
                print("There is nothing in your todo list to replace.")
                time.sleep(1.3)
            else:
                print("At which position is the item you want to replace? (Answer as 1,2,3,4, etc.)")
                score = 0
                for i in og_list:
                    score += 1
                    print(score, i)
                replace = input()
                if not replace.isdigit():
                    print("Invalid input, try again.")
                else:
                    rep = int(replace)

                    if rep == 0:
                        print("Invalid input, try again.")
                    else:
                        score = 0
                        position = rep - 1
                        for i in og_list:
                            score += 1
                        if rep < 1 or rep > score:
                            print("Invalid input. Try again")
                        else:
                            previous_list = og_list.copy()
                            previous_complete = complete_list.copy()
                            stuff = input("What would you like to replace text with?")
                            og_list[position] = stuff
                            print("Item has been replaced.")

        elif player_choice == "f":
            if og_list == []:
                print("There is nothing in your todo list to mark as complete.")
                time.sleep(1.3)
            else:
                print("At which position is the item you want to mark as complete? (Answer as 1,2,3,4, etc.)")
                score = 0
                for i in og_list:
                    score += 1
                    print(score, i)
                check_off = input()
                if not check_off.isdigit():
                    print("Invalid input, try again.")
                else:
                    chff = int(check_off)
                    if chff == 0:
                        print("Invalid input, try again.")
                    else:
                        score = 0
                        position = chff - 1
                        for i in og_list:
                            score += 1
                        if chff < 1 or chff > score:
                            print("Invalid input. Try again")
                        else:
                            previous_list = og_list.copy()
                            previous_complete = complete_list.copy()
                            add = og_list.pop(position)
                            complete_list.append(add)
                            print("Item has been marked as completed.")
                            time.sleep(1.3)

        elif player_choice == "g":
            print("Exiting app...")
            time.sleep(1.3)
            break

        else:
            print("Invalid input, try again.")
            time.sleep(1.3)

list_app()