from unicodedata import digit

number = 495184
list_digit = [int(i) for i in str(number)]
print(list_digit)
sum_of_digits = sum(list_digit)
print("Сумма цифр", sum_of_digits)
print("Количество цифр", len(list_digit))
print("Минимальная цифра", min(list_digit))  # TODO минимальная цифра
print("Максимальная цифра", max(list_digit))  # TODO максимальная цифра
print("Среднее арифметическое цифр", round(sum_of_digits/len(list_digit),2))  # TODO среднее арифметическое цифр
