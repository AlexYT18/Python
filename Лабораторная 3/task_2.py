def find_common_participants(group1, group2, delimiter=','):
    participants_first_group = set(group1.split(delimiter))
    participants_second_group = set(group2.split(delimiter))
    common_participants = participants_first_group.intersection(participants_second_group)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common_participants)
