ticket = int(input('Выберите количество билетов: '))
total_price = 0
under_18_count = 0
for i in range(ticket):
    age = int(input(f'Возраст посетителя №{i+1}: '))
    if age < 18:
        price = 0
        under_18_count += 1
    elif age >= 18 and age < 25:
        price = 990
    else:
        price = 1390
    total_price += price
if ticket > 3:
    total_price *= 0.9
print(f'Сумма к оплата {total_price:.2f} руб.')
print(f'количество посетителей моложе 18 лет: {under_18_count}')