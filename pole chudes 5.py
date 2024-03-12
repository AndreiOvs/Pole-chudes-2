import random

p = 'да'
while p == 'да':
    slovar = ['арбуз', 'вода', 'стол', 'кастрюля', 'мышь', 'лето', 'зонт', 'деталь', 'палка', 'флаг', 'щприц', 'муха', 'сапог', 'оружие', 'день', 'каша']
    i = random.choice(slovar)
    print(len(i) * '*')
    slovo = list(i)
    slovo2 = i
    slovo3 = i
    slovo4 = list(len(i) * '*')
    x = input()
    health = 15
    m = len(i)
    while health:
        if x in slovo:
            del slovo[slovo2.find(x)]
            slovo4[slovo3.find(x)] = x
            print(''.join(slovo4))
            slovo2 = ''.join(slovo)
            m -= 1
            if m == 0:
                print('Молодец!!!')
                print('Хочешь еще попробовать?')
                p = input()
                break
            x = input()
        else:
            print(''.join(slovo4))
            health -= 1
            if health == 0:
                print('Не молодец(((')
                print('Хочешь еще попробовать?')
                p = input()
                break
            x = input()