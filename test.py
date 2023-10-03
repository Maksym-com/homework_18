# Створіть DataFrame з ім'ям "students", який містить такі стовпці:
# "Name" (ім'я студента)
# "Age" (вік студента)
# "Gender" (стать студента)
# "Score" (оцінка студента за певний предмет); +
# Додайте в DataFrame "students" декілька рядків з інформацією про різних студентів. +
# Виведіть перші 5 рядків з DataFrame "students". +
# Обчисліть середній вік студентів. +
# Виведіть студентів, які отримали оцінку вище 80. +
# Змініть оцінку студента з іменем "Anna" на 95. +
# Створіть Series з ім'ям "ages" на основі стовпця "Age" з DataFrame "students". +
# Знайдіть максимальний вік серед студентів. +
# Видаліть рядок з іменем "John" з DataFrame "students". +
# Збережіть отриманий DataFrame у форматі CSV файлу під назвою "students.csv".

import pandas as pd
import random

students = {
        'Name': ['John', 'Stacy', 'Maks', 'Anna'],
        'Age': [17, 18, 17, 19],
        'Gender': ['male', 'female', 'male', 'female'],
        'english_score': [93, 82, 70, 65],
    }

def work_with_dict():
    df = pd.DataFrame(students)

    print(f'{df} \n')

def add_student():
    columns = ['Name', 'Age', 'Gender', 'english_score']
    df = pd.DataFrame(students, columns=columns)
    new_row = {'Name': 'Alice', 'Age': 17, 'Gender': 'female', 'english_score': 76}
    df.loc[len(df)] = new_row
    print(df)


def test_filtration():
    df = pd.DataFrame(students)
    score_filter = df[(df['english_score'] > 80)]
    print("\n Фільтр по оцінкам")
    print(f'\n {score_filter}')

def test_smth():
    df = pd.DataFrame(students)

    print(f"\n {df['Age'].loc[3]}")

    avg_age = df['Age'].mean()
    print(f"\n Avg age {avg_age}")

    df.loc[df['Name'] == 'Anna', 'english_score'] = 95
    print(f" \n{df[df['Name'] == 'Anna']}")

    max_age = df['Age'].max()
    print(f'\n {max_age}')

    df.drop(df[df['Name'] == 'John'].index, inplace=True)
    print(f'\n {df}')

def series(): 
    df = pd.DataFrame(students)

    data_0 = df['Age']
    ages = pd.Series(data_0)
    print(f'\n {ages}')

def save():
    df = pd.DataFrame(students)
    df.to_csv('students.csv', index=False)

work_with_dict()
add_student()
test_filtration()
test_smth()
series()
save()