import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Читання CSV файлу
def read_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        print('Файл CSV не знайдено.')
        return None


# Підрахунок кількості чоловіків і жінок
def count_by_gender(employees):
    male_count = sum(1 for e in employees if e['Стать'] == 'Чоловіча')
    female_count = sum(1 for e in employees if e['Стать'] == 'Жіноча')

    print(f'Чоловіків: {male_count}, Жінок: {female_count}')
    return male_count, female_count


# Побудова діаграми гендерного розподілу
def plot_gender_distribution(male_count, female_count):
    labels = ['Чоловіки', 'Жінки']
    sizes = [male_count, female_count]
    colors = ['blue', 'pink']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Гендерний розподіл')
    plt.show()


# Підрахунок кількості співробітників у вікових категоріях
def count_by_age_group(employees):
    current_year = datetime.now().year
    age_groups = {
        'younger_18': 0,
        '18-45': 0,
        '45-70': 0,
        'older_70': 0
    }

    for employee in employees:
        dob_year = datetime.strptime(employee['Дата народження'], '%Y-%m-%d').year
        age = current_year - dob_year

        if age < 18:
            age_groups['younger_18'] += 1
        elif 18 <= age < 45:
            age_groups['18-45'] += 1
        elif 45 <= age < 70:
            age_groups['45-70'] += 1
        else:
            age_groups['older_70'] += 1

    print(f'Співробітники віком до 18: {age_groups["younger_18"]}')
    print(f'Співробітники віком 18-45: {age_groups["18-45"]}')
    print(f'Співробітники віком 45-70: {age_groups["45-70"]}')
    print(f'Співробітники віком понад 70: {age_groups["older_70"]}')
    return age_groups


# Побудова діаграми за віковими категоріями
def plot_age_group_distribution(age_groups):
    labels = ['До 18', '18-45', '45-70', '70+']
    sizes = [age_groups['younger_18'], age_groups['18-45'], age_groups['45-70'], age_groups['older_70']]
    colors = ['yellowgreen', 'gold', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Розподіл за віковими категоріями')
    plt.show()


# Підрахунок кількості чоловіків та жінок у кожній віковій категорії
def count_gender_in_age_groups(employees):
    current_year = datetime.now().year
    age_gender_groups = {
        'younger_18': {'male': 0, 'female': 0},
        '18-45': {'male': 0, 'female': 0},
        '45-70': {'male': 0, 'female': 0},
        'older_70': {'male': 0, 'female': 0}
    }

    for employee in employees:
        dob_year = datetime.strptime(employee['Дата народження'], '%Y-%m-%d').year
        age = current_year - dob_year
        gender = 'male' if employee['Стать'] == 'Чоловіча' else 'female'

        if age < 18:
            age_gender_groups['younger_18'][gender] += 1
        elif 18 <= age < 45:
            age_gender_groups['18-45'][gender] += 1
        elif 45 <= age < 70:
            age_gender_groups['45-70'][gender] += 1
        else:
            age_gender_groups['older_70'][gender] += 1

    print("Гендерний розподіл за віковими категоріями:")
    for group, genders in age_gender_groups.items():
        print(f'{group}: Чоловіків: {genders["male"]}, Жінок: {genders["female"]}')

    return age_gender_groups


# Побудова діаграм гендерного розподілу у вікових категоріях
def plot_gender_in_age_groups(age_gender_groups):
    for group, genders in age_gender_groups.items():
        labels = ['Чоловіки', 'Жінки']
        sizes = [genders['male'], genders['female']]
        colors = ['blue', 'pink']

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(f'Гендерний розподіл у категорії {group}')
        plt.show()


if __name__ == '__main__':
    employees = read_csv('employees.csv')
    if employees:
        # Кількість чоловіків та жінок
        male_count, female_count = count_by_gender(employees)
        plot_gender_distribution(male_count, female_count)

        # Кількість співробітників у вікових категоріях
        age_groups = count_by_age_group(employees)
        plot_age_group_distribution(age_groups)

        # Гендерний розподіл у вікових категоріях
        age_gender_groups = count_gender_in_age_groups(employees)
        plot_gender_in_age_groups(age_gender_groups)

