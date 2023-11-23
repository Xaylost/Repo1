import random

def guess_number(n):
    k = 0
    while 2**k < n:
        k += 1
    return k

def main():
    n = int(input("Верхний порог: "))
    max_attempts = guess_number(n)
    print(f"Попыток угадать: {max_attempts}")

    number_to_guess = random.randint(0, n)
    attempts = 0
    guess = None

    while attempts < max_attempts:
        guess = int(input("Угадай число: "))
        if guess == number_to_guess:
            print("Верно")
            break
        elif guess < number_to_guess:
            print("Число больше")
        else:
            print("Число меньше")
        attempts += 1

    if attempts == max_attempts:
        print(f"Неверно. {number_to_guess}")

if __name__ == "__main__":
    main()