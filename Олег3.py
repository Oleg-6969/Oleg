students = {}

while True:
    name = input("Введіть ім'я студента (або 'stop' для завершення): ")
    if name.lower() == 'stop':
        break
    try:
        grade = int(input(f"Введіть оцінку студента {name}: "))
        if grade < 1 or grade > 12:
            print("Оцінка має бути від 1 до 12. Спробуйте ще раз.")
            continue
    except ValueError:
        print("Будь ласка, введіть числову оцінку.")
        continue
    students[name] = grade

print("\nСписок студентів та їх оцінки:")
for student, grade in students.items():
    print(f"{student}: {grade}")

if students:
    average = sum(students.values()) / len(students)
    print(f"\nСередній бал по групі: {average:.2f}")

excellent = [name for name, grade in students.items() if 10 <= grade <= 12]
good = [name for name, grade in students.items() if 7 <= grade <= 9]
satisfactory = [name for name, grade in students.items() if 4 <= grade <= 6]
fail = [name for name, grade in students.items() if 1 <= grade <= 3]

print(f"\nВідмінники (10-12): {len(excellent)} - {', '.join(excellent) if excellent else 'немає'}")
print(f"Хорошисти (7-9): {len(good)} - {', '.join(good) if good else 'немає'}")
print(f"Відстаючі (4-6): {len(satisfactory)} - {', '.join(satisfactory) if satisfactory else 'немає'}")
print(f"Не здали (1-3): {len(fail)} - {', '.join(fail) if fail else 'немає'}")
