import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

monsters=["wicked fairy", "troll", "witch", "dragon", "pirate"]

def monsters():
    monster=random.choice(monsters)
    return monster

def intro(monsters):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monstoers} is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def choices(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    house_cave = input("Please enter 1 or 2.")
    while True:
     if house_cave == '1':
        house(items)
     elif house_cave == '2':
        cave(items)
     else:
        house_cave = input("Please enter 1 or 2.")

def fight(items, monsters):
    if "entered_cave" in items:
        print_pause(f"As the {monsters} moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_pause(f"But the {monsters} takes one look at your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {monsters}. You are victorious!")
        play_again(items)
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {monsters}.")
        print_pause("You have been defeated!")
        play_again(items)

def house(items, monsters):
    print_pause(f"You are about to knock when the door opens and out steps a {monsters}")
    print_pause(f"Eep! This is the {monsters}'s house!")
    print_pause(f"The {monsters} attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")
    fight_run = input("Please enter 1 or 2.")
    if fight_run == '1':
        fight(items)
    elif fight_run == '2':
        field(items)
    else:
        fight_run = input("Please enter 1 or 2.")


def cave(items):
    if "entered_cave" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        print_pause("you walk back out to the field.")
        items.append("entered_cave")
    choices(items)

def field(items):
    print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
    choices(items)

def play_again(items):
    play_again = input("Would you like to play again? (y/n)")
    if play_again == 'y':
        intro(items)
    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time.")

def play_game():
    items = []
    intro(monsters)
    choices(items, monsters)

play_game()
