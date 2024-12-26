from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)
    cats = []

    if not file_path.exists():
        print(f"Файл'{file_path}' не знайдено.")
        return None

    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file:
            cleared_string=(line.strip().split(','))
            if len(cleared_string) == 3:
                id, name, age = cleared_string
                
                try:
                    age = int(age)
                    cats.append({'id': id, 'name': name, 'age': age})
                    
                except ValueError:
                    continue
   
    if not cats:
        print("Файл не містить даних про котів або дані некоректні.")
    return(cats)

cats_info = get_cats_info('cats.txt')
print(cats_info)