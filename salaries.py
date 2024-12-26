from pathlib import Path
def total_salary(path):
    file_path = Path(path)
    salaries = []

    if not file_path.exists():
        print(f"Файл'{file_path}' не знайдено.")
        return None

    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file:
            cleared_string=(line.strip().split(','))
            if len(cleared_string) == 2:  #
                try:
                    salary = int(cleared_string[1])
                    salaries.append(salary)
                except ValueError:
                    continue
    if salaries and len(salaries) > 0:
        total = sum(salaries)
        averrage = total / len(salaries)
        return (total, averrage)
    else:
        print('Немає валідних зарплат у файлі')
        return(0,0)




total, average = total_salary('test.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")