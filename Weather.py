# temperature = int(input('Enter temperature:'))
# if temperature >= 20 and temperature <= 30:
#     isRain = input('Is rain? Write "Yes" or "No":  ')
#     if isRain == 'Yes':
#         print("Put on a T-shirt and raincoat")
#     else:
#         print('Put on a T-shirt and shorts')
# elif temperature >= 0 and temperature < 20:
#     isRain = input('Is rain? Write "Yes" or "No":  ')
#     if isRain == 'Yes':
#         isRain = input('Its heavy or medium? :')
#         if isRain == 'Heavy' or 'heavy':
#             print('Put on coats, rubber boots and gloves')
#         if isRain == 'Medium' or 'medium':
#             print('Put on a coat and raincoat')
#     else:
#         print('Put on only coat')
# elif temperature < 0:
#     print('Put on down jacket')
# elif temperature > 30:
#     print('Very hot')

# S = 0  # это наша переменная-счетчик, в которой мы будем считать сумму чисел
# n = 1  # текущее натуральное число, с которого начинаем складывать натуральные числа
#
# # заводим цикл while, который будет работать пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S = S + n  # увеличиваем сумму, равносильно S = S + n
#     n = n + 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n-1)
#
# text = '''Here you can find activities to practise your reading skills. Reading will help you to improve your understanding of the language and build your vocabulary.'''
# text = text.lower()
# text = text.replace('\n', '')
# text = text.replace(' ', '')
# count = {}
# for letter in text:
#     if letter in count:
#         count[letter] += 1
#     else:
#         count[letter] = 1
# for char, cnt in count.items():
#      print(f"symbol {char} incres {cnt} times")
# print('-----')
# print(sum(count[letter]))
heads = 35  # количество голов
legs = 94  # количество ног

# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
    # Программа "Угадай число, цикл вайл"
# import random
# random_mumber = random.randint(1, 20)
# user_number = -1
# count = 0
# while user_number != random_mumber :
#     count += 1
#     user_number = int(input("Угадай число от 1 до 20:"))
#     if user_number > random_mumber:
#         print("Число должно быть меньше")
#     elif user_number < random_mumber:
#         print("Число должно быть больше")
#     else:
#         print('Ты угадал! Это число: ', str(random_mumber))
#         print('Количество попыток: ', count)
#         if count < 5:
#             print('Классный результат! Шоу "Экстрасенсы" ждет тебя!')
#         elif count >= 5:
#             print('Угадывать - это не твое...')
#         break
# Функция которая считает количество делителей у числа
# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# print(get_multipliers(5))

# def pow_func(base, n=2):
#    resalt = ** n
#    return resalt
#
# c = pow_func(2)
#     print(c)
# def make_adder(x):
#     def adder(n):
#         return x + n
#     return adder
# add_10 = make_adder(10)
# print(add_10(5))
def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break