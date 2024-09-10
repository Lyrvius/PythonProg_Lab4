import csv
import random
from faker import Faker

def generate_employee_data(num_records=2000):
    fake = Faker('uk_UA')
    employees = []

    male_count = int(num_records * 0.6)  # 60% чоловіків
    female_count = num_records - male_count  # 40% жінок

    for _ in range(male_count):
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        middle_name = fake.middle_name_male()
        dob = fake.date_of_birth(minimum_age=16, maximum_age=85)
        position = random.choice(['Програміст', 'Менеджер', 'Аналітик', 'Директор'])
        city = fake.city()
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()

        employees.append({
            'Прізвище Ім\'я По батькові': f'{last_name} {first_name} {middle_name}',
            'Стать': 'Чоловіча',
            'Дата народження': dob,
            'Посада': position,
            'Місто проживання': city,
            'Адреса проживання': address,
            'Телефон': phone,
            'Email': email
        })

    for _ in range(female_count):
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        middle_name = fake.middle_name_female()
        dob = fake.date_of_birth(minimum_age=16, maximum_age=85)
        position = random.choice(['Програміст', 'Менеджер', 'Аналітик', 'Директор'])
        city = fake.city()
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()

        employees.append({
            'Прізвище Ім\'я По батькові': f'{last_name} {first_name} {middle_name}',
            'Стать': 'Жіноча',
            'Дата народження': dob,
            'Посада': position,
            'Місто проживання': city,
            'Адреса проживання': address,
            'Телефон': phone,
            'Email': email
        })

    random.shuffle(employees)  # Перемішуємо список
    return employees

def save_to_csv(filename, employees):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)

if __name__ == '__main__':
    employees = generate_employee_data()
    save_to_csv('employees.csv', employees)
