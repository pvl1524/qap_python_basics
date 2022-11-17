total_price = 0
num_visitors = int(input("Введите число посетителей: "))
#print("visitors - ", num_visitors)

#Создаем список Ages с возрастами поситетелей
Ages = [int(input(f"Возраст поситетеля {i}: ")) for i in range(1, num_visitors+1)]
#print("Ages - ", Ages)

for age in Ages:
    if age < 18:
        print(f"Оплата не требуется, возраст посетителя меньше 18 лет")
    elif 18 <= age <= 25:
        total_price += 990
    elif age > 25:
        total_price += 1390

#Если больше 3 посетителей, применить скидку 10% к общей стоимости
#По условию не оговаривается НЕучет бесплатных билетов при расчете скидки
if num_visitors > 3:
    total_price *= 0.9

print(f"Cумма к оплате: {total_price}")



