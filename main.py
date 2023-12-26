import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def add_record(file_path, new_record):
    data = read_json(file_path)
    data.append(new_record)
    write_json(file_path, data)

def remove_record(file_path, index):
    data = read_json(file_path)
    if 0 <= index < len(data):
        del data[index]
        write_json(file_path, data)
    else:
        print("Invalid index.")

def search_by_field(file_path, field_name, value):
    data = read_json(file_path)
    results = [record for record in data if record.get(field_name) == value]
    return results

def calculate_average_grades(data):
    averages = []
    for student in data:
        total_grades = sum(student['grades'].values())
        average = total_grades / len(student['grades'])
        averages.append(average)
    return averages

def find_students_above_class_average(file_path):
    data = read_json(file_path)
    averages = calculate_average_grades(data)
    class_average = sum(averages) / len(averages)

    above_average_students = [student['surname'] for i, student in enumerate(data) if averages[i] > class_average]
    return above_average_students


initial_data = [
    {"surname": "student1", "grades": {"math": 90, "english": 85, "history": 92, "science": 88, "art": 95}},
    {"surname": "student2", "grades": {"math": 88, "english": 92, "history": 78, "science": 85, "art": 90}},
    {"surname": "student3", "grades": {"math": 23, "english": 56, "history": 67, "science": 45, "art": 43}},
    {"surname": "student4", "grades": {"math": 56, "english": 13, "history": 34, "science": 68, "art": 67}},
    {"surname": "student5", "grades": {"math": 87, "english": 52, "history": 23, "science": 12, "art": 12}},
    {"surname": "student6", "grades": {"math": 83, "english": 34, "history": 13, "science": 23, "art": 24}},
    {"surname": "student7", "grades": {"math": 13, "english": 63, "history": 24, "science": 34, "art": 24}},
    {"surname": "student8", "grades": {"math": 88, "english": 85, "history": 78, "science": 45, "art": 32}},
    {"surname": "student9", "grades": {"math": 53, "english": 36, "history": 67, "science": 56, "art": 12}},
    {"surname": "student10", "grades": {"math": 24, "english": 45, "history": 65, "science": 78, "art": 16}}
]

write_json("students.json", initial_data)


while True:
    print("\n1. Вивести вміст JSON файлу")
    print("2. Додати новий запис")
    print("3. Видалити запис за індексом")
    print("4. Пошук за полем")
    print("5. Знайти учнів з вищою середньою оцінкою")

    choice = input("Виберіть опцію (або 'q' для виходу): ")

    if choice == '1':
        data = read_json("students.json")
        print(json.dumps(data, indent=2))
    elif choice == '2':
        surname = input("Введіть прізвище: ")
        grades = {subject: int(input(f"Введіть оцінку з {subject}: ")) for subject in ["math", "english", "history", "science", "art"]}
        new_record = {"surname": surname, "grades": grades}
        add_record("students.json", new_record)
    elif choice == '3':
        index = int(input("Введіть індекс запису, який потрібно видалити: "))
        remove_record("students.json", index)
    elif choice == '4':
        field_name = input("Введіть назву поля: ")
        value = input("Введіть значення поля: ")
        results = search_by_field("students.json", field_name, value)
        print(json.dumps(results, indent=2))
    elif choice == '5':
        above_average_students = find_students_above_class_average("students.json")
        print("Учні з вищою середньою оцінкою в класі:", above_average_students)
    elif choice.lower() == 'q':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")