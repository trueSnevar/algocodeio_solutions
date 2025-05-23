"""
URL-ификация строки

средне
решено

Дан список s, представляющий URL-адрес (буквы и пробелы).
Нужно заменить все пробелы в первых k символах на "%20", используя свободное место в конце списка,
и вернуть изменённый список s в качестве результата.

Пример 1:

Ввод:
    s = ["h","e","l","l","o"," ","w","o","r","l","d","#","#"], k = 11
Вывод:
    ["h","e","l","l","o","%","2","0","w","o","r","l","d"]

Объяснение:
    Исходная строка "hello world"
    Преобразуем каждый пробел в "%20" → "hello%20world"

Пример 2:

Ввод:
    s = ["a"," ","b"," "," ","c","#","#","#","#","#","#"], k = 6
Вывод:
    ["a","%","2","0","b","%","2","0","%","2","0","c"]

Объяснение:
    Первые 6 символов образуют строку "a b c"
    Замена пробелов → "a%20b%20%20c"

Ограничения:
- len(s) ≥ 1
- В списке s есть достаточно места ('#') для замены всех пробелов на "%20"
"""
from typing import List


def urlify(s: List[str], k: int) -> List[str]:
    """
    Заменяет все пробелы в первых k символах списка s на "%20".
    Работа производится in-place с использованием двух указателей.
    Возвращает модифицированный список s.
    """
    slow = len(s) - 1
    fast = k - 1

    while fast >= 0:
        if s[fast] == " ":
            s[slow] = '0'
            s[slow - 1] = '2'
            s[slow - 2] = '%'
            slow -= 3
            fast -= 1
        else:
            s[slow] = s[fast]
            slow -= 1
            fast -= 1
    return s

if __name__ == "__main__":
    # Пример 1
    s1 = ["h","e","l","l","o"," ","w","o","r","l","d","#","#"]
    print(urlify(s1, 11))  # ['h','e','l','l','o','%','2','0','w','o','r','l','d']

    # Пример 2
    s2 = ["a"," ","b"," "," ","c","#","#","#","#","#","#"]
    print(urlify(s2, 6))   # ['a','%','2','0','b','%','2','0','%','2','0','c']

"""
Оценка сложности

Время: O(n), где n - длина строки s
Память: O(1)
"""

