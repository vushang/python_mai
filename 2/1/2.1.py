def read_file_with_numbers(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()
        
        for line in data:
            line = line.strip()  
            try:
                num = float(line)
                print(line)
            except ValueError:
                raise TypeError(f"Строка '{line}' не является числовым значением.")

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

read_file_with_numbers("data.txt")