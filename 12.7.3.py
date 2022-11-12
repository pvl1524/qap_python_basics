per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = [] # Обявление переменной-списка deposit
money = int(input("Введите размер депозита: "))

# Сохранение процентов разных банков в список percents
percents = list(per_cent.values())
for i in percents: # Перебор значений в списке percents
    deposit.append(round(i/100*money)) # Добавление в список deposit суммы дохода для текущей ставки i
print(deposit) # Вывод в консоль итогового списка deposit

# Определение максимального дохода
# max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))

# Определение банка, предлагающего максимальную доходность по вкладу
index_max_percent = percents.index(max(percents)) # Индекс элемента с макс. ставкой в списке percents
bank_max = list(per_cent.keys())[index_max_percent] # Название банка с максимальной ставкрй
print("Банк, предлагающий максимальный процент - ", bank_max)
