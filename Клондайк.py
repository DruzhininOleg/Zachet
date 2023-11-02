import os


def print_field(m):
    print(' ', ' '.join([str(i) for i in range(len(m))]))
    for i in range(len(m)):
        print(f'{i}|' + '|'.join(m[i]) + '|')


def is_enter_ok(s):
    if not all(i.isdigit() for i in s.split()):
        return False
    if len(s.split()) != 2:
        return False
    if not (0 <= int(s.split()[0]) <= 9) or not (0 <= int(s.split()[1]) <= 9):
        return False
    return True


def gameover(m, ny, nx):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dy, dx in moves:
        dy1 = dy + ny
        dx1 = dx + nx
        if 0 <= dy1 <= 9 and 0 <= dx1 <= 9:
            if m[dy1][dx1] == 'X':
                for dy2, dx2 in moves:
                    if 0 <= (dy1 + dy2) <= 9 and 0 <= (dx1 + dx2) <= 9 and (dy1 + dy2) != ny and (dx1 + dx2) != nx:
                        if m[dy1 + dy2][dx1 + dx2] == 'X':
                            return True
    return False


field = [['.'] * 10 for _ in range(10)]
print_field(field)
h = 0
while True:
    print(
        f'Ход игрока {h % 2 + 1}. '
        f'Введите через пробел координаты клетки, в которую желаете поставить фишку.')
    print('Сначала цифру по вертикали, затем по горизонтали (от 0 до 9)')
    coords = input()
    if not is_enter_ok(coords):
        print('Неверный ввод. Попробуйте еще раз')
        continue
    y, x = list(map(int, coords.split()))
    if field[y][x] != '.':
        print('Клетка уже занята. Введите другие координаты\n')
        continue
    field[y][x] = "X"
    os.system('cls||clear\n')
    print_field(field)
    if gameover(field, y, x):
        print(f'Игра окончена!')
        print(f'Победил игрок {(h - 1) % 2 + 1}')
        break
    h += 1

input('Нажмите Enter для выхода\n')
