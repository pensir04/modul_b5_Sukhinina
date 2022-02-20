field = [['-'] * 3 for _ in range(3)]


# функция игрового поля
def show_field(f):
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])


# функция ввода координат
def user_input(f):
    while True:
        place = input("Введите координаты ").split()
        if len(place) != 2:
            print("Введите две координаты через пробел ")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Введите два числа ")
            continue
        x, y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print("числа должны быть в диапазоне от 0 до 2")
            continue
        if f[x][y] != "-":
            print("Клетка занята")
            continue
        break
    return x, y


# функция проверки результата
def win(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True
        return False


# функция игры
def game(field):
    count = 0
    while True:
        if count % 2 == 0:
            user = "х"
        else:
            user = "о"
        show_field(field)
        x, y = user_input(field)
        field[x][y] = user
        if count == 8:
            print("ничья")
            show_field(field)
            break
        if win(field, user):
            print(f"Выиграл {user}")
            show_field(field)
            break
        count += 1


# функция начала игры
def start():
    p = input("Поиграем в крестики-нолики? Если желаете играть наберите Y ")
    if p == "Y":
        game(field)
    else:
        print("Тогда до встречи в другой раз!")


start()
