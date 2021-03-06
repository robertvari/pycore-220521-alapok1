import random

game_title = "MAGIC NUMBER"
try_count = 3
min_number = 1
max_number = 10

print("-"*50, game_title, "-"*50)
print(f"There is number between {min_number} and {max_number}. Can you guess it?")
print(f"You have {try_count} tries.")


magic_number = random.randint(min_number, max_number)

user_guess = input("Your guess?")

while user_guess != str(magic_number):
    try_count -= 1

    if try_count == 0:
        print("You have no more tries :(")
        break

    print(f"Wrong guess. You have {try_count} tries left.")
    user_guess = input("Your guess?")


if user_guess == str(magic_number):
    print("You win!")
else:
    print(f"You lost. My number was {magic_number}. Maybe next time.")