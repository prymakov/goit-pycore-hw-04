
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for record in file:
                name, salary = record.split(",")
                total += int(salary)
                count += 1
        
        avarage = total / count
        return (total, avarage)
    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте чи існує вказаний файл.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)
