# ДЗ: 1. Решение ёлочки (для тех, кто не решил на уроке) с применением while.
#     2. Переделать ёлочку так, чтобы минимальное значение для высоты было 3, а максимальное 30
#        (через логическое условие while).
#     3. Доработать ёлочку так, чтобы после вывода основной ёлочки, программа дорисовывала ей ножку тольщиной 2 зыезды
#        (**), глубиной 3 звезды.


print('Введите глубину ёлки:')
stars = int(input())
star = 1
while star < stars+1:
    print(star * '*')
    star = star + 1
for star in range(3):
  print('*''*')