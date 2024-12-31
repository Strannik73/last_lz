
#Strannik73


#convertation function
def pym (h, sv, sn):
    return  1/3 * h *( sv + 0.5 * (sv * sn) + sn)

#функция main
def main ():
    # ввод через одну строку: "высота-верхнего основания-нижнего основания"
    user_input = input('введите значения высота, верхнего основания и нижнего основания через " - " ')
    times = user_input.split('-')
    
    
    h = int(times[0]) # высота пирамиды
    sv = int(times[1]) # площадь верхнего основания пирамиды
    sn = int(times[2]) # площадь  нижнего основания пирамиды

    V = pym(h, sv, sn)
    print('обЪем усеченной пирамиды :  ' ,V )


if __name__ == "__main__":
    main()