import random

p = 'да'
while p == 'да' or p == 'Да' or p == 'дА' or p == 'ДА':
    slovar = ['арбуза', 'вода', 'стол', 'кастрюля', 'мышь', 'лето', 'зонт',
              'деталь', 'палка', 'флаг', 'полка', 'муха', 'сапог', 'оружие',
              'день', 'каша']
    i = random.choice(slovar)
    print(len(i) * '*')
    slovo = list(i)
    slovo5 = list(i)
    slovo2 = i
    slovo3 = i
    slovo4 = list(len(i) * '*')
    health = 15
    m = len(i)
    while health:
        x = input()
        if x.lower() in slovo:
            if slovo.count(x) > 1:
                for idx, kl in enumerate(slovo5):
                    if kl == x:
                        del slovo[slovo2.find(x)]
                        slovo4[idx] = x
                        slovo2 = ''.join(slovo)
                        m -= 1
            else:
                del slovo[slovo2.find(x)]
                slovo4[slovo3.find(x)] = x
                slovo2 = ''.join(slovo)
                m -= 1
            print(''.join(slovo4))
  
            if m == 0:
                print('Молодец!!!')
                print('Хочешь еще попробовать?')             
                print('Если да, то напиши "да", если нет, то введи, что угодно')
                p = input()
                break
        elif x == '\get_griddy' or x.lower() == i:
            print(i)
            m = 0
            print('Молодец!!!')
            print('Хочешь еще попробовать?')
            print('Если да, то напиши "да", если нет, то введи, что угодно')
            p = input()
            break
        elif x.isalpha() == False or len(x) > 1:
            print('Нужно вводить буквы и только по одной')
        elif x.lower() not in slovo:
            print(''.join(slovo4))
            health -= 1
            if health == 0:
                print('Не молодец(((')
                print('Хочешь еще попробовать?')
                print('Если да, то напиши "да", если нет, то введи, что угодно')
                p = input()
                break