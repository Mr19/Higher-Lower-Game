from art import logo, vs
from game_data import data
from os import system, name
import random


def clear():
    # cls for windows, posix for mac or linux
    system('cls') if name == 'nt' else system('clear')


def user_guess_check(user_choice, a_person_followers, b_person_followers):
    if a_person_followers > b_person_followers:
        return user_choice == "a"
    else:
        return user_choice == "b"


def main():
    b_person = random.choice(data)
    score = 0
    while score >= 0:
        clear()
        print(logo)

        if score > 0:
            print(f"You're right! Current score: {score}.")
        a_person = b_person
        b_person = random.choice(data)

        while a_person == b_person:
            b_person = random.choice(data)
        print(f'Compare A: {a_person["name"]}, a {a_person["description"]}, from {a_person["country"]}')
        print(vs)
        print(f'Against B: {b_person["name"]}, a {b_person["description"]}, from {b_person["country"]}')
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_guess_check(user_choice, a_person["follower_count"], b_person["follower_count"]):
            score += 1
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            score = -1


if __name__ == '__main__':
    main()

