
#Strannik73


#convertation function
def yu (Lstar, Lsun):
    return   0.5 * (Lstar / Lsun)

#функция main
def main ():
    # ввод через одну строку: "Lstar-Lsun"
    user_input = input('Lstar и Lsun через " - " ')
    times = user_input.split('-')
    

    Lstar = float(times[0]) # вписываем Lstar 
    Lsun = float(times[1]) # вписываем Lsun


    dAU = yu(Lstar, Lsun)
    print('радиус обитаемой зоны вокруг звезды :  ' ,dAU )#отображаем вычислинный радиус вокруг звезды


if __name__ == "__main__":
    main()