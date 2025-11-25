import requests         # Робота з веб-запитами
import numpy            # Робота з масивами та числами
import pandas           # Таблиці та аналітика даних
import matplotlib.pyplot as plt  # Побудова графіків
import pyjokes          # Генерує жарти англійською
import emoji            # Додає емодзі до тексту
import colorama         # Кольоровий текст у терміналі
import tqdm             # Прогрес-бар у циклах
import faker            # Генерує фейкові дані (імена, адреси)
import PIL           # Робота з зображеннями

# Функції з try для 5 бібліотек

def test_requests():
    """requests — для відправки запитів до сайтів"""
    try:
        response = requests.get("https://api.github.com")
        print("requests працює! Статус:", response.status_code)
    except Exception as e:
        print("Помилка у requests:", e)


def test_numpy():
    """numpy — робота з масивами"""
    try:
        import numpy as np
        arr = np.array([2, 4, 6, 8])
        print("numpy працює! Середнє значення:", np.mean(arr))
    except Exception as e:
        print("Помилка у numpy:", e)


def test_pandas():
    """pandas — створення таблиць"""
    try:
        data = {"Ім'я": ["Анна", "Богдан"], "Вік": [18, 19]}
        df = pandas.DataFrame(data)
        print("pandas працює! Таблиця:")
        print(df)
    except Exception as e:
        print("Помилка у pandas:", e)


def test_matplotlib():
    """matplotlib — побудова графіків"""
    try:
        x = [1, 2, 3, 4, 5]
        y = [i**2 for i in x]
        plt.plot(x, y, marker="o")
        plt.title("Простий графік")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
        print("matplotlib працює! Графік побудовано.")
    except Exception as e:
        print("Помилка у matplotlib:", e)


def test_pyjokes():
    """pyjokes — бібліотека для жартів"""
    try:
        joke = pyjokes.get_joke()
        print("pyjokes працює! Ось жарт:")
        print(joke)
    except Exception as e:
        print("Помилка у pyjokes:", e)


# Головна функція

if __name__ == "__main__":
    print("=== Перевірка бібліотек ===\n")
    test_requests()
    test_numpy()
    test_pandas()
    test_matplotlib()
    test_pyjokes()
  
