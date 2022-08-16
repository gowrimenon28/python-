actual_number=45
attempts=0

while True:
    attempts += 1
    guess=int(input("guess the number:\n"))
    if guess<actual_number:
        print("your guess was too low")

    elif guess>actual_number:
        print("your guess was too high")
    else:
        print(f"you guessed the number in {attempts} attempts")
        break
print("thanks for playing!")
