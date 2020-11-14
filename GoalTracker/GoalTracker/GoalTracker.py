# DESCRIPTION
# Goal setting and tracking program with progress bars,
# I will mostly use this to track school
#
# Date Started: Nov 12, 2020
# Mustafa Al-Youzbaki
# v0.4
import sys

running = True
goal_file = open("goal_file.txt","r+")
goals = []

class Goal:
    def __init__(self, topic, due_date, progress):
        self.topic = topic       # str
        self.due_date = due_date # str
        self.progress = progress # int
        
    def increase_prog(self, amount):
        if (self.progress + amount) <= 10:
            self.progress = self.progress + amount

    def decrease_prog(self, amount):
        if (self.progress - amount) >= 0:
            self.progress = self.progress - amount

    def prog_bar(self, prog):
        progress_bar = ""
        if prog < 10 and prog >= 0:
            for block in range(prog):
                progress_bar = progress_bar + "I"
            for block in range(10-prog):
                progress_bar = progress_bar + "*"
        elif prog == 10:
            progress_bar = "COMPLETED"
        return progress_bar

    def status(self):
        print("{:<25} | DUE ON {:<25} |".format(self.topic, self.due_date) + self.prog_bar(self.progress))

def splash_screen():
    print("GOAL TRACKER")
    print("Use this to set goals, track their progress, and")
    print("check it off your list. Basically a digital to-do list")

def menu():
    global goals
    print("\nMENU")
    print("1. Add goal")
    print("2. Remove goal")
    print("3. Increase goal progress")
    print("4. Decrease goal progress")
    print("5. Exit")
    while True:
        choice = int(input("Pick a #(1-5): "))
        print("")
        if choice < 1 or choice > 5:
            print("Please enter a number between 1 and 5.")
        elif choice == 1: # ADD GOAL
            topic = input("Enter the topic: ")
            date = input("Enter the due date: ")
            prog = int(input("Enter your progress in that goal (0-10): "))
            goals.append(Goal(topic,date,prog))
            print("Your goal was added!\n")
            break

        elif choice == 2: # DELETE GOAL
            index = int(input("Which goal would you like to remove? Enter a #: ")) - 1
            try:
                del goals[index]
                print("Your goal was removed!\n")
                break
            except:
                print("That is not a valid index.")
                break

        elif choice == 3: # INCREASE PROGRESS
            index = int(input("Which goal would you like to increase? Enter a #: ")) - 1
            amount = int(input("How many steps would you like to increase by? Enter a #: "))
            try:
                if (goals[index].progress + amount) > 10:
                    goals[index].increase_prog(10-goals[index].progress)
                    print("That goal was capped off and completed!")
                else:
                    goals[index].increase_prog(amount)
                    print("That goal was increased by " + str(amount) + " steps!")
                break
            except:
                print("Enter a valid index please.")
                break

        elif choice == 4: # DECREASE PROGRESS
            index = int(input("Which goal would you like to decrease? Enter a #: ")) - 1
            amount = int(input("How many steps would you like to decrease by? Enter a #: "))
            try:
                if (goals[index].progress - amount) < 0:
                    goals[index].decrease_prog(goals[index].progress)
                    print("That goal was reset to zero!")
                else:
                    goals[index].decrease_prog(amount)
                    print("That goal was decreased by " + str(amount) + " steps!")
                break
            except:
                print("Enter a valid index please.")
                break

        else: # EXIT
            global running
            input("Work hard! Goodbye.")
            running = False
            break

def print_goals():
    print("\n-GOALS-")
    print("--------------------------------------------------------------------------")
    if len(goals) == 0:
        print("No goals currently")
    else:
        i = 1
        for goal in goals:
            print(str(i), end=" ")
            goal.status()
            i = i + 1
    print("--------------------------------------------------------------------------\n")

def save_goals():
    global goal_file, goals
    goal_file.close()

    goal_file = open("goal_file.txt","w+")
    for goal in goals:
        goal_file.write(goal.topic + "," + goal.due_date + "," + str(goal.progress) + "\n")
    goal_file.close()

def load_goals():
    global goal_file, goals

    for line in goal_file:
        curr_goal = line.split(",")
        goals.append(Goal(curr_goal[0],curr_goal[1],int(curr_goal[2])))

def main():
    splash_screen()
    load_goals()
    while running:
        print_goals()
        menu()
    save_goals()

main()