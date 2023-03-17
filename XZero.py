
# Функция приветсвие
def condition():
    print()
    print('Привет Мир!')
    print('Это игра в крестики и нолики.')
    print('Два игрока по очереди вводят две координаты поля.')
    print('После хода на поле клетка заполняется X или 0.')
    print('Тот у кого проставлено три подряд по вертикали, горизонтали или диагонали, тот победил.')
    print('В противном случае, ничья.')
    print('Удачи!')

condition()

field = [[' '] * 3 for i in range(3)]

# Функция поля
def show_field():
    print()
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} | "
        print(row_str)
        print('---------------')
    print()

show_field()

# Фунция запроса хода
def step():
    while True:
        a, b = map(int, input('Координаты свободной клетки от 0 до 2: ').split())
        if 0 <= a <= 2 and 0 <= b <= 2:
           if field[a][b] == " ":
              return a, b
           else:
               print('Занято: ')
        else:
            print('Аут, еще раз: ')

step()

# Фунция запроса хода, второй вариант
# def step():
#     while True:
#         coordinates = input('Координаты свободной клетки от 0 до 2: ').split()
#
#         if len(coordinates) != 2:
#             print('Ай-я-яй')
#             continue
#
#         a, b = coordinates
#
#         if not(a.isdigit()) or not(b.isdigit()):
#             print('Ай-я-яй')
#             continue
#
#         a, b = int(a), int(b)
#
#         if 0 > a or a > 2 or 0 > b or b > 2:
#             print('Аут, еще раз: ')
#             continue
#
#         if field[a][b] != " ":
#             print('Занято: ')
#             continue
#
#         return a, b
#
# step()

# Функция проверки победителя
def win():
    win_position = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                    ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2))]
    for position in win_position:
        c = position[0]
        d = position[1]
        e = position[2]
        if field[c[0]][c[1]] == field[d[0]][d[1]] == field[e[0]][e[1]] != " ":
            print(f'Победил {field[c[0]][c[1]]}')
            return True
    return False

win()

# Игра
# condition()
# field = [[' '] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show_field()

    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    a, b = step()

    if num % 2 == 1:
        field[a][b] = 'X'
    else:
        field[a][b] = '0'

    if win():
        break

    if num == 9:
        print('Ничья')
        break
print('Игра закончена!')