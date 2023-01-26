# Игра "Крестики - Нолики"
import random
from colorama import Fore
from colorama import Back
from colorama import init
init(autoreset=True)


print(Fore.GREEN +" ___________________________________________")
print(Fore.GREEN + '>> Добро пожаловать в игру "Крестики - Нолики <<"')
print(Fore.GREEN + "___________________________________________")
# Строим игровое поле
game_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_arena = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def print_game_arena():
    for x in range(rows):
        print('\n +---+---+---+')
        print(' |', end='')
        for y in range(cols):
            print("", game_arena[x][y], end=' |')
    print('\n +---+---+---+')
# Определяем ход игрока
def enter_array(num, turn):
    num -= 1
    if num == 0:
        game_arena[0][0] = turn
    elif num == 1:
        game_arena[0][1] = turn
    elif num == 2:
        game_arena[0][2] = turn
    elif num == 3:
        game_arena[1][0] = turn
    elif num == 4:
        game_arena[1][1] = turn
    elif num == 5:
        game_arena[1][2] = turn
    elif num == 6:
        game_arena[2][0] = turn
    elif num == 7:
        game_arena[2][1] = turn
    elif num == 8:
        game_arena[2][2] = turn
# Функция проверки победителя
X = '\x1b[44mX'
O = '\x1b[41mO'
def check_winner(game_arena):
    if game_arena[0][0] == X and game_arena[0][1] == X and game_arena[0][2] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[0][0] == O and game_arena[0][1] == O and game_arena[0][2] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[1][0] == X and game_arena[1][1] == X and game_arena[1][2] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[1][0] == O and game_arena[1][1] == O and game_arena[1][2] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[2][0] == X and game_arena[2][1] == X and game_arena[2][2] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[2][0] == O and game_arena[2][1] == O and game_arena[2][2] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[0][0] == X and game_arena[1][0] == X and game_arena[2][0] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[0][0] == 'O' and game_arena[1][0] == 'O' and game_arena[2][0] == 'O':
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[0][1] == X and game_arena[1][1] == X and game_arena[2][1] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[0][1] == O and game_arena[1][1] == O and game_arena[2][1] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[0][2] == X and game_arena[1][2] == X and game_arena[2][2] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[0][2] == O and game_arena[1][2] == O and game_arena[2][2] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[0][0] == X and game_arena[1][1] == X and game_arena[2][2] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[0][0] == O and game_arena[1][1] == O and game_arena[2][2] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O
    elif game_arena[0][2] == X and game_arena[1][1] == X and game_arena[2][0] == X:
        print(Fore.CYAN +'>> Человек выйграл! <<')
        return X
    elif game_arena[0][2] == O and game_arena[1][1] == O and game_arena[2][0] == O:
        print(Fore.RED + 'Компьютер выйграл!')
        return O

# Очередность ходов
exit_turn = False
turn = 'X'
turn_conter = 0
while exit_turn == False:
    # Ход игрока
    if turn_conter % 2 == 1:
        print_game_arena()
        num_turn = int(input(Fore.LIGHTGREEN_EX + '\n Введите число от 1 до 9: '))
        if num_turn not in game_numbers:
            print(Fore.RED + 'Клетка занята, попробуйте еще:')
            continue
        if num_turn >= 1 and num_turn <= 9:
            enter_array(num_turn, Back.BLUE + 'X')
            game_numbers.remove(num_turn)
            turn_conter += 1
        else:
            print(Fore.RED + 'Неверно значение, попробуйте еще:')
            continue
    # Ход компьютера
    else:
        while True:
            comp_turn = random.choice(game_numbers)
            print(Fore.RED + '\n Ход компьютера', comp_turn)
            if(comp_turn in game_numbers):
                enter_array(comp_turn, Back.RED + 'O')
                game_numbers.remove(comp_turn)
                turn_conter += 1
                break
    if turn_conter == 9:
        print(" Ничья!")
        break
    if check_winner(game_arena):
        break
