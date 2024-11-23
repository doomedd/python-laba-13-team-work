import csv
import json

# (Глумний Тимур КН-33.2)
# Функція для створення CSV-файлу з даними про книги
def create_csv_file():
    data = [
        # Назва книги, автор, рік публікації
        {"title": "1984", "author": "George Orwell", "year": 1949},      
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
    ]

    try:
        with open('books.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
            writer.writeheader()
            writer.writerows(data)
        print("CSV файл 'books.csv' успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні CSV-файлу: {e}")

# (Руденко Данііл КН-33.2)
# Функція для конвертації CSV у JSON
def csv_to_json():
    try:
        data = {}

        # Читання CSV файлу
        with open('books.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['year'] = int(row['year'])  # Рік публікації (int)
                # Використовуємо назву книги як ключ для словника
                data[row['title']] = {"author": row['author'], "year": row['year']}

        # Запис у JSON файл
        with open('books.json', mode='w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("JSON файл 'books.json' успішно створено.")

    except FileNotFoundError:
        print("Помилка: Файл 'books.csv' не знайдено.")
    except json.JSONDecodeError:
        print("Помилка: Не вдалося декодувати JSON.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

# (Чорномаз Вікторія КН-33.1)
# Функція для переписування даних з JSON у CSV, з додаванням нових рядків
def json_to_csv_with_new_rows():
    try:
        # Читання даних з JSON файлу
        with open('books.json', mode='r') as file:
            data = json.load(file)

        # Додаємо нові книги
        new_books = {
            "Brave New World": {"author": "Aldous Huxley", "year": 1932},
            "Moby Dick": {"author": "Herman Melville", "year": 1851},
            "War and Peace": {"author": "Leo Tolstoy", "year": 1869}
        }
        
        # Оновлюємо словник data новими книгами
        data.update(new_books)

        # Запис у новий CSV файл
        with open('books_updated.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
            writer.writeheader()
            for title, info in data.items():
                writer.writerow({"title": title, "author": info["author"], "year": info["year"]})
        
        print("CSV файл 'books_updated.csv' успішно створено.")
        
    except FileNotFoundError:
        print("Помилка: Файл 'books.json' не знайдено.")
    except json.JSONDecodeError:
        print("Помилка: Не вдалося декодувати JSON.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

# Виконання
create_csv_file()
csv_to_json()
json_to_csv_with_new_rows()
