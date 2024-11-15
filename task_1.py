import json

def task() -> float:
    with open("input.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    total_sum = 0.0
    for entry in data:
        score = entry.get("score", 0)
        weight = entry.get("weight", 0)
        total_sum += score * weight
    return round(total_sum, 3)

print(task())