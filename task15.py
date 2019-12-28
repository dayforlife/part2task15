age = int(input("Введите ваш возраст: "))
i = list(range(age))
if age % 2 == 0:
    print(i[2::2])
else:
    print(i[1::2])