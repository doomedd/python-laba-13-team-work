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

