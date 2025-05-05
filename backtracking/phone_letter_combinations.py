"""
Комбинации букв

средне
решено

Дана строка s, содержащая цифры от 2 до 9.

Нужно вернуть все возможные комбинации букв, которые могли получиться при нажатии на эти цифры на телефоне,
в порядке, соответствующем цифрам в строке s. Ответ можно вернуть в любом порядке.


Пример 1:

Ввод: s = "28"
Вывод: ["at","au","av","bt","bu","bv","ct","cu","cv"]

Пример 2:

Ввод: s = ""
Вывод: []

Пример 3:

Ввод: s = "7"
Вывод: ["p","q","r","s"]

Ограничения:

len(s) >= 0
"""

from typing import *

def generate_combinations(s: str) -> List[str]:
    if len(s) == 0:
        return []
    mapping = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    res = []
    n = len(s)

    def backtrack(idx: int, curr: List[str], n: int):
        if len(curr) == n:
            res.append("".join(curr[:]))
            return

        for char in mapping[s[idx]]:
            curr.append(char)
            backtrack(idx+1, curr, n)
            curr.pop()

    backtrack(0, [], n)
    return res

if __name__ == "__main__":
    ex1 = "28"
    ex2 = ""
    ex3 = "7"

    ans1 = generate_combinations(ex1)
    ans2 = generate_combinations(ex2)
    ans3 = generate_combinations(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Оценка сложности

Время: O(n*4ⁿ), где n длина строки s
Память: O(n*4ⁿ), где n длина строки s
"""

# Эталон:
from typing import List

def bruteforce(index: int, s: str, current_combination: List[str], all_combinations: List[str]):
    # Если дошли до конца строки, добавляем текущую комбинацию в результат
    if index == len(s):
        all_combinations.append("".join(current_combination))
        return

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    # Получаем текущую цифру
    digit = s[index]

    # Перебираем все буквы, соответствующие текущей цифре
    for letter in phone_map[digit]:
        # Добавляем букву в текущую комбинацию
        current_combination.append(letter)
        # Рекурсивно перебираем оставшиеся цифры
        bruteforce(index + 1, s, current_combination, all_combinations)
        # Убираем букву, чтобы попробовать следующую
        current_combination.pop()


def generate_combinations(s: str) -> List[str]:
    # Возвращает все комбинации букв для заданных цифр (рекурсивный способ).
    if len(s) == 0:
        return []

    # Результирующий список всех комбинаций
    result = []
    # Запускаем рекурсивный перебор
    bruteforce(0, s, [], result)
    return result