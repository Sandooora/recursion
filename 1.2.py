def reverse_string_tail_recursion(s, reversed_s=""):
    # Базовий випадок: якщо рядок порожній, повертаємо зворотний рядок
    if s == "":
        return reversed_s
    # Рекурсивний виклик: додаємо перший символ до результату
    return reverse_string_tail_recursion(s[1:], s[0] + reversed_s)

# Запитуємо користувача ввести слово
input_string = input("Введіть слово: ")
output_string = reverse_string_tail_recursion(input_string)
print("Зворотне слово:", output_string)
