import random

# 1️⃣ Функція для генерації текстового файлу
def generate_text_file(filename="text.txt", lines=100, chars_per_line=120):
    letters = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя "
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(lines):
            line = "".join(random.choice(letters) for _ in range(chars_per_line))
            f.write(line + "\n")

# 2️⃣ Генератор пар букв
def letter_pairs_generator(filename="text.txt"):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            pairs = []
            for i in range(len(line) - 1):
                if line[i] == " " or line[i+1] == " ":
                    continue
                if line[i] == "у" and line[i+1] == "н":
                    continue
                pairs.append(line[i] + line[i+1])
            for i in range(0, len(pairs), 3):
                yield pairs[i:i+3]

# 3️⃣ Точка входу
if __name__ == "__main__":
    generate_text_file()           # створює text.txt
    gen = letter_pairs_generator("text.txt")
    for _ in range(10):           # виводимо перші 10 груп по 3 пари
        print(next(gen))