money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Количество месяцев без долгов

while True:
    bank = money_capital + salary
    if bank >= spend:
        months += 1
        money_capital = bank - spend
        spend *= (1 + increase)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
