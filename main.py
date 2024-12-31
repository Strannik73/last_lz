# Импортируем наши функции
import pyramid as pyd
import life_zone as lzon




def main():
    user_cloise = input('введите одну из возможных команд: pyd, lzon:  ')
    if user_cloise.lower() == 'pyd' :               # если (pyd) --> Вызываем функцию расчета обЪема усеченной пирамиды
        pyd.main()
    elif user_cloise.lower() == 'lzon' :               # если (lzon) --> Вызываем функцию расчета радиуса обитаемой зоны вокруг звезды по формуле
        lzon.main()


if __name__ == "__main__": # если прямой запуск - выполняем main
    main()