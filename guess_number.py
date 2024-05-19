from random import randint

number = randint(1, 100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число: '))

    if guess > number:
        print('Больше загаданного')

    elif guess < number:
        print('Меньше загаданного')
    
    elif guess == number:
        break

print('Угадал')