import random


def guessing_game():
    answer = random.randint(10, 30)
    chances = 3
    count = 0

    while chances >= count:
        count += 1

        if chances == count:
            print('This is last chance!')
        elif chances < count:
            print(f'💥 Too bad! The answer was {answer}.')
            break

        guess = int(input('What is your guess?: '))

        if guess == answer:
            print(f'🎉 Right! The answer is {answer}')
            break

        if guess < answer:
            print(f'{guess} is too low...')
            continue
        else:
            print(f'{guess} is too high...')
            continue


if __name__ == '__main__':
    guessing_game()
