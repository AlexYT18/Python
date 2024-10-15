numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
unum = [i for i in numbers if i is not None]
numbers[numbers.index(None)] = round(sum(unum) / (len(unum) + 1), 5)
print("Измененный список:", numbers)