
def get_cats_info(path):
    results = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for record in file:
                id, name, age = record.strip().split(",")
                results.append({
                    "id" : id, 
                    "name" : name,
                     "age" : age
                })
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте чи існує вказаний файл.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    
    return results

print(get_cats_info("test.txt"))