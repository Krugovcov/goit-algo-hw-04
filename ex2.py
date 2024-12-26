def get_cats_info(path):
    file_path = Path(path)
    cats = [{}]

    if not file_path.exists():
        print(f"Файл'{file_path}' не знайдено.")
        return None

    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file:
            cleared_string=(line.strip().split(','))
    print(cleared_string)
get_cats_info('cats.txt')