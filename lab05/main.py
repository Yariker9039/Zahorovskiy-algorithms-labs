"""Лабораторна 5. Сортування об'єктів."""
from dataclasses import dataclass


@dataclass
class Student:
    surname: str
    group: str
    grade: int
    year: int


students = [
    Student('Ткаченко', 'ІПЗ-3/1', 85, 2024),
    Student('Бондар', 'ІПЗ-3/2', 92, 2023),
    Student('Іваненко', 'ІПЗ-3/1', 85, 2024),
    Student('Коваль', 'ІПЗ-3/2', 78, 2024),
    Student('Сидоренко', 'ІПЗ-3/1', 85, 2023),
    Student('Мельник', 'ІПЗ-3/2', 92, 2024),
    Student('Гриценко', 'ІПЗ-3/1', 78, 2023),
    Student('Дяченко', 'ІПЗ-3/2', 85, 2023),
]

# Unicode-порядок не збігається з українською абеткою: І має йти після И.
ALPHABET = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'


def surnameKey(student):
    return [ALPHABET.index(letter) for letter in student.surname.lower()]


def printAll(title, items):
    print(title)
    for s in items:
        print(s.surname, s.group, s.grade, s.year)


def main():
    printAll('За прізвищем:', sorted(students, key=surnameKey))
    printAll('За балом від вищого:', sorted(students, key=lambda s: -s.grade))
    printAll('За групою і балом:', sorted(students, key=lambda s: (s.group, -s.grade)))
    printAll('За балом і прізвищем:', sorted(students, key=lambda s: (-s.grade, surnameKey(s))))


if __name__ == '__main__':
    main()
