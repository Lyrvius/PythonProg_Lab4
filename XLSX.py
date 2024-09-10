import csv
import openpyxl
from datetime import datetime

def read_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        print('Файл CSV не знайдено.')
        return None

def save_to_excel(data, filename):
    try:
        wb = openpyxl.Workbook()
        ws_all = wb.active
        ws_all.title = 'all'
        ws_all.append(['№', 'Прізвище Ім\'я По батькові', 'Дата народження', 'Вік'])

        current_year = datetime.now().year
        for i, employee in enumerate(data, start=1):
            dob_year = datetime.strptime(employee['Дата народження'], '%Y-%m-%d').year
            age = current_year - dob_year
            ws_all.append([i, employee['Прізвище Ім\'я По батькові'], employee['Дата народження'], age])

        # Створення інших аркушів і фільтрація за віком
        age_ranges = {
            'younger_18': (0, 18),
            '18-45': (18, 45),
            '45-70': (45, 70),
            'older_70': (70, 100)
        }

        for sheet_name, (min_age, max_age) in age_ranges.items():
            ws = wb.create_sheet(title=sheet_name)
            ws.append(['№', 'Прізвище Ім’я По батькові', 'Дата народження', 'Вік'])
            for i, employee in enumerate(data, start=1):
                dob_year = datetime.strptime(employee['Дата народження'], '%Y-%m-%d').year
                age = current_year - dob_year
                if min_age <= age < max_age:
                    ws.append([i, employee['Прізвище Ім\'я По батькові'], employee['Дата народження'], age])

        wb.save(filename)
        print('Ok')

    except Exception as e:
        print(f'Помилка при створенні файлу XLSX: {e}')

if __name__ == '__main__':
    employees = read_csv('employees.csv')
    if employees:
        save_to_excel(employees, 'employees.xlsx')
